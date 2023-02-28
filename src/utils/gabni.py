"""
GABNI
~~~
Python implementation of GABNI for a Boolean network inference from gene
expression data.

Author: Kenneth Schackart <schackartk1@gmail.com>
"""

import random
from functools import partial


# -------------------------------------------------------------------------------------
def calc_adjusted_fitness(
    fitness: float, max_fitness: float, min_fitness: float, h: float
) -> float:
    """
    Calculate adjusted fitness. This linear adjustment assigns the selection
    probabilty of the best chromosome to `h+1` times that of the worst chromosome
    in the population.

    Arguments:
    `fitness`: Individual chromosome fitness score
    `max_fitness`: Maximum fitness value in the population
    `min_fitness`: Minimum fitness value in the population
    `h`: Adjustment parameter
    """

    alpha = h / (max_fitness - min_fitness)
    beta = 1 - alpha * min_fitness

    return (alpha * fitness) + beta


# -------------------------------------------------------------------------------------
def test_calc_adjusted_fitness() -> None:
    """Test calc_adjusted_fitness()"""

    # Lowest score becomes 1 (baseline)
    assert calc_adjusted_fitness(1.0, 2.0, 1.0, 5.0) == 1.0
    assert calc_adjusted_fitness(3.0, 5.0, 3.0, 3.0) == 1.0

    # Highest score becomes h+1 times lowest score
    assert calc_adjusted_fitness(2.0, 2.0, 1.0, 2.0) == 3.0
    assert calc_adjusted_fitness(5.0, 5.0, 3.0, 3.0) == 4.0


# -------------------------------------------------------------------------------------
def calc_adjusted_fitnesses(fitnesses: list[float], h: float):
    """
    Calculate adjusted fitnesses for all chromosomes in population. The best chromosome
    will have an adjusted fitness `h+1` times that of the worst chromosome
    in the population.

    Arguments:
    `fitnesses`: Array of fitnesses
    `h`: Adjustment parameter
    """

    max_fitness = max(fitnesses)
    min_fitness = min(fitnesses)

    partial_fitness_adjustment = partial(
        calc_adjusted_fitness, max_fitness=max_fitness, min_fitness=min_fitness, h=h
    )

    return [partial_fitness_adjustment(f) for f in fitnesses]


# -------------------------------------------------------------------------------------
def test_calc_adjusted_fitnesses() -> None:
    """Test calc_adjusted_fitnesses()"""

    # Max and min are properly adjusted
    # Min becomes 1.0
    # Max becomes h+1*min
    h = 3.0
    fitnesses = [5.0, 3.0]
    adj_fitnesses = [4.0, 1.0]

    assert calc_adjusted_fitnesses(fitnesses, h) == adj_fitnesses

    # Given evenly spaces input, output is evenly spaced
    h = 4.0
    fitnesses = [5.0, 4.0, 3.0]
    adj_fitnesses = [5.0, 3.0, 1.0]

    assert calc_adjusted_fitnesses(fitnesses, h) == adj_fitnesses


# -------------------------------------------------------------------------------------
def crossover(parent_1: list[int], parent_2: list[int]) -> tuple(list[int]):
    """
    Conduct a crossover between to parent chromosomes, yeilding two offspring
    chromosomes.

    Arguments:
    `parent_1`: Parent 1 chromosome
    `parent_2`: Parent 2 chromosome
    """

    offspring_1 = []
    offspring_2 = []

    for par_1_gene, par_2_gene in zip(parent_1, parent_2):
        if par_1_gene == par_2_gene:
            offspring_1.append(par_1_gene)
            offspring_2.append(par_2_gene)
        else:
            genes = [par_1_gene, par_2_gene]
            offspring_1.append(random.choice(genes))
            offspring_2.append(random.choice(genes))

    return offspring_1, offspring_2


# -------------------------------------------------------------------------------------
def test_crossover() -> None:
    """Test crossover()"""

    # If parent chromosomes are identical, offspring inherit exactly
    parent_1 = [1, 1, 1, 0, 0, 1]
    parent_2 = [1, 1, 1, 0, 0, 1]

    assert crossover(parent_1, parent_2) == ([1, 1, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1])

    # Crossover occurs for differing genes
    parent_1 = [1, 0, 1, 0, 0, 0]
    parent_2 = [1, 1, 0, 0, 1, 1]

    random.seed(951)
    assert crossover(parent_1, parent_2) == ([1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 1, 0])
