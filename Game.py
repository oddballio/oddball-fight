# pylint: disable=invalid-name, line-too-long
import re
from lib.Character import *
from lib.Fight import *


class Game:
    def __init__(self):
        self.all_char = [Rob("rob", 15, 15, "Nerd"), Travis(
            "travis", 20, 10, "Business Man"), XiaoLu("xiaolu", 200, 300, "GM")]
        self.current_user = ""
        self.current_user_s = ""
        self.current_opponent_s = ""
        self.current_opponent = ""
        self.possible_opponent = ['xiaolu', 'travis', 'rob']

    def choose_opponent(self, player):
        choose = raw_input(
            "who do you wish to fight? {}: ".format(self.possible_opponent))

        self.current_opponent = choose
        self.confirm_opponent(player)

    def confirm_opponent(self, player):
        s = raw_input(
            "are you sure you want to fight {}? y/n :".format(self.current_opponent))
        p = re.compile('^Y|y|O|o')
        match = p.match(s)
        if match:
            self.set_user_stat(self.current_opponent, player)
            print "you will fight {}".format(self.current_opponent)
        else:
            self.choose_opponent(player)

    def start_fight(self):
        fight = Fight(user=self.current_user_s,
                      opponent=self.current_opponent_s, user_mp=self.current_user_s.mp, opp_mp=self.current_opponent_s.mp)
        fight.start_fight()

    def set_user_stat(self, name, player):
        for item in self.all_char:
            if item.name == name:
                if player == "user":
                    self.current_user_s = item
                else:
                    self.current_opponent_s = item

    def start_game(self, player):
        s = raw_input("Who are you? : ")
        if len(s) and s == "travis":
            travis = Travis("travis", 20, 10, "Business Man")
            travis.show_stats()
            travis.show_skills()
            travis.show_inventory()
            self.current_user = "travis"
            self.set_user_stat(self.current_user, player)
            print "you are now travis"

        elif len(s) and s == "rob":
            rob = Rob("rob", 15, 15, "Nerd")
            rob.show_stats()
            rob.show_skills()
            rob.show_inventory()
            self.current_user = "rob"
            self.set_user_stat(self.current_user, player)
            print "you are now rob"

        elif len(s) and s == "xiaolu":
            xiaolu = XiaoLu("xiaolu", 200, 300, "GM")
            xiaolu.show_stats()
            xiaolu.show_skills()
            xiaolu.show_inventory()
            self.current_user = "xiaolu"
            self.set_user_stat(self.current_user, player)
            print "you are now {}".format(s)
        else:
            print "you are not one of oddball yet!"
