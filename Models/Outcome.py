class Outcome:
    def __init__(self, outcome_type, consequences):
        self.outcome_type = outcome_type
        self.consequences = consequences
        self.value = sum(conseq.relative_value * count for conseq, count in consequences.items())

    def __str__(self):
        return "/".join(f"{count}{conseq.printable_symbol}" for conseq, count in self.consequences.items())
    