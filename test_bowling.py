from bowling import BowlingGame

def test_gutter_game():
    """A game where no pins are knocked down should score 0."""
    game = BowlingGame("00 00 00 00 00 00 00 00 00 00")
    assert game.score() == 0

def test_scoring_in_a_single_open_frame():
    """A game with one frame of 1 and 2, and the rest zeros, should score 3."""
    game = BowlingGame("12 00 00 00 00 00 00 00 00 00")
    assert game.score() == 3
