class Utils:

    @staticmethod
    def getModifier(abilityScore):
        if abilityScore == 1:
            return -5
        elif abilityScore <= 3:
            return -4
        elif abilityScore <= 5:
            return -3
        elif abilityScore <= 7:
            return -2
        elif abilityScore <= 9:
            return -1
        elif abilityScore <= 11:
            return 0
        elif abilityScore <= 13:
            return 1
        elif abilityScore <= 15:
            return 2
        elif abilityScore <= 17:
            return 3
        elif abilityScore <= 19:
            return 4
        elif abilityScore <= 21:
            return 5
        elif abilityScore <= 23:
            return 6
        elif abilityScore <= 25:
            return 7
        elif abilityScore <= 27:
            return 8
        elif abilityScore <= 29:
            return 9
        elif abilityScore == 30:
            return 10
        else:
            # throw error
            return 0


#TODO getRandomRace
#TODO getRandomClass