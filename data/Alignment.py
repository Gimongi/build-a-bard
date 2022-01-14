import enum

class Alignment(str, enum.Enum):
    lawful_good = "lawful good"
    neutral_good = "neutral good"
    chaotic_good = "chaotic good"
    lawful_neutral = "lawful neutral"
    neutral = "neutral"
    chaotic_neutral = "chaotic neutral"
    lawful_evil = "lawful evil"
    neutral_evil = "neutral evil"
    chaotic_evil = "chaotic evil"

    @staticmethod
    def fromStr(alignment):
        if alignment == "lawful good":
            return Alignment.lawful_good
        elif alignment == "neutral good":
            return Alignment.neutral_good
        elif alignment == "chaotic good":
            return Alignment.chaotic_good
        elif alignment == "lawful neutral":
            return Alignment.lawful_neutral
        elif alignment == "neutral":
            return Alignment.neutral
        elif alignment == "chaotic neutral":
            return Alignment.chaotic_neutral
        elif alignment == "lawful evil":
            return Alignment.lawful_evil
        elif alignment == "neutral evil":
            return Alignment.neutral_evil
        elif alignment == "chaotic evil":
            return Alignment.chaotic_evil
        else:
            return NotImplementedError

        