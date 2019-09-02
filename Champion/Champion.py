class Champions:
    "a Champion has name, a list of attributes and score that is initiially 0"
    def __init__(self, name, attribute):
        self.name = name
        self.attribute = []
        if type(attribute) == list:
            for x in attribute:
                self.attribute.append(x)
        if type(attribute) == str:
            self.attribute.append(attribute)
        self.attribute.sort()
        self.score = 0

    def get_score(self):
        return self.score

    def add_score(self, score):
        self.score = score

    def display_attributes(self):
        print("{} has type of".format(self.name))
        for x in self.attribute:
            if x is not None:
                print(x)

    def __repr__(self):
        return self.name

