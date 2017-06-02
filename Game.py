# pylint: disable=invalid-name, line-too-long
import re
from lib.Character import *


class Game:
    def __init__(self):
        self.all_char = [Rob("rob", 15, 15, "Nerd"), Travis(
            "travis", 20, 10, "Business Man"), XiaoLu("xiaolu", 200, 300, "GM")]
        self.current_user = ""
        self.current_opponent = ""
        self.possible_opponent = ['xiaolu', 'travis', 'rob']

    @classmethod
    def choose_opponent(self, possible_opponent, all_char):
        flag = True
        choose = raw_input(
            "who do you wish to fight? {}: ".format(possible_opponent))

        self.current_opponent = choose
        self.confirm_opponent(all_char, possible_opponent)

    @classmethod
    def confirm_opponent(self, all_char, possible_opponent):
        s = raw_input(
            "are you sure you want to fight {}? y/n :".format(self.current_opponent))
        p = re.compile('^Y|y|O|o')
        match = p.match(s)
        if match:
            for item in all_char:
                if item.name == self.current_opponent:
                    item.show_stats()
        else:
            self.choose_opponent(possible_opponent, all_char)

    @classmethod
    def start_game(self):
        s = raw_input("Who are you? : ")
        if len(s) and s == "travis":
            travis = Travis("travis", 20, 10, "Business Man")
            travis.show_stats()
            print "your skills are : {}".format(travis.skill_n)
            print "your inventory : {}".format(travis.inventory)
            print "you are now travis"
            self.current_user = "travis"
        elif len(s) and s == "rob":
            rob = Rob("rob", 15, 15, "Nerd")
            rob.show_stats()
            print "your skills are : {}".format(rob.skill_n)
            print "your inventory : {}".format(rob.inventory)
            print "you are now rob"
            self.current_user = "rob"
        elif len(s) and s == "xiaolu":
            xiaolu = XiaoLu("xiaolu", 200, 300, "GM")
            xiaolu.show_stats()
            print "your skills are : {}".format(xiaolu.skill_n)
            print "your inventory : {}".format(xiaolu.inventory)
            self.current_user = "xiaolu"
        else:
            print "you are not one of oddball yet!"
