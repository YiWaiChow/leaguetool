class User:
    def __init__(self):
        self.pool = []
        self.preference = []

    def get_pool(self):
        return self.pool

    def add_prefer(self, prefer):
        if type(prefer) == list:
            for x in prefer:
                self.preference.append(x)
        if type(prefer) == str:
            self.preference.append(prefer)
        self.preference.sort()

    def add_champ_to_pool(self, name):
        if type(name) == list:
            for x in name:
                self.pool.append(ChampionList.find(x))
        if type(name) == str:
            self.pool.append(ChampionList.find(name))
