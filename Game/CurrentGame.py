class Game:
    def __init(self):
        "each of these achamp and echamo represent the current selected chmap beside yourself"
        self.achamp = [None, None, None, None, None]
        self.echamp = [None, None, None, None, None]

    def add_champ(self, champ, position,team):
        if team == "a":
            self.achamp[position-1] = champ
        if team == "e":
            self.echamp[position-1] = champ


