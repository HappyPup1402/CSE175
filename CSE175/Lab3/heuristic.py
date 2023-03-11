#
# heuristic.py
#
# This Python script file provides two functions in support of minimax search
# using the expected value of game states. First, the file provides the
# function "expected_value_over_delays". This function takes as an argument
# a state of game play in which the current player has just selected an
# action. The function calculates the expected value of the state over all
# possible random results determining the amount of time before the
# Guardian changes gaze direction. This function calculates this value
# regardless of whose turn it is. The value of game states that result from
# different random outcomes is determined by calling "value". Second, the
# file provides a heuristic evaluation function for non-terminal game states.
# The heuristic value returned is between "max_payoff" (best for the
# computer player) and negative one times that value (best for the opponent).
# The heuristic function may be applied to any state of play. It uses
# features of the game state to predict the game payoff without performing
# any look-ahead search.
#
# This content is protected and may not be shared, uploaded, or distributed.
#
# PLACE ANY COMMENTS, INCLUDING ACKNOWLEDGMENTS, HERE
#
# PLACE YOUR NAME AND THE DATE HERE
#


from parameters import *
from minimax import probability_of_time
from minimax import value


def expected_value_over_delays(state, ply):
    """Calculate the expected utility over all possible randomly selected
    Guardian delay times. Return this expected utility value."""
    val = 0.0
    #PLACE YOUR CODE HERE
    for delay in range(min_time_steps, max_time_steps):
        state.time_remaining = delay
        val = val + (probability_of_time(delay) * value(state, ply))
    return val


def heuristic_value(state):
    """Return an estimate of the expected payoff for the given state of
    game play without performing any look-ahead search. This value must
    be between the maximum payoff value and the additive inverse of the
    maximum payoff."""

    val = 0.0
    #PLACE YOUR CODE HERE
    computer_value = abs(board_size) - abs(state.w_loc)
    player_value = abs(board_size) - abs(state.e_loc)
    if player_value == computer_value:
        if state.current_turn is Player.west:
            val = -25
        else:
            val = 25
    elif player_value > computer_value:
        if state.current_turn is Player.west:
            val = -100
        else:
            val = -50
    elif computer_value > player_value:
        if state.current_turn is Player.east:
            val = 100
        else:
            val = 50

    return val