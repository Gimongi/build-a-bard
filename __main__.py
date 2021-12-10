import sys
from templates.Character import Character
from utils.CharRace import CharRace
from utils.CharClass import CharClass

class __main__:
    print("Argument List:" + str(sys.argv[1]))
    race = CharRace.fromStr(sys.argv[1])
    char = CharClass.fromStr(sys.argv[2])
    level = sys.argv[3]
    newChar = Character(char, race, level, "")
    # newChar.characterInfo()
