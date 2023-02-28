"""
Metrics
~~~
Functions for calculating performance metrics

Authors: Kenneth Schackart <schackartk1@gmail.com>
"""


# -------------------------------------------------------------------------------------
def calc_precision(tp: int, fp: int) -> float:
    """
    Calculate Precision as tp / (tp + fp)

    Arguments:
    `tp`: Number of True Positives
    `fp`: Number of False Positives
    """

    if tp == 0 and fp == 0:
        return 1.0

    return tp / (tp + fp)


# -------------------------------------------------------------------------------------
def test_calc_precision() -> None:
    """Test calc_precision()"""

    # Returns 1 when inputs are zero
    assert calc_precision(0, 0) == 1.0

    # Works on good numbers
    assert calc_precision(5, 5) == 0.5
    assert calc_precision(15, 5) == 0.75
    assert calc_precision(10, 0) == 1.0


# -------------------------------------------------------------------------------------
def calc_recall(tp: int, fn: int) -> float:
    """
    Calculate Recall as tp / (tp + fn)

    Arguments:
    `tp`: Number of True Positives
    `fn`: Number of False Negatives
    """

    if tp == 0 and fn == 0:
        return 1.0

    return tp / (tp + fn)


# -------------------------------------------------------------------------------------
def test_calc_recall() -> None:
    """Test calc_precision()"""

    # Returns 1 when inputs are zero
    assert calc_recall(0, 0) == 1.0

    # Works on good numbers
    assert calc_recall(5, 5) == 0.5
    assert calc_recall(15, 5) == 0.75
    assert calc_recall(10, 0) == 1.0


# -------------------------------------------------------------------------------------
def calc_structural_accuracy(tp: int, tn: int, fp: int, fn: int) -> float:
    """
    Calculate Structural Accuracy as (tp + tn) / (tp + fp + fn + tn)

    Arguments:
    `tp`: Number of True Positives
    `tn`: Number of True Negatives
    `fp`: Number of False Positives
    `fn`: Number of False Negatives
    """

    if tp == 0 and tn == 0 and fp == 0 and fn == 0:
        return 1.0

    return (tp + tn) / (tp + fp + fn + tn)


# -------------------------------------------------------------------------------------
def test_calc_structural_accuracy() -> None:
    """Test calc_structural_accuracy()"""

    # Returns 1 when inputs are zero
    assert calc_structural_accuracy(0, 0, 0, 0) == 1.0

    # Works on good numbers
    assert calc_structural_accuracy(5, 5, 5, 5) == 0.5
    assert calc_structural_accuracy(15, 15, 5, 5) == 0.75
    assert calc_structural_accuracy(15, 15, 0, 0) == 1.0
