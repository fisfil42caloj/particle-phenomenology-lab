import numpy as np
import pytest

from llp_acceptance.kinematics import (
    beta_from_energy,
    betagamma_from_energy,
    betagamma_from_momentum,
    gamma_from_energy,
    lab_decay_length,
    momentum_from_energy,
)


def test_particle_at_rest_has_expected_kinematics() -> None:
    E = 5.0
    m = 5.0

    assert momentum_from_energy(E, m) == pytest.approx(0.0)
    assert beta_from_energy(E, m) == pytest.approx(0.0)
    assert gamma_from_energy(E, m) == pytest.approx(1.0)
    assert betagamma_from_energy(E, m) == pytest.approx(0.0)


def test_ultrarelativistic_beta_approaches_one() -> None:
    beta = beta_from_energy(E=1_000.0, m=1.0)

    assert beta == pytest.approx(1.0, abs=1e-6)


def test_betagamma_from_energy_matches_momentum_over_mass() -> None:
    E = 20.0
    m = 2.0
    p = momentum_from_energy(E, m)

    assert betagamma_from_energy(E, m) == pytest.approx(p / m)
    assert betagamma_from_momentum(p, m) == pytest.approx(p / m)


def test_energy_below_mass_raises_clear_physical_error() -> None:
    with pytest.raises(ValueError, match="energy below its rest mass"):
        momentum_from_energy(E=0.9, m=1.0)


def test_lab_decay_length_uses_ctau_in_meters() -> None:
    assert lab_decay_length(ctau=2.0, betagamma=3.0) == pytest.approx(6.0)


def test_array_inputs_are_supported() -> None:
    energies = np.array([1.0, 2.0, 10.0])
    masses = 1.0
    betagamma = betagamma_from_energy(energies, masses)

    assert isinstance(betagamma, np.ndarray)
    assert betagamma[0] == pytest.approx(0.0)
