from Models import OutcomeType

class Role:
    def __init__(self, role_type, cost, outcomes, ev):
        self.role_type = role_type
        self.cost = cost
        self.outcomes = outcomes
        self.ev = ev

    @property
    def name(self):
        return self.role_type.name.lower().capitalize()
    
    def __describe__(self):
        success_outcome = self.outcomes[2]
        escape_outcome = self.outcomes[1]
        caught_outcome = self.outcomes[0]
        
        return {
            "cost": self.cost, 
            "caught": caught_outcome, 
            "succeed": success_outcome, 
            "escape": escape_outcome, 
            "expected_value": self.ev
        }
