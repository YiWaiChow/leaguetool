class Game:
    """ an instance of game to store the champion posiiton that is selected so far"""
    def __init__(self):
        """each of these achamp and echamo represent the current selected chmap beside yourself"""
        self.achamp = [None, None, None, None, None]
        self.echamp = [None, None, None, None, None]

    def add_champ(self, champ, position, team):
        """ set each champ into corresponding location depending on what position and what team it is"""
        if team == "a":
            self.achamp[position-1] = champ
        if team == "e":
            self.echamp[position-1] = champ

    def is_none(self):
        a_found=0
        e_found=0
        for x in self.achamp:
            if x is not None:
                a_found = 1
        for y in self.echamp:
            if y is not None:
                e_found = 1
        return a_found == 0 and e_found == 0
