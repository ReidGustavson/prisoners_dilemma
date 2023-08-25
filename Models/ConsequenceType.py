from enum import Enum

class ConsequenceType(Enum):
    @property
    def printable_symbol(self):
        if self == ConsequenceType.MONEY:
            return "$"
        return self.name[0]
    
    @property
    def relative_value(self):
        if self == ConsequenceType.MONEY:
            return 1
        if self == ConsequenceType.GRIT or self == ConsequenceType.KNOWLEDGE:
            return 80
        if self == ConsequenceType.HEAT:
            return -40
        if self == ConsequenceType.MISDEMEANOR:
            return -100
        if self == ConsequenceType.FELONY:
            return -1000

    MONEY = 1
    GRIT = 2
    KNOWLEDGE = 3
    HEAT = 4
    FELONY = 5
    MISDEMEANOR = 6

