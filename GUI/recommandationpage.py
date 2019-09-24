"""the champion selection recommandation page( Frame) """
import tkinter as tk
import GUI.mainpage
from Champion.Score.ScoreCalculator import Scorecalculator
from Champion.Score.decisionTree import ScoreAVLTree


class recommandationpage(tk.Frame):
    """the recommandation frame"""
    def __init__(self, parent, controller):
        self.controller = controller
        self.final_list = []

        tk.Frame.__init__(self, parent)
        endbutton = tk.Button(self, text="End Program", command=lambda: self.quit())
        endbutton.grid(row=5)

    def outputrecommanded(self):
        """calculate and output the recommanded champion image to the frame"""
        background_image = tk.PhotoImage(file="character pic/white.png")
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        cp = self.controller.get_page(GUI.mainpage.ChampionPage)
        cg = cp.CG
        cl = cp.CL
        user = cp.user
        sc = Scorecalculator(cl, cg, user)
        if cg.is_none() is False:
            att_list = sc.att_in_need()
            print(att_list)
            sc.calculate_champscore(att_list)
            sat = ScoreAVLTree()
            topnode = None
            for x in cl.get_champ_list():
                if x not in cg.achamp and x not in cg.echamp:
                    topnode = sat.insert(topnode, x)
            maxnode = sat.max_score(topnode)
            self.final_list = maxnode.get_champ_list()
            position = 1
            r = 0
            for x in self.final_list:
                x = "character pic/{}Square.png".format(x.name)
                photo = tk.PhotoImage(file=x)
                champion = tk.Label(self, image=photo)
                champion.image = photo
                champion.grid(row=r, column=position)
                if position == 5:
                    r += 1
                    position = 1
                position += 1
        backbutton = tk.Button(self, text="back to main", command=lambda: self.controller.show_frame(GUI.mainpage.ChampionPage))
        backbutton.grid(row=1, column=1)
