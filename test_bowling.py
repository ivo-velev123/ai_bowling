from bowling import BowlingGame

def test_gutter_game():
    """A game where no pins are knocked down should score 0."""
    game = BowlingGame("00 00 00 00 00 00 00 00 00 00")
    assert game.score() == 0
