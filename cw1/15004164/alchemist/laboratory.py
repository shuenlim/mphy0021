import random


class Laboratory(object):
    def __init__(self, yaml_shelves):
        self.shelf1 = yaml_shelves.get('lower')
        self.shelf2 = yaml_shelves.get('upper')
        self.number = len(yaml_shelves.keys())
        if self.number > 2:
            raise TypeError("Too many shelves!")

    def can_react(self, substance1, substance2):
        if "antianti" in substance1 or "antianti" in substance2:
            raise TypeError("antianti products not permitted!")
        cond1 = substance1 == "anti" + substance2
        cond2 = substance2 == "anti" + substance1
        return cond1 or cond2

    def update_shelves(self, shelf1, shelf2, substance1, substance2_index):
        index1 = shelf1.index(substance1)
        shelf1 = shelf1[:index1] + shelf1[index1+1:]
        shelf2 = shelf2[:substance2_index] + shelf2[substance2_index+1:]
        return shelf1, shelf2

    def do_a_reaction(self):
        for substance1 in self.shelf1:
            possible_targets = [i for i, target in enumerate(self.shelf2) if
                                self.can_react(substance1, target)]
            if not possible_targets:
                continue
            else:
                substance2_index = random.choice(possible_targets)
                return self.update_shelves(self.shelf1, self.shelf2,
                                           substance1, substance2_index)
        return self.shelf1, self.shelf2

    def run_full_experiment(self):
        count = 0
        ended = False
        while not ended:
            shelf1_new, shelf2_new = self.do_a_reaction()
            if shelf1_new != self.shelf1:
                count += 1
            ended = (shelf1_new == self.shelf1) and (shelf2_new == self.shelf2)
            self.shelf1, self.shelf2 = shelf1_new, shelf2_new
        return self.shelf1, self.shelf2, count
