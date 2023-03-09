# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random


def player(prev_play, opponent_history=[]):
  if prev_play == "":
    # Start a random move
    return random.choice(["R", "P", "S"])
  else:
    # Add the opponent last move to history
    opponent_history.append(prev_play)

    # Count the number of times the opponent has played each move
    rock_count = opponent_history.count("R")
    paper_count = opponent_history.count("P")
    scissors_count = opponent_history.count("S")

    # Choose our next move based on the opponent move history
    most_common = max(rock_count, paper_count, scissors_count)
    if most_common == rock_count:
      move = "P"
    elif most_common == paper_count:
      move = "S"
    elif most_common == scissors_count:
      move = "R"

    # Add some randomness to our decision
    if random.random() < 0.2:
      move = random.choice(["R", "P", "S"])

    return move