import itertools

from Factories import CrimeGenerator
from Models import RoleType
from Models.Stage import Stage


class StageGenerator:
    @classmethod
    def new_stage(cls, lvl):
        crimes = []
        if (lvl == 0):
            for _ in range(10):
                crimes.append(CrimeGenerator.new_crime(0, [RoleType.LONEWOLF]))
        elif (lvl < 3):
            numbers = [1, 2, 3, 4, 5]
            combinations = list(itertools.combinations(numbers, 3))
            for c in combinations:
                if lvl == 2:
                    c = tuple(x + 5 for x in c) 

                roles = [role for role in RoleType if role.value in c]
                crimes.append(CrimeGenerator.new_crime(lvl, roles))
        return Stage(lvl, crimes)
