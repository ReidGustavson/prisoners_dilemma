import random
from .OutcomeGenerator import OutcomeGenerator
from Models import OutcomeType, Role

class RoleGenerator:
    @classmethod
    def new_role(cls, lvl, role_type, target_expected_value):
        cost = random.choice([10,20])
        
        caught_expected = random.randint(-4, -1) * 10
        escape_expected = random.randint(-4,2) * 10
        alibi_cost = 20
        success_expected = 4 * (target_expected_value - (.25 * caught_expected + .5 * escape_expected - cost - alibi_cost))
        success_expected = round(success_expected / 10) * 10

        caught_outcome = OutcomeGenerator.new_outcome(lvl, OutcomeType.Caught, caught_expected)
        escape_outcome = OutcomeGenerator.new_outcome(lvl, OutcomeType.Escape, escape_expected)
        success_outcome = OutcomeGenerator.new_outcome(lvl, OutcomeType.Success, success_expected)
        ev = .25*caught_outcome.value + .5*escape_outcome.value + .25*success_outcome.value - cost - alibi_cost 
        return Role(role_type, cost, [caught_outcome, escape_outcome, success_outcome], ev)    
