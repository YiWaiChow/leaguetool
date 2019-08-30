from Champion import Champions


class ChampionList:
    def __init__(self):
        self.list = []
        aatrox = Champions("Aatrox", ["AD", "AR"])
        ahri = Champions("Ahri", ["AP"])
        akali = Champions("Akali", ["AP"])
        alistar = Champions("Alistar", ["MR", "AR"])
        amumu = Champions("Amumu", ["MR, AR"])
        Anivia = Champions("Anivia", ["AP"])
        Annie = Champions("Annnie", ["AP"])
        Ashe = Champions("Ashe", ["AD"])
        AurelionSol = Champions("Aurelion Sol", ["AP"] )
        Azir = Champions("Azir", ["AP"])
        Bard = Champions("Bard", ["MR", "AR"])
        Blitzcrank = Champions("Blitzcrank", ["MR", "AR"])
        Brand = Champions("Brand", ["AP"])
        self.list.append(aatrox)
        self.list.append(ahri)
        self.list.append(akali)
        self.list.append(alistar)
        self.list.append(amumu)
        self.list.append(Anivia)
        self.list.append(Annie)
        self.list.append(Ashe)
        self.list.append(AurelionSol)
        self.list.append(Azir)
        self.list.append(Bard)
        self.list.append(Blitzcrank)
        self.list.append(Brand)

    def champ_w_attribute(self, attribute):
        temp_list = []
        for x in self.list:
            if attribute in x.attribute:
                temp_list.append(x)
        return temp_list
