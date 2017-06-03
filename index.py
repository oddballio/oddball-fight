# pylint: disable=invalid-name, line-too-long
"""This script is the flow control script for OddballFight, alerts user what action to take after an action has been completed"""
import re
from Game import Game
new_game = Game()
start_confirm = raw_input(
    "Welcome to Oddball Fight! Do you wish to start? y/n : ")
p = re.compile('^Y|y|O|o')
match = p.match(start_confirm)
while match:
    new_game.start_game("user")
    new_game.choose_opponent("opponent")
    new_game.start_fight()
else:
    print 'game ended'
