import random
from Models import OutcomeType, ConsequenceType, Outcome

class OutcomeGenerator:
    @classmethod
    def new_outcome(cls, lvl, outcome_type, expected_value):
        allowed_consequences = cls.get_allowed_consequences(lvl, outcome_type)
        consequences = cls.generate_consequences(allowed_consequences, expected_value)
        return Outcome(outcome_type, consequences)
    
    @classmethod
    def generate_consequences(cls, allowed_consequences, expected_value):
        consequences = dict()
        current_value = 0
        consequence_count = 0
        while (current_value - expected_value != 0):
            if consequence_count == 2:
                consequences[ConsequenceType.MONEY] = consequences.get(ConsequenceType.MONEY, 0) + expected_value - current_value 
                break
            consequence = cls.generate_consequence(allowed_consequences)
            consequences[consequence['type']] = consequences.get(consequence['type'], 0) + consequence['amount']
            current_value += consequence['type'].relative_value * consequence['amount']
            consequence_count += 1
        return consequences

    @classmethod
    def generate_consequence(cls, allowed_consequences):
        all_options = [(key, item) for key, sublist in allowed_consequences.items() for item in sublist]
    
        selected_key, selected_item = random.choice(all_options)
        
        sign = 1
        if (selected_key == "either"):
            sign = random.choice([-1,1])
        if (selected_key == "lose"):
            sign = -1

        amount = 1
        if selected_item == ConsequenceType.MONEY:
            amount = random.randint(1,6) * 10
        return {"type": selected_item, "amount": sign * amount}
        
    @classmethod
    def get_allowed_consequences(cls, lvl, outcome_type):
        if (lvl == 0):
            if (outcome_type == OutcomeType.Success):
                return { "gain": [ConsequenceType.MONEY, ConsequenceType.GRIT, ConsequenceType.KNOWLEDGE]}
            if (outcome_type == OutcomeType.Escape):
                return {
                    "either": [ConsequenceType.MONEY, ConsequenceType.GRIT, ConsequenceType.KNOWLEDGE],
                    "gain": [ConsequenceType.HEAT]
                }
            # Caught
            return {"lose": [ConsequenceType.MONEY]}
        if (lvl == 1):
            if (outcome_type == OutcomeType.Success):
                return { "gain": [ConsequenceType.MONEY, ConsequenceType.GRIT, ConsequenceType.KNOWLEDGE]}
            if (outcome_type == OutcomeType.Escape):
                return {
                    "either": [ConsequenceType.MONEY, ConsequenceType.GRIT, ConsequenceType.KNOWLEDGE],
                    "gain": [ConsequenceType.HEAT]
                }
            # Caught
            return {
                "lose": [ConsequenceType.MONEY],
                "either": [ConsequenceType.GRIT, ConsequenceType.KNOWLEDGE],
                "gain": [ConsequenceType.MISDEMEANOR]
            }
        # Else lvl 2
        if (outcome_type == OutcomeType.Success):
            return { "gain": [ConsequenceType.MONEY, ConsequenceType.GRIT, ConsequenceType.KNOWLEDGE, ConsequenceType.HEAT]}
        if (outcome_type == OutcomeType.Escape):
            return {
                "either": [ConsequenceType.MONEY, ConsequenceType.GRIT, ConsequenceType.KNOWLEDGE],
                "gain": [ConsequenceType.HEAT, ConsequenceType.MISDEMEANOR]
            }
        # Caught
        return {
            "gain": [ ConsequenceType.FELONY, ConsequenceType.MISDEMEANOR], 
                "either": [ConsequenceType.GRIT, ConsequenceType.KNOWLEDGE],
            "lose": [ConsequenceType.MONEY]
        }