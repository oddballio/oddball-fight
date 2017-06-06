# pylint: disable=invalid-name, line-too-long, too-many-instance-attributes, too-few-public-methods
"""This class is the base character class of every created charactor"""


class Character:
    """basic prototype of a character"""

    def __init__(self, name, hp, mp, charclass):
        """Initializes the data."""

        self.name = name
        self.hp = hp
        self.mp = mp
        self.level = 0
        self.char_class = charclass
        self.inventory = []
        self.exp = 0
        self.exp_cap = 20 + self.level * 5

    def show_stats(self):
        """prints character stats to the ternimal"""

        print "name: {}".format(self.name)
        print "level: {}".format(self.level)
        print "hp: {}".format(self.hp)
        print "mp: {}".format(self.mp)
        print "class: {}".format(self.char_class)

    def show_skill_names(self, skills):
        """prints skill names in an array"""
        result = []
        for item in skills:
            result.append(item.items()[0][1])
        return result


class Travis(Character):
    """Initializes Travis."""

    def __init__(self, name, hp, mp, charclass):
        Character.__init__(self, name, hp, mp, charclass)
        self.char_class = charclass
        self.weapon = "stick"
        self.skills = [{"name": "Attack", "dmg": self.level + 1, "mpc": 0}, {
            "name": "Poke", "dmg": self.level + 2, "mpc": 2}, {"name": "OpenRA", "dmg": self.level + 4, "mpc": 4}]
        self.skill_n = self.show_skill_names(self.skills)

    def show_skills(self):
        print "skills : {}" .format(self.skill_n)

    def show_inventory(self):
        print "inventory : {}".format(self.inventory)


class Rob(Character):
    """Initializes Rob"""

    def __init__(self, name, hp, mp, charclass):
        Character.__init__(self, name, hp, mp, charclass)
        self.char_class = charclass
        self.weapon = "nerdy wand"
        self.skills = [{"name": "Attack", "dmg": self.level + 1, "mpc": 0}, {
            "name": "Nerdy Glare", "dmg": self.level + 3, "mpc": 2}, {"name": "Nerd Hand Gastures", "dmg": self.level + 5, "mpc": 4}]
        self.skill_n = self.show_skill_names(self.skills)

    def show_skills(self):
        print "skills : {}" .format(self.skill_n)

    def show_inventory(self):
        print "inventory : {}".format(self.inventory)


class XiaoLu(Character):
    """Initializes XiaoLu"""

    def __init__(self, name, hp, mp, charclass):
        Character.__init__(self, name, hp, mp, charclass)
        self.char_class = charclass
        self.weapon = "redbull can"
        self.skills = [{"name": "Attack", "dmg": 1000, "mpc": 1}]
        self.skill_n = self.show_skill_names(self.skills)

    def show_skills(self):
        print "skills : {}" .format(self.skill_n)

    def show_inventory(self):
        print "inventory : {}".format(self.inventory)
