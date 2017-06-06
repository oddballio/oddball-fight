# pylint: disable=invalid-name, line-too-long

import pprint
import random


class Fight:
    def __init__(self, user, opponent, user_mp, opp_mp):
        self.opponent_moved = False
        self.user_moved = False
        self.user = user
        self.opponent = opponent
        self.round_number = 0
        self.user_mp = user_mp
        self.opp_mp = opp_mp
        self.user_current_skill = ""
        self.opp_current_skill = ""
        self.end_fight = False

    def start_fight(self):
        while not self.end_fight:
            self.attack()

    def attack(self):
        while self.user.hp > 0 and self.opponent.hp > 0:
            s = raw_input(
                "which skill do you want to use? {} : ".format(self.user.skill_n))
            if int(s) <= len(self.user.skills):
                self.start_turn()
                self.regen_mp()
                self.user_attack(s)
                self.opponent_attack()
                self.show_hp_mp(self.user_current_skill,
                                self.opp_current_skill)

            else:
                print "that skill is not available, choose again"

        self.handle_end_fight()
        self.end_fight = True
        print "HoLALALALALALALA {}".format(self.end_fight)

    def start_turn(self):
        print "Round {}".format(self.round_number + 1)
        self.round_number += 1

    def regen_mp(self):
        print self.user_mp, self.opp_mp
        if self.user.mp != self.user_mp:
            self.user.mp += 1
            print "You gained 1 mp."
        if self.opponent.mp != self.opp_mp:
            self.opponent.mp += 1
            print "{} gained 1 mp.".format(self.opponent.name)

    def user_attack(self, s):
        user_skill = self.user.skills[int(s) - 1].values()
        if user_skill[1] <= self.user.mp:
            print "you used {}".format(user_skill[0])
            print "your {} caused {} dmg to {}!".format(user_skill[0], user_skill[2], self.opponent.name)
            self.opponent.hp -= user_skill[2]
            self.user.mp -= user_skill[1]
            self.user_current_skill = user_skill
        else:
            print "you dont have enough MP to activate that skill!"

    def opponent_attack(self):
        random_attack = random.choice(self.opponent.skills).values()
        if random_attack[1] <= self.opponent.mp:
            print "{} used {}".format(self.opponent.name, random_attack[0])
            print "{}'s {} caused {} dmg to you!".format(self.opponent.name, random_attack[0], random_attack[2])
            self.user.hp -= random_attack[2]
            self.opponent.mp -= random_attack[1]
            self.opp_current_skill = random_attack
        else:
            return

    def show_hp_mp(self, user_skill_used, opp_skill_used):
        print "your hp: {} -> {}".format(self.user.hp + opp_skill_used[2], self.user.hp)
        print "your mp: {} -> {}".format(self.user.mp + user_skill_used[1], self.user.mp)
        print "{}'s hp: {} -> {}".format(self.opponent.name, self.opponent.hp + user_skill_used[2], self.opponent.hp)
        print "{}'s mp: {} -> {}".format(self.opponent.name, self.opponent.mp + opp_skill_used[1], self.opponent.mp)

    def handle_end_fight(self):
        if self.user.hp <= 0:
            print "You died! You've gained {} exp!".format(self.user.exp + 2)
            self.user.exp += 2
        elif self.opponent.hp <= 0:
            print "You won! You've gained {} exp!".format(self.user.exp + 5)
            self.user.exp += 5
            print self.user.exp
        if self.user.exp >= self.user.exp_cap:
            self.user.level += 1
