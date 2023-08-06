from __future__ import print_function, division

import argparse
import json
import random

import os

import itertools

import pysmt.shortcuts as smt
import time

import problem
import parse
from smt_print import pretty_print
from learner import Learner
from smt_check import SmtChecker
from smt_check import test as smt_test


class InsufficientBalanceError(RuntimeError):
    def __init__(self, partial_samples=None):
        self.partial_samples = partial_samples


class SyntheticProblem(object):
    def __init__(self, theory_problem, cnf_or_dnf, formula_count, terms_per_formula, half_space_count, error_percent=0):
        self.theory_problem = theory_problem
        self.cnf_or_dnf = cnf_or_dnf
        self.formula_count = formula_count
        self.terms_per_formula = terms_per_formula
        self.half_space_count = half_space_count
        self.error_percent = error_percent

    @property
    def bool_count(self):
        return len(self.theory_problem.domain.bool_vars)

    @property
    def real_count(self):
        return len(self.theory_problem.domain.real_vars)

    @property
    def k(self):
        return self.formula_count

    @property
    def h(self):
        return self.half_space_count

    @property
    def literals(self):
        return self.terms_per_formula

    def get_data(self, sample_count, max_ratio):
        samples = get_problem_samples(self.theory_problem, sample_count, max_ratio)
        return SyntheticData(self, samples)

    @staticmethod
    def create(domain, cnf_or_dnf, formula_count, terms_per_formula, half_space_count, name):
        if cnf_or_dnf == "cnf":
            theory = generate_cnf(domain, formula_count, terms_per_formula, half_space_count)
        elif cnf_or_dnf == "dnf":
            theory = generate_dnf(domain, formula_count, terms_per_formula, half_space_count)
        elif cnf_or_dnf == "cnf_strict":
            theory = generate_strict_cnf(domain, formula_count, terms_per_formula, half_space_count)
        else:
            raise RuntimeError("cnf_or_dnf was neither 'cnf' nor 'dnf'")
        theory_problem = problem.Problem(domain, theory, name)
        return SyntheticProblem(theory_problem, cnf_or_dnf, formula_count, terms_per_formula, half_space_count)


class Data(object):
    def __init__(self, theory_problem, samples):
        self.theory_problem = theory_problem
        self.samples = samples


class SyntheticData(object):
    def __init__(self, synthetic_problem, samples):
        self.synthetic_problem = synthetic_problem
        self.samples = samples


def export_synthetic_problem(synthetic_problem, to_str=True):
    """
    :type synthetic_problem: SyntheticProblem
    :type to_str: bool
    """
    flat = {
        "problem": problem.export_problem(synthetic_problem.theory_problem, to_str=False),
        "cnf_or_dnf": synthetic_problem.cnf_or_dnf,
        "formula_count": synthetic_problem.formula_count,
        "terms_per_formula": synthetic_problem.terms_per_formula,
        "half_space_count": synthetic_problem.half_space_count,
        "error_percent": synthetic_problem.error_percent,
    }
    return json.dumps(flat) if to_str else flat


def import_synthetic_problem(flat):
    theory_problem = problem.import_problem(flat["problem"])
    cnf_or_dnf = str(flat["cnf_or_dnf"])
    formula_count = int(flat["formula_count"])
    terms_per_formula = int(flat["terms_per_formula"])
    half_space_count = int(flat["half_space_count"])
    error_percent = int(flat.get("error_percent", 0))
    return SyntheticProblem(theory_problem, cnf_or_dnf, formula_count, terms_per_formula, half_space_count,
                            error_percent)


def export_data(data, to_str=True):
    """
    :type data: Data
    :type to_str: bool
    """
    flat_samples = []
    for row, label in data.samples:
        flat_samples.append({"instance": row, "label": label})

    flat = {
        "problem": problem.export_problem(data.theory_problem, to_str=False),
        "samples": flat_samples,
    }
    return json.dumps(flat) if to_str else flat


def import_data(flat):
    theory_problem = problem.import_problem(flat["problem"])
    samples = []
    for example in flat["samples"]:
        samples.append((example["instance"], example["label"]))
    return Data(theory_problem, samples)


def export_synthetic_data(synthetic_data, to_str=True):
    """
    :type synthetic_data: SyntheticData
    :type to_str: bool
    """
    flat_samples = []
    synthetic_problem = synthetic_data.synthetic_problem
    for row, label in synthetic_data.samples:
        flat_samples.append({"instance": row, "label": label})

    flat = {
        "synthetic_problem": export_synthetic_problem(synthetic_problem, to_str=False),
        "samples": flat_samples,
    }
    return json.dumps(flat) if to_str else flat


def import_synthetic_data(flat):
    synthetic_problem = import_synthetic_problem(flat["synthetic_problem"])
    samples = []
    for example in flat["samples"]:
        samples.append((example["instance"], example["label"]))
    return SyntheticData(synthetic_problem, samples)


def generate_cnf(domain, and_count, or_count, half_space_count):
    formulas = get_formulas(domain, and_count, or_count, half_space_count)
    return smt.And(smt.Or(*formula) for formula in formulas)


def generate_strict_cnf(domain, and_count, or_count, half_space_count):
    half_spaces = [generate_half_space_sample(domain, len(domain.real_vars)) for _ in range(half_space_count)]
    candidates = [domain.get_symbol(v) for v in domain.bool_vars] + half_spaces
    candidates += [smt.Not(c) for c in candidates]

    formulas = []
    iteration = 0
    max_iterations = 100 * and_count
    while len(formulas) < and_count:
        if iteration >= max_iterations:
            return generate_strict_cnf(domain, and_count, or_count, half_space_count)
        iteration += 1
        formula_candidates = [c for c in candidates]
        random.shuffle(formula_candidates)
        formula = []
        try:
            while len(formula) < or_count:
                next_term = formula_candidates.pop(0)
                if len(formula) == 0 or smt.is_sat(~smt.Or(*formula) & next_term):
                    formula.append(next_term)
        except IndexError:
            continue
        if len(formulas) == 0 or smt.is_sat(~smt.And(*[smt.Or(*f) for f in formulas]) & smt.Or(*formula)):
            formulas.append(formula)
    return smt.And(*[smt.Or(*f) for f in formulas])


def generate_dnf(domain, or_count, and_count, half_space_count):
    formulas = get_formulas(domain, and_count, or_count, half_space_count)
    return smt.Or(smt.And(*formula) for formula in formulas)


def get_formulas(domain, formula_count, terms_per_formula, half_space_count):
    half_spaces = [generate_half_space_sample(domain, len(domain.real_vars)) for _ in range(half_space_count)]
    candidates = [domain.get_symbol(v) for v in domain.bool_vars] + half_spaces
    return [
        list(random.sample(candidates, terms_per_formula))
        for _ in range(formula_count)
    ]


def generate_half_space(domain, real_count):
    coefficients = [smt.Real(random.random() * 2 - 1) * domain.get_symbol(domain.real_vars[i]) for i in
                    range(real_count)]
    return smt.LE(smt.Plus(*coefficients), smt.Real(random.random() * 2 - 1))


def generate_half_space_sample(domain, real_count):
    samples = [get_sample(domain) for _ in range(real_count)]
    coefficients, offset = Learner.fit_hyperplane(domain, samples)
    coefficients = [smt.Real(float(coefficients[i][0])) * domain.get_symbol(domain.real_vars[i]) for i in
                    range(real_count)]
    if random.random() < 0.5:
        return smt.Plus(*coefficients) <= offset
    else:
        return smt.Plus(*coefficients) >= offset


def generate_domain(bool_count, real_count):
    variables = ["b{}".format(i) for i in range(bool_count)] + ["r{}".format(i) for i in range(real_count)]
    var_types = dict()
    var_domains = dict()
    for i, v in enumerate(variables):
        if i < bool_count:
            var_types[v] = smt.BOOL
        else:
            var_types[v] = smt.REAL
            var_domains[v] = (0, 1)

    return problem.Domain(variables, var_types, var_domains)


def evaluate_assignment(test_problem, assignment):
    """
    Calculate if the given assignment satisfies the problem formula
    :param test_problem: The problem containing the formula and domain
    :param assignment: An assignment to (all) the domain variables
    :return: True iff the assignment satisfies the problem formula
    """
    return SmtChecker(assignment).walk_smt(test_problem.theory)


def get_labeled_sample(test_problem):
    """
    Sample n instances for the given problem
    :param test_problem: The problem to sample from
    :return: A sample (dictionary mapping variable names to values) and its label (True iff the sample satisfies the
    theory and False otherwise)
    """
    instance = get_sample(test_problem.domain)
    return instance, evaluate_assignment(test_problem, instance)


def get_sample(domain):
    instance = dict()
    for v in domain.variables:
        if domain.var_types[v] == smt.REAL:
            lb, ub = domain.var_domains[v]
            instance[v] = random.uniform(lb, ub)
        elif domain.var_types[v] == smt.BOOL:
            instance[v] = True if random.random() < 0.5 else False
        else:
            raise RuntimeError("Unknown variable type {} for variable {}", domain.var_types[v], v)
    return instance


def get_problem_samples(test_problem, sample_count, max_ratio):
    samples = []
    pos_count = 0
    neg_count = 0
    minimal_count = sample_count * min(max_ratio, 1 - max_ratio)
    for i in range(sample_count):
        instance, label = get_labeled_sample(test_problem)
        samples.append((instance, label))
        if label:
            pos_count += 1
        else:
            neg_count += 1
        remaining = sample_count - (pos_count + neg_count)

        # Approximate check
        # if pos_count + neg_count == 20:
        #     current_ratio = max(pos_count, neg_count) / float(pos_count + neg_count)
        #     if current_ratio > max_ratio + 0.1:
        #         print("Triggered")
        #         raise InsufficientBalanceError()

        # Definite check
        if pos_count + remaining < minimal_count or neg_count + remaining < minimal_count:
            # print("Definite test")
            raise InsufficientBalanceError()
    return samples


def get_synthetic_problem_name(prefix, bool_count, real_count, cnf_or_dnf, k, l_per_term, h, sample_count, seed,
                               ratio_percent, error_percent, i=None):
    name = "{prefix}_{bc}_{rc}_{type}_{fc}_{tpf}_{hc}_{sc}_{seed}_{ratio}" \
        .format(bc=bool_count, rc=real_count, type=cnf_or_dnf, fc=k, tpf=l_per_term, hc=h, sc=sample_count,
                prefix=prefix, seed=seed, ratio=int(ratio_percent))
    if error_percent > 0:
        name += "_{error}".format(error=int(error_percent))
    if i is not None:
        name = name + "_" + str(i)
    return name


class GeneratorError(RuntimeError):
    pass


class Generator(object):
    def __init__(self, bool_count, real_count, bias, k, l, h, sample_count, max_ratio, errors, seed, prefix):
        self.domain = generate_domain(bool_count, real_count)
        self.bias = bias
        self.k = k
        self.l = l
        self.h = h
        self.sample_count = sample_count
        self.max_ratio = max_ratio
        self.errors = errors
        self.seed = seed
        self.prefix = prefix + "_r"
        self.max_tries = 10000

    @property
    def bool_count(self):
        return len(self.domain.bool_vars)

    @property
    def real_count(self):
        return len(self.domain.real_vars)

    def symbol(self, var_name):
        return self.domain.get_symbol(var_name)

    def test_ratio(self, bits):
        max_ratio = max(self.max_ratio, 1 - self.max_ratio)
        return (1 - max_ratio) <= bits.count() / self.sample_count <= max_ratio

    def get_name(self, i):
        b = self.bool_count
        r = self.real_count
        ratio = self.max_ratio * 100
        k, l, h = self.k, self.l, self.h
        return get_synthetic_problem_name(self.prefix, b, r, self.bias, k, l, h, self.sample_count, self.seed, ratio, i)

    def get_samples(self):
        return [get_sample(self.domain) for _ in range(self.sample_count)]

    def get_half_spaces(self, samples):
        from bitarray import bitarray

        half_spaces = []
        print("Generating half spaces: ", end="")
        if self.real_count > 0:
            while len(half_spaces) < self.h:
                half_space = generate_half_space_sample(self.domain, self.real_count)
                bits = bitarray([smt_test(half_space, sample) for sample in samples])
                if True or self.test_ratio(bits):
                    half_spaces.append((half_space, bits))
                    print("y", end="")
                else:
                    print("x", end="")
        print()
        return half_spaces

    def get_term(self, literal_pool):
        from bitarray import bitarray

        print("Generate term: ", end="")
        for i in range(self.max_tries):
            literals = random.sample(literal_pool, self.l)

            term = smt.Or(*list(zip(*literals))[0])

            covered = bitarray(self.sample_count)
            covered.setall(False)
            significant_literals = 0
            for _, bits in literals:
                prev_size = covered.count()
                covered |= bits
                if (covered.count() - prev_size) / self.sample_count >= 0.05:
                    significant_literals += 1

            if significant_literals == self.l:  # & test_ratio(covered):
                print("y", end="")
                print()
                return term, covered
            else:
                print("x", end="")
        print(" Failed after {} tries".format(self.max_tries))
        raise GeneratorError()

    def get_formula(self, name, literal_pool):
        from bitarray import bitarray

        print("Generate formula:")
        for i in range(self.max_tries):
            terms = [self.get_term(literal_pool) for _ in range(self.k)]
            formula = smt.And(*list(zip(*terms))[0])

            covered = bitarray(self.sample_count)
            covered.setall(True)
            significant_terms = 0
            for _, bits in terms:
                prev_size = covered.count()
                covered &= bits
                if (prev_size - covered.count()) / self.sample_count >= 0.05:
                    significant_terms += 1

            if significant_terms == self.k and self.test_ratio(covered):
                print("y({:.2f})".format(covered.count() / self.sample_count), end="")
                data_set = self.get_data_set(name, formula)
                data_set_positives = bitarray([example[1] for example in data_set.samples])
                if self.test_ratio(data_set_positives):
                    print("c({:.2f})".format(data_set_positives.count() / self.sample_count))
                    return data_set
                else:
                    print("r({:.2f})".format(data_set_positives.count() / self.sample_count))
            else:
                if not self.test_ratio(covered):
                    print("Ratio not satisfied")
                else:
                    print("Not enough significant terms")
        print("Failed to generate formula after {} tries".format(self.max_tries))
        raise GeneratorError()

    def get_data_set(self, name, formula):
        theory_problem = problem.Problem(self.domain, formula, name)
        synthetic_problem = SyntheticProblem(theory_problem, "cnf", self.k, self.l, self.h)
        data_set = synthetic_problem.get_data(self.sample_count, 1)
        return data_set

    def generate(self, n):
        from bitarray import bitarray

        count = 0
        i = 0
        while count < n and i < self.max_tries:
            print("Generate data set {}".format(count))
            i += 1
            samples = self.get_samples()

            half_spaces = self.get_half_spaces(self.get_samples())

            bool_literals = [(self.symbol(v), bitarray([sample[v] for sample in samples])) for v in self.domain.bool_vars]
            literal_pool = half_spaces + bool_literals
            literal_pool += [(smt.Not(l), ~bits) for l, bits in literal_pool]

            try:
                data_set = self.get_formula(self.get_name(i), literal_pool)
                count += 1
                yield data_set
            except GeneratorError:
                continue
        if i == self.max_tries:
            print("Failed to generate enough data sets after {} tries".format(self.max_tries))


def generate_synthetic_data_sampling(data_sets_per_setting, bool_count, real_count, cnf_or_dnf, k, l_per_term, h,
                                     sample_count, max_ratio, seed, prefix="synthetics"):
    def test_ratio(_indices):
        return (1 - max_ratio) * sample_count <= len(_indices) <= max_ratio * sample_count

    data_set_count = 0
    domain = generate_domain(bool_count, real_count)
    while data_set_count < data_sets_per_setting:
        name = get_synthetic_problem_name(prefix, bool_count, real_count, cnf_or_dnf, k, l_per_term, h, sample_count,
                                          seed, max_ratio * 100, data_set_count)
        samples = [get_sample(domain) for _ in range(sample_count)]

        half_spaces = []
        print("Generating half spaces: ", end="")
        if real_count > 0:
            while len(half_spaces) < h:
                half_space = generate_half_space_sample(domain, real_count)
                indices = {i for i in range(sample_count) if smt_test(half_space, samples[i])}
                if True or test_ratio(indices):
                    half_spaces.append((half_space, indices))
                    print("y", end="")
                else:
                    print("x", end="")
        print()

        bool_literals = [(domain.get_symbol(v), {i for i in range(sample_count) if samples[i][v]})
                         for v in domain.bool_vars]

        literal_pool = half_spaces + bool_literals
        literal_pool += [(smt.Not(l), {i for i in range(sample_count)} - indices) for l, indices in literal_pool]
        random.shuffle(literal_pool)

        term_pool = []
        print("Generating terms: ", end="")
        for literals in itertools.combinations(literal_pool, l_per_term):
            term = smt.Or(*[t[0] for t in literals])
            covered = set()
            all_matter = True
            for _, indices in literals:
                prev_size = len(covered)
                covered |= indices
                if (len(covered) - prev_size) / sample_count < 0.05:
                    all_matter = False

            if all_matter:  # & test_ratio(covered):
                term_pool.append((term, covered))
                print("y", end="")
            else:
                print("x", end="")
        print()

        print("Generating formulas: ", end="")
        random.shuffle(term_pool)
        counter = 0
        max_tries = 10000
        for terms in itertools.combinations(term_pool, k):
            if counter >= max_tries:
                print("Restart")
                break
            formula = smt.And(*[t[0] for t in terms])
            covered = {i for i in range(sample_count)}
            all_matter = True
            for _, indices in terms:
                prev_size = len(covered)
                covered &= indices
                if prev_size == len(covered):
                    all_matter = False
            if all_matter & test_ratio(covered):
                print("y({:.2f})".format(len(covered) / sample_count), end="")
                synthetic_problem = SyntheticProblem(problem.Problem(domain, formula, name), "cnf", k, l_per_term, h)
                data_set = synthetic_problem.get_data(sample_count, 1)
                new_sample_positives = [sample for sample in data_set.samples if sample[1]]
                if test_ratio(new_sample_positives):
                    print("c({:.2f})".format(len(new_sample_positives) / sample_count))
                    data_set_count += 1
                    yield data_set
                    break
                else:
                    print("r({:.2f})".format(len(new_sample_positives) / sample_count), end="")
            else:
                print("x", end="")
            print(" ", end="")
            counter += 1
        print()


def generate_synthetic_data(data_sets_per_setting, bool_count, real_count, cnf_or_dnf, formula_count, terms_per_formula,
                            half_space_count, sample_count, max_ratio, prefix="synthetic"):
    data_set_count = 0
    domain = generate_domain(bool_count, real_count)
    while data_set_count < data_sets_per_setting:
        try:
            name = "{prefix}_{bc}_{rc}_{type}_{fc}_{tpf}_{hc}_{sc}_{i}" \
                .format(bc=bool_count, rc=real_count, type=cnf_or_dnf, fc=formula_count, tpf=terms_per_formula,
                        hc=half_space_count, sc=sample_count, i=data_set_count, prefix=prefix)
            data = SyntheticProblem.create(domain, cnf_or_dnf, formula_count, terms_per_formula, half_space_count,
                                           name).get_data(sample_count, max_ratio)
            data_set_count += 1
            yield data
        except InsufficientBalanceError:
            pass


def import_synthetic_data_files(directory, prefix):
    for filename in os.listdir(directory):
        if filename.startswith(prefix) and filename.endswith(".txt"):
            with open(os.path.join(directory, filename), "r") as f:
                yield import_synthetic_data(json.load(f))


def generate(data_sets, prefix, b_count, r_count, cnf_or_dnf, k, l_per_term, h, sample_count, ratio_percent,
             data_dir, plot_dir=None):
    seed = hash(time.time())
    random.seed(seed)

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    i = 0
    for data_set in generate_synthetic_data_sampling(data_sets, b_count, r_count, cnf_or_dnf, k, l_per_term, h,
                                                    sample_count, ratio_percent / 100, seed, prefix):
        data_file = os.path.join(data_dir, "{}.txt".format(data_set.synthetic_problem.theory_problem.name))
        with open(data_file, "w") as f:
            print(export_synthetic_data(data_set), file=f)

        if plot_dir is not None and b_count == 0 and r_count == 2:
            import plotting
            dir_name = get_synthetic_problem_name(prefix, b_count, r_count, cnf_or_dnf, k, l_per_term, h, sample_count,
                                                  seed, ratio_percent)
            domain = data_set.synthetic_problem.theory_problem.domain
            output_dir = os.path.join(plot_dir, dir_name)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            indices = list(range(len(data_set.samples)))
            name = os.path.join(output_dir, "overview_{}".format(i))
            plotting.draw_border_points(domain.real_vars[0], domain.real_vars[1], data_set.samples, indices, name)

        i += 1


def generate_random(data_sets, prefix, b_count, r_count, bias, k, lits, h, sample_count, ratio_percent, error_percent,
                    data_dir, plot_dir=None):

    seed = hash(time.time())
    random.seed(seed)

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    i = 0
    ratio, errors = ratio_percent / 100, error_percent / 100
    producer = Generator(b_count, r_count, bias, k, lits, h, sample_count, ratio, errors,seed, prefix)
    for data_set in producer.generate(data_sets):
        data_file = os.path.join(data_dir, "{}.txt".format(data_set.synthetic_problem.theory_problem.name))
        with open(data_file, "w") as f:
            print(export_synthetic_data(data_set), file=f)

        if plot_dir is not None and b_count == 0 and r_count == 2:
            import plotting
            dir_name = get_synthetic_problem_name(prefix, b_count, r_count, bias, k, lits, h, sample_count,
                                                  seed, ratio_percent, error_percent)
            domain = data_set.synthetic_problem.theory_problem.domain
            output_dir = os.path.join(plot_dir, dir_name)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            indices = list(range(len(data_set.samples)))
            name = os.path.join(output_dir, "overview_{}".format(i))
            plotting.draw_border_points(domain.real_vars[0], domain.real_vars[1], data_set.samples, indices, name)

        i += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("data_dir")
    parser.add_argument("--data_sets", default=10, type=int)
    parser.add_argument("--prefix", default="synthetics")
    parser.add_argument("--bool_count", default=2, type=int)
    parser.add_argument("--real_count", default=2, type=int)
    parser.add_argument("--bias", default="cnf")
    parser.add_argument("--k", default=3, type=int)
    parser.add_argument("--literals", default=4, type=int)
    parser.add_argument("--h", default=7, type=int)
    parser.add_argument("--sample_count", default=1000, type=int)
    parser.add_argument("--ratio", default=90, type=int)
    parser.add_argument("-p", "--plot_dir", default=None)
    parsed = parser.parse_args()
    generate_random(parsed.data_sets, parsed.prefix, parsed.bool_count, parsed.real_count, parsed.bias, parsed.k,
             parsed.literals, parsed.h, parsed.sample_count, parsed.ratio, parsed.data_dir, parsed.plot_dir)
