import scipy.stats as stats


def t_test(group_a, group_b):
    """Independent t-test for two groups."""
    return stats.ttest_ind(group_a, group_b, equal_var=False)


def chi_square_test(table):
    """Chi-square test for categorical association."""
    return stats.chi2_contingency(table)


def z_test(p1, p2, n1, n2):
    """Z-test for proportions (claim frequency)."""

    p_pool = (p1 * n1 + p2 * n2) / (n1 + n2)

    se = (p_pool * (1 - p_pool) * (1/n1 + 1/n2)) ** 0.5

    z = (p1 - p2) / se

    return z