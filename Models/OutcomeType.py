from enum import Enum

class OutcomeType(Enum):
    Success = 1
    Escape = 0
    Caught = -1
