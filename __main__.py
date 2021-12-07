from templates.Character import Character
from utils.CharClass import CharClass

class __main__:
    newChar = Character(CharClass.bard, "dwerf", 3, "")
    # print(newChar.charClass)
    # print(newChar.hitDie)
    # print(newChar.health)
    # print(newChar.abilities.strength)
    newChar.characterInfo()
