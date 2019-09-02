class Scorecalculator:
    def __init__(self, champlist, game, user):
        self.champlist = champlist
        self.game = game
        self.user = user
        "each number in attributelist represent each of the attribute score , lowest is the attribute needed"
        self.attributelist =[0, 0, 0, 0]

    def att_in_need(self):
        for x in self.game.achamp:
            if x:
                for att in x.attribute:
                    if att == "AD":
                        self.attributelist[0] += 1
                    if att == "AP":
                        self.attributelist[1] += 1
                    if att == "AR":
                        self.attributelist[2] += 1
                    if att == "MR":
                        self.attributelist[3] += 1
        for x in self.game.echamp:
            if x:
                for att in x.attribute:
                    if att == "AD":
                        self.attributelist[2] -= 1
                    if att == "AP":
                        self.attributelist[3] -= 1
                    if att == "AR":
                        self.attributelist[1] -= 1
                    if att == "MR":
                        self.attributelist[0] -= 1
        min_score = min(self.attributelist)
        print(self.attributelist)
        att_in_need_list =[]
        position = 0
        for x in self.attributelist:
            if x == min_score:
                if position == 0:
                    att_in_need_list.append("AD")
                if position == 1:
                    att_in_need_list.append("AP")
                if position == 2:
                    att_in_need_list.append("AR")
                if position == 3:
                    att_in_need_list.append("MR")
            position += 1
        return att_in_need_list

    def calculate_champscore(self, list):
        for x in self.champlist.get_champ_list():
            score = 0
            if x in self.user.get_pool():
                score += 1
            for att in list:
                for y in x.attribute:
                    if y == self.user.preference:
                        score += 1
                    if y == att:
                        score += 1
            x.add_score(score)
        return self.champlist
