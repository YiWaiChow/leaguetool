class User:
    def __init__(self, name):
        self.pool = []
        self.preference = []
        self.name = name

    def get_pool(self):
        return self.pool

    def add_prefer(self, prefer):
        if type(prefer) == list:
            for x in prefer:
                self.preference.append(x)
        if type(prefer) == str:
            self.preference.append(prefer)
        self.preference.sort()

    def add_champ_to_pool(self, champ):
        self.pool.append(champ)

