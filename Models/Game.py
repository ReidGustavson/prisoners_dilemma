from Factories import StageGenerator

class Game:
    def __init__(self):
        self.crimes = StageGenerator.new_stage(0).crimes + \
            StageGenerator.new_stage(1).crimes + \
            StageGenerator.new_stage(2).crimes