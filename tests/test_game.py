import pytest

from src.main import RockPaperScissors


# Tests for decide_winner()
@pytest.mark.parametrize(
    "user_choice, computer_choice, expected",
    [
        ("rock", "scissors", "Congratulations! You won!"),
        ("rock", "paper", "Oops! The computer won!"),
        ("rock", "rock", "It's a draw!"),
        ("paper", "rock", "Congratulations! You won!"),
        ("paper", "paper", "It's a draw!"),
        ("paper", "scissors", "Oops! The computer won!"),
        ("scissors", "paper", "Congratulations! You won!"),
        ("scissors", "rock", "Oops! The computer won!"),
        ("scissors", "scissors", "It's a draw!"),
    ],
)
def test_decide_winner(user_choice, computer_choice, expected):
    game = RockPaperScissors()

    result = game.decide_winner(user_choice, computer_choice)

    assert result == expected


# Tests for player_choice()
def test_player_choice_valid_input(monkeypatch):
    game = RockPaperScissors()

    monkeypatch.setattr("builtins.input", lambda _: "rock")

    result = game.player_choice()

    assert result == "rock"


def test_player_choice_invalid_then_valid(monkeypatch, capsys):
    game = RockPaperScissors()

    inputs = iter(["baba", "rock"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = game.player_choice()
    captured = capsys.readouterr()

    assert result == "rock"
    assert "Invalid choice. Please try again." in captured.out


# Test for computer_choice()
def test_computer_choice(monkeypatch):
    game = RockPaperScissors()

    def fake_choice(items):
        return "scissors"

    monkeypatch.setattr("src.main.random.choice", fake_choice)

    result = game.computer_choice()

    assert result == "scissors"


# Test for play()
def test_play(monkeypatch, capsys):
    game = RockPaperScissors()

    monkeypatch.setattr(game, "player_choice", lambda: "rock")
    monkeypatch.setattr(game, "computer_choice", lambda: "scissors")

    game.play()
    captured = capsys.readouterr()

    assert "Your choice: rock" in captured.out
    assert "Computer choice: scissors" in captured.out
    assert "Congratulations! You won!" in captured.out
