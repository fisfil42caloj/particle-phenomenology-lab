from llp_acceptance.decay import decay_probability_between
from llp_acceptance.kinematics import lab_decay_length


def main() -> None:
    ctau = 1.0
    betagamma = 10.0
    L_lab = lab_decay_length(ctau, betagamma)

    probability = decay_probability_between(1.0, 4.0, L_lab)
    print(f"L_lab = {L_lab:.3g} m")
    print(f"P(1 m < L < 4 m) = {probability:.6f}")


if __name__ == "__main__":
    main()
