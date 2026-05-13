import numpy as np
import pytest

from llp_acceptance.decay import (
    decay_pdf,
    decay_probability_before,
    decay_probability_between,
    survival_probability,
)


def test_decay_probability_over_full_positive_axis_is_one() -> None:
    assert decay_probability_between(0.0, np.inf, L_lab=3.0) == pytest.approx(1.0)


def test_decay_probability_between_is_non_negative() -> None:
    probability = decay_probability_between(1.0, 4.0, L_lab=2.0)

    assert probability >= 0.0


def test_probabilities_partition_unity() -> None:
    L1 = 1.0
    L2 = 4.0
    L_lab = 2.5

    total = (
        decay_probability_before(L1, L_lab)
        + decay_probability_between(L1, L2, L_lab)
        + survival_probability(L2, L_lab)
    )

    assert total == pytest.approx(1.0)


def test_far_region_is_suppressed_for_short_lab_decay_length() -> None:
    probability = decay_probability_between(100.0, 500.0, L_lab=1.0)

    assert probability < 1e-40


def test_detector_scale_lab_decay_length_gives_appreciable_probability() -> None:
    probability = decay_probability_between(1.0, 4.0, L_lab=2.0)

    assert probability > 0.1


def test_close_interval_is_numerically_stable() -> None:
    L1 = 1.0
    L2 = 1.0 + 1e-10
    L_lab = 1e6

    probability = decay_probability_between(L1, L2, L_lab)

    assert probability > 0.0
    assert probability == pytest.approx((L2 - L1) / L_lab, rel=1e-6)


def test_decay_pdf_matches_exponential_density() -> None:
    assert decay_pdf(0.0, L_lab=5.0) == pytest.approx(0.2)


@pytest.mark.parametrize(
    ("L1", "L2", "L_lab"),
    [
        (-1.0, 2.0, 1.0),
        (1.0, 1.0, 1.0),
        (1.0, 2.0, 0.0),
    ],
)
def test_invalid_decay_inputs_raise(L1: float, L2: float, L_lab: float) -> None:
    with pytest.raises(ValueError):
        decay_probability_between(L1, L2, L_lab)
