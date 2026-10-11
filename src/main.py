import random


class RockPaperScissors:
    """Main class for the Rock Paper Scissors game."""

    def __init__(self):
        self.items = ["rock", "paper", "scissors"]

    def player_choice(self) -> str:
        """Get and validate the player's choice."""

        while True:
            user_choice = input(
                f"Please enter your choice from {self.items}: "
            ).strip().lower()

            if user_choice in self.items:
                return user_choice

            print("Invalid choice. Please try again.")

    def computer_choice(self) -> str:
        """Return a random choice from the available items."""

        return random.choice(self.items)

    def decide_winner(
        self, user_input: str, computer_choice_item: str
    ) -> str:
        """Determine the winner of the round."""

        if user_input == computer_choice_item:
            return "It's a draw!"

        win_combinations = [
            ("paper", "rock"),
            ("rock", "scissors"),
            ("scissors", "paper"),
        ]

        for player_choice, computer_choice in win_combinations:
            if (
                user_input == player_choice
                and computer_choice_item == computer_choice
            ):
                return "Congratulations! You won!"

        return "Oops! The computer won!"

    def play(self) -> None:
        """Play one round of the game."""

        user_input = self.player_choice()
        computer_choice_item = self.computer_choice()

        print(
            f"Your choice: {user_input}, "
            f"Computer choice: {computer_choice_item}"
        )
        print("\n-- Match result --")
        print(self.decide_winner(user_input, computer_choice_item))
        print()


def main() -> None:
    """Run the game and allow the player to play multiple rounds."""

    game = RockPaperScissors()

    while True:
        game.play()

        play_again = input(
            "Press Q to quit, or any other key to play again: "
        ).strip().lower()

        if play_again == "q":
            print("Thank you for playing! Goodbye!")
            break

        print("-- Next game --")


if __name__ == "__main__":
    main()
