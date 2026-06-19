import pytest
from logic_utils import check_guess


def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

# pytest written by claude to check that the high/low logic is correct and not swapped. This is important to ensure that the game provides accurate feedback to the player, which is crucial for the gameplay experience.

# Parametrized cases to verify high/low direction is not swapped
@pytest.mark.parametrize("guess, secret, expected_outcome", [
    (75, 50, "Too High"),   # guess above secret → Too High
    (25, 50, "Too Low"),    # guess below secret → Too Low
    (1,  100, "Too Low"),   # extreme low end
    (100, 1,  "Too High"),  # extreme high end
    (51, 50,  "Too High"),  # one above secret
    (49, 50,  "Too Low"),   # one below secret
    (50, 50,  "Win"),       # exact match
])
def test_high_low_direction(guess, secret, expected_outcome):
    outcome, _ = check_guess(guess, secret)
    assert outcome == expected_outcome, (
        f"check_guess({guess}, {secret}) returned '{outcome}', expected '{expected_outcome}'"
    )
