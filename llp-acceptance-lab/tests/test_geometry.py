import numpy as np
import pytest

from llp_acceptance.decay import decay_probability_between
from llp_acceptance.geometry import (
    CALORIMETER_TOY,
    Region1D,
    probabilities_in_regions,
    probability_in_region,
)


def test_region_probability_matches_decay_probability_between() -> None:
    region = Region1D("test_region", 1.0, 4.0)
    L_lab = 2.0

    assert probability_in_region(region, L_lab) == pytest.approx(
        decay_probability_between(1.0, 4.0, L_lab)
    )


def test_probability_in_region_supports_array_lab_lengths() -> None:
    L_lab = np.array([1.0, 2.0, 10.0])
    probabilities = probability_in_region(CALORIMETER_TOY, L_lab)

    assert isinstance(probabilities, np.ndarray)
    assert probabilities.shape == L_lab.shape
    assert np.all(probabilities >= 0.0)


def test_probabilities_in_regions_returns_names() -> None:
    regions = [Region1D("near", 0.0, 1.0), Region1D("far", 10.0, 20.0)]

    result = probabilities_in_regions(regions, L_lab=5.0)

    assert set(result) == {"near", "far"}


@pytest.mark.parametrize(
    ("name", "L_min", "L_max"),
    [
        ("", 0.0, 1.0),
        ("negative_min", -1.0, 1.0),
        ("inverted", 2.0, 1.0),
        ("nan_max", 0.0, np.nan),
    ],
)
def test_invalid_region_definitions_raise(
    name: str,
    L_min: float,
    L_max: float,
) -> None:
    with pytest.raises(ValueError):
        Region1D(name, L_min, L_max)
