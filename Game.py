# pylint: disable=invalid-name, line-too-long
from lib.Character import *


class Game:
    @classmethod
    def start_game(self):
        s = raw_input("Who are you? : ")
        if len(s) and s == "travis":
            travis = Travis("travis", 20, 10, "Business Man")
            travis.show_stats()
            print "your skills are : {}".format(travis.skill_n)
            print "your inventory : {}".format(travis.inventory)
        elif len(s) and s == "rob":
            rob = Rob("rob", 15, 15, "Nerd")
            rob.show_stats()
            print "your skills are : {}".format(rob.skill_n)
            print "your inventory : {}".format(rob.inventory)
        elif len(s) and s == "xiaolu":
            xiaolu = XiaoLu("xiaolu", 200, 300, "GM")
            xiaolu.show_stats()
            print "your skills are : {}".format(xiaolu.skill_n)
            print "your inventory : {}".format(xiaolu.inventory)
