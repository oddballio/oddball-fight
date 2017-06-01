# pylint: disable=invalid-name, line-too-long
"""This script is the flow control script for OddballFight, alerts user what action to take after an action has been completed"""
import re
import Game

start_game = Game.Game

start_confirm = raw_input(
    "Welcome to Oddball Fight! Do you wish to start?: ")
p = re.compile('^Y|y|O|o')
match = p.match(start_confirm)
while match:
    start_game.start_game()
