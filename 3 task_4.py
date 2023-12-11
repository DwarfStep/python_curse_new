class Apple:
    grow = ['цветение', 'зеленое', 'красное']

    def __init__(self, index, stage_grow=grow[0]):
        self.index = index
        self.stage_grow = stage_grow

    def return_stage(self):
        return self.stage_grow


class Tree:

    def __init__(self, index, *args):
        self.index = index
        self.apples = [int(i) for i in args]


class Gardener:

    def __init__(self, name, *args):
        self.name = name
        self.trees = [int(i) for i in args]


print(Apple(1).return_stage())