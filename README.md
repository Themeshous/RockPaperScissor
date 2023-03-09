# RockPaperScissor

This repository contains a file called RPS.py which includes a function named player. The function requires a string input describing the previous move made by the opponent, which can be "R", "P", or "S". The function must then output a string representing the next move for the player, which can also be "R", "P", or "S".

For the first game in a match, the player function will receive an empty string as input since there is no previous play.

The example function provided in RPS.py has two arguments, player(prev_play, opponent_history = []). However, the second argument (opponent_history = []) is optional and the function is never called with this argument. The reason why it is included is that it enables the saving of state between consecutive calls of the player function. The opponent_history argument is only required if you want to track the opponent's move history.
