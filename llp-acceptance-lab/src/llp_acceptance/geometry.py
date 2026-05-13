"""Toy detector regions for LLP decay-acceptance studies.

The regions in this module are one-dimensional intervals measured along the
LLP trajectory. They are deliberately idealized toy geometries, not dimensions
of any real detector.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

from .decay import decay_probability_between

FloatArray: TypeAlias = npt.NDArray[np.float64]
FloatLike: TypeAlias = float | FloatArray


@dataclass(frozen=True)
class Region1D:
    """One-dimensional toy detector region along an LLP trajectory.

    Parameters
    ----------
    name:
        Human-readable region name.
    L_min:
        Inner boundary along the trajectory, in meters.
    L_max:
        Outer boundary along the trajectory, in meters. It may be ``np.inf``.
    """

    name: str
    L_min: float
    L_max: float

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("Region name must be non-empty.")
        if not np.isfinite(self.L_min):
            raise ValueError("Region L_min must be finite.")
        if self.L_min < 0.0:
            raise ValueError("Region L_min must be non-negative.")
        if not (np.isfinite(self.L_max) or np.isposinf(self.L_max)):
            raise ValueError("Region L_max must be finite or positive infinity.")
        if not self.L_max > self.L_min:
            raise ValueError("Region L_max must be greater than L_min.")


INNER_TRACKER_TOY = Region1D("inner_tracker_toy", 0.01, 1.0)
CALORIMETER_TOY = Region1D("calorimeter_toy", 1.0, 4.0)
MUON_SYSTEM_TOY = Region1D("muon_system_toy", 4.0, 10.0)
FAR_DETECTOR_TOY = Region1D("far_detector_toy", 100.0, 500.0)

TOY_REGIONS_1D: tuple[Region1D, ...] = (
    INNER_TRACKER_TOY,
    CALORIMETER_TOY,
    MUON_SYSTEM_TOY,
    FAR_DETECTOR_TOY,
)


def probability_in_region(region: Region1D, L_lab: FloatLike) -> FloatLike:
    """Return the probability for an LLP to decay inside a toy 1D region.

    ``L_lab`` is the mean lab-frame decay length in meters. For a fixed
    ``beta*gamma`` and proper decay length ``ctau``, it is
    ``L_lab = beta*gamma*ctau``.
    """

    return decay_probability_between(region.L_min, region.L_max, L_lab)


def probabilities_in_regions(
    regions: Iterable[Region1D],
    L_lab: FloatLike,
) -> dict[str, FloatLike]:
    """Return decay probabilities for several toy 1D regions."""

    return {region.name: probability_in_region(region, L_lab) for region in regions}
