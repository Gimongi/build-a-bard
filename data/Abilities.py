import enum

class Abilities(str, enum.Enum):
    strength = "str"
    dexterity = "dex"
    constitution = "con"
    intelligence = "int"
    wisdom = "wis"
    charisma = "cha"

    @staticmethod
    def fromStr(ability):
        if ability == "str":
            return Abilities.strength
        elif ability == "dex":
            return Abilities.dexterity
        elif ability == "con":
            return Abilities.constitution
        elif ability == "int":
            return Abilities.intelligence
        elif ability == "wis":
            return Abilities.wisdom
        elif ability == "cha":
            return Abilities.charisma
        else:
            return NotImplementedError
