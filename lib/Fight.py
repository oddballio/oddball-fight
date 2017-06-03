import pprint


class Fight:
    def __init__(self, user, opponent):
        self.opponent_moved = False
        self.user_moved = False
        self.user = user
        self.opponent = opponent
        self.round_number = 0

    def start_fight(self):
        self.attack()

    def attack(self):
        while self.user.hp > 0 and self.opponent.hp > 0:
            s = raw_input(
                "which skill do you want to use? {} : ".format(self.user.skill_n))
            if int(s) <= len(self.user.skills):
                print "Round {}".format(self.round_number + 1)
                self.round_number += 1

                user_skill = self.user.skills[int(s) - 1]
                if user_skill.values()[1] <= self.user.mp:
                    print "you used {}".format(user_skill.values()[0])
                    print "your {} caused {} dmg to {}!".format(user_skill.values()[0], user_skill.values()[2], self.opponent.name)
                    self.opponent.hp -= user_skill.values()[2]
                    self.user.mp -= user_skill.values()[1]
                    print"{}'s hp : {} -> {}".format(self.opponent.name,
                                                     self.opponent.hp + user_skill.values()[2], self.opponent.hp)
                    print"your mp : {} -> {}".format(self.user.mp + user_skill.values()[1], self.user.mp)
                else:
                    print "you dont have enough MP to activate that skill!"
            else:
                print "that skill is not available, choose again"

        if self.user.hp <= 0:
            print "you died"

        elif self.opponent.hp <= 0:
            print "you won!"
