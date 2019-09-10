import tkinter as tk

from Champion.Champ_List import ChampionList
from Champion.Score.ScoreCalculator import Scorecalculator
from Champion.Score.decisionTree import ScoreAVLTree
from Game.CurrentGame import Game
from User.User import User


class ChampionTool(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame()
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (recommandationpage,ChampionPage, Championselectionpage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.champ = None
        self.show_frame(ChampionPage)

    def get_page(self, page_class):
        return self.frames[page_class]

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class ChampionPage(tk.Frame):

    def __init__(self, parent, controller):
        self.champ = None
        self.CL = ChampionList()
        self.CG = Game()
        self.user = User("doesn't matter")
        self.a = 0
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
        self.a4 = 0
        self.e1 = 0
        self.e2 = 0
        self.e3 = 0
        self.e4 = 0
        self.e5 = 0
        self.controller = controller

        tk.Frame.__init__(self, parent)
        "SET UP BUTTON FOR CHARACTER SELECTION"
        achamp_1 = tk.Button(self, text="select Champ1",
                             command=lambda:[self.specific_position(1, 'a'), controller.show_frame(Championselectionpage)])
        achamp_2 = tk.Button(self, text="select Champ2",
                             command=lambda:[self.specific_position(2, 'a'), controller.show_frame(Championselectionpage)])
        achamp_3 = tk.Button(self, text="select Champ3",
                             command=lambda:[self.specific_position(3, 'a'), controller.show_frame(Championselectionpage)])
        achamp_4 = tk.Button(self, text="select Champ4",
                             command=lambda:[self.specific_position(4, 'a'), controller.show_frame(Championselectionpage)])
        echamp_1 = tk.Button(self, text="select enemy Champ1",
                             command=lambda:[self.specific_position(1, 'e'), controller.show_frame(Championselectionpage)])
        echamp_2 = tk.Button(self, text="select enemy Champ2",
                             command=lambda:[self.specific_position(2, 'e'), controller.show_frame(Championselectionpage)])
        echamp_3 = tk.Button(self, text="select enemy Champ3",
                             command=lambda:[self.specific_position(3, 'e'), controller.show_frame(Championselectionpage)])
        echamp_4 = tk.Button(self, text="select enemy Champ4",
                             command=lambda:[self.specific_position(4, 'e'), controller.show_frame(Championselectionpage)])
        echamp_5 = tk.Button(self, text="select enemy Champ5",
                             command=lambda:[self.specific_position(5, 'e'), controller.show_frame(Championselectionpage)])
        achamp_1.grid(row=0, column=0, padx=50, pady=50, sticky="nsew")
        achamp_2.grid(row=0, column=1, padx=50, pady=50, sticky="nsew")
        achamp_3.grid(row=0, column=2, padx=50, pady=50, sticky="nsew")
        achamp_4.grid(row=0, column=3, padx=50, pady=50, sticky="nsew")
        echamp_1.grid(row=1, column=0, padx=50, pady=50, sticky="nsew")
        echamp_2.grid(row=1, column=1, padx=50, pady=50, sticky="nsew")
        echamp_3.grid(row=1, column=2, padx=50, pady=50, sticky="nsew")
        echamp_4.grid(row=1, column=3, padx=50, pady=50, sticky="nsew")
        echamp_5.grid(row=1, column=4, padx=50, pady=50, sticky="nsew")

        poolbutton = tk.Button(self, text="MainChamp",command=lambda:[self.specific_position(0, 'm'),
                                                                      controller.show_frame(Championselectionpage)])
        poolbutton.grid(row=0, column = 4, padx=50, pady=50)
        CPP = self.controller.get_page(recommandationpage)
        resultbutton = tk.Button(self, text="RESULT" , command=lambda: [recommandationpage.outputrecommanded(CPP),
                                                                     controller.show_frame(recommandationpage)])
        resultbutton.grid(row=2, column=2, padx=50, pady=50)

    def get_champ(self):
        CP = self.controller.get_page(Championselectionpage)
        self.champ = CP.champ
        champ = self.CL.find_champ(self.champ)
        x = "character pic/{}Square.png".format(self.champ)
        photo = tk.PhotoImage(file=x)
        if self.a1 == 1:
            cb = tk.Button(self, image=photo,command=lambda: [self.specific_position(1, 'a'),
                                                              self.controller.show_frame(Championselectionpage)])
            cb.image = photo
            cb.grid(row=0, column=0, padx=50, pady=50)
            self.CG.add_champ(champ, 1, 'a')

        if self.a2 == 1:
            cb = tk.Button(self, image=photo,command=lambda: [self.specific_position(2, 'a'),
                                                              self.controller.show_frame(Championselectionpage)])
            cb.image = photo
            cb.grid(row=0, column=1, padx=50, pady=50)
            self.CG.add_champ(champ, 2,'a')
        if self.a3 == 1:
            cb = tk.Button(self, image=photo,command=lambda: [self.specific_position(3, 'a'),
                                                              self.controller.show_frame(Championselectionpage)])
            cb.image = photo
            cb.grid(row=0, column=2, padx=50, pady=50)
            self.CG.add_champ(champ, 3,'a')
        if self.a4 == 1:
            cb = tk.Button(self, image=photo,command=lambda: [self.specific_position(4, 'a'),
                                                              self.controller.show_frame(Championselectionpage)])
            cb.image = photo
            cb.grid(row=0, column=3, padx=50, pady=50)
            self.CG.add_champ(champ, 4,'a')

        if self.e1 == 1:
            cb = tk.Button(self, image=photo,command=lambda: [self.specific_position(1, 'e'),
                                                              self.controller.show_frame(Championselectionpage)])
            cb.image = photo
            cb.grid(row=1,column=0,padx=50, pady=50)
            self.CG.add_champ(champ, 1,'e')
        if self.e2 == 1:
            cb = tk.Button(self, image=photo,command=lambda: [self.specific_position(2, 'e'),
                                                              self.controller.show_frame(Championselectionpage)])
            cb.image = photo
            cb.grid(row=1, column=1, padx=50, pady=50)
            self.CG.add_champ(champ, 2,'e')
        if self.e3 == 1:
            cb = tk.Button(self, image=photo,command=lambda: [self.specific_position(3, 'e'),
                                                              self.controller.show_frame(Championselectionpage)])
            cb.image = photo
            cb.grid(row=1, column=2, padx=50, pady=50)
            self.CG.add_champ(champ, 3, 'e')
        if self.e4 == 1:
            cb = tk.Button(self, image=photo,command=lambda: [self.specific_position(4, 'e'),
                                                              self.controller.show_frame(Championselectionpage)])
            cb.image = photo
            cb.grid(row=1, column=3,  padx=50, pady=50)
            self.CG.add_champ(champ,4 ,'e')
        if self.e5 == 1:
            cb = tk.Button(self, image=photo,command=lambda: [self.specific_position(5, 'e'),
                                                              self.controller.show_frame(Championselectionpage)])
            cb.image = photo
            cb.grid(row=1, column=4, padx=50, pady=50)
            self.CG.add_champ(champ,5, 'e')
        if self.a == 1:
            cb = tk.Button(self, image=photo,command=lambda: [self.specific_position(0, 'm'),
                                                              self.controller.show_frame(Championselectionpage)])
            cb.image = photo
            cb.grid(row=0, column =4, padx=50, pady=50)
            self.user.add_prefer(champ)

    def reset_pos(self):
        self.a = 0
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
        self.a4 = 0
        self.e1 = 0
        self.e2 = 0
        self.e3 = 0
        self.e4 = 0
        self.e5 = 0

    def specific_position(self, position, team):
        if position == 0:
            self.reset_pos()
            self.a = 1
        if team == 'a':
            if position == 1:
                self.reset_pos()
                self.a1 = 1
            if position == 2:
                self.reset_pos()
                self.a2 = 1
            if position == 3:
                self.reset_pos()
                self.a3 = 1
            if position == 4:
                self.reset_pos()
                self.a4 = 1
        if team == 'e':
            if position == 1:
                self.reset_pos()
                self.e1 = 1
            if position == 2:
                self.reset_pos()
                self.e2 = 1
            if position == 3:
                self.reset_pos()
                self.e3 = 1
            if position == 4:
                self.reset_pos()
                self.e4 = 1
            if position == 5:
                self.reset_pos()
                self.e5 = 1

    def print_selected_x(champ):
        print(champ.champ)


class recommandationpage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.final_list = []

        tk.Frame.__init__(self, parent)
        Endbutton =tk.Button(self, text="End Program",command=lambda: self.quit())
        Endbutton.grid(row = 5)

    def outputrecommanded(self):
        cp = self.controller.get_page(ChampionPage)
        CG = cp.CG
        CL = cp.CL
        user = cp.user
        SC = Scorecalculator(CL, CG, user)
        att_list = SC.att_in_need()
        print(att_list)
        SC.calculate_champscore(att_list)
        SAT = ScoreAVLTree()
        TopNode = None
        for x in CL.get_champ_list():
            if x not in CG.achamp and x not in CG.echamp:
                TopNode = SAT.insert(TopNode, x)
        MAX_node = SAT.max_score(TopNode)
        self.final_list = MAX_node.get_champ_list()
        position = 1
        r = 0
        for x in self.final_list:
            x = "character pic/{}Square.png".format(x.name)
            photo = tk.PhotoImage(file=x)
            champion = tk.Label(self, image=photo)
            champion.image= photo
            champion.grid(row=r, column=position)
            if position == 5:
                r +=1
                position =1
            position += 1


class Championselectionpage(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        self.champ = None
        tk.Frame.__init__(self, parent)
        CP = self.controller.get_page(ChampionPage)
        photo1 = tk.PhotoImage(file="character pic/AatroxSquare.png")
        photo2 = tk.PhotoImage(file="character pic/AhriSquare.png")
        photo3 = tk.PhotoImage(file="character pic/AkaliSquare.png")
        photo4 = tk.PhotoImage(file="character pic/AlistarSquare.png")
        photo5 = tk.PhotoImage(file="character pic/AmumuSquare.png")
        photo6 = tk.PhotoImage(file="character pic/AniviaSquare.png")
        photo7 = tk.PhotoImage(file="character pic/AnnieSquare.png")
        photo8 = tk.PhotoImage(file="character pic/AsheSquare.png")
        photo9 = tk.PhotoImage(file="character pic/Aurelion_SolSquare.png")
        photo10 = tk.PhotoImage(file="character pic/AzirSquare.png")
        photo11 = tk.PhotoImage(file="character pic/BardSquare.png")
        photo12 = tk.PhotoImage(file="character pic/BlitzcrankSquare.png")
        photo13 = tk.PhotoImage(file="character pic/BrandSquare.png")
        photo14 = tk.PhotoImage(file="character pic/BraumSquare.png")
        canvas = tk.Canvas(self, width=160, height=160)
        canvas.grid(row=1)
        Aatroxbutton = tk.Button(self, image=photo1, command=lambda: [self.return_Aatrox(), ChampionPage.get_champ(CP), controller.show_frame(ChampionPage)])
        ahributton = tk.Button(self, image=photo2, command=lambda: [self.return_Ahri(), ChampionPage.get_champ(CP), controller.show_frame(ChampionPage)])
        Akalibutton = tk.Button(self, image=photo3, command=lambda: [self.return_Akali(), ChampionPage.get_champ(CP), controller.show_frame(ChampionPage)])
        Alistarbutton = tk.Button(self, image=photo4, command=lambda: [self.return_Alistar(), ChampionPage.get_champ(CP), controller.show_frame(ChampionPage)])
        Amumubutton = tk.Button(self, image=photo5, command=lambda: [self.return_Amumu(), ChampionPage.get_champ(CP), controller.show_frame(ChampionPage)])
        Aniviabutton = tk.Button(self, image=photo6, command=lambda: [self.return_Anivia(), ChampionPage.get_champ(CP), controller.show_frame(ChampionPage)])
        Anniebutton = tk.Button(self, image=photo7, command=lambda: [self.return_Annie(), ChampionPage.get_champ(CP), controller.show_frame(ChampionPage)])
        ashebutton = tk.Button(self, image=photo8, command=lambda: [self.return_Ashe(), ChampionPage.get_champ(CP), controller.show_frame(ChampionPage)])
        Aurelion_Solbutton = tk.Button(self, image=photo9, command=lambda: [self.return_Aurelion(), ChampionPage.get_champ(CP), controller.show_frame(ChampionPage)])
        Azirbutton = tk.Button(self, image=photo10, command=lambda: [self.return_Azir(), ChampionPage.get_champ(CP), controller.show_frame(ChampionPage)])
        Bardbutton = tk.Button(self, image=photo11, command=lambda: [self.return_Bard(), ChampionPage.get_champ(CP), controller.show_frame(ChampionPage)])
        Blitzcrankbutton = tk.Button(self, image=photo12, command=lambda: [self.return_Blitzcrank(), ChampionPage.get_champ(CP), controller.show_frame(ChampionPage)])
        Brandbutton = tk.Button(self, image=photo13, command=lambda: [self.return_Brand(), ChampionPage.get_champ(CP), controller.show_frame(ChampionPage)])
        Braumbutton = tk.Button(self, image=photo14, command=lambda: [self.return_Braum(), ChampionPage.get_champ(CP), controller.show_frame(ChampionPage)])
        Aatroxbutton.image = photo1
        ahributton.image = photo2
        Akalibutton.image = photo3
        Alistarbutton.image = photo4
        Amumubutton.image = photo5
        Aniviabutton.image =photo6
        Anniebutton.image = photo7
        ashebutton.image = photo8
        Aurelion_Solbutton.image = photo9
        Azirbutton.image = photo10
        Bardbutton.image = photo11
        Blitzcrankbutton.image = photo12
        Brandbutton.image = photo13
        Braumbutton.image = photo14
        Aatroxbutton.grid(row=1,column=1)
        ahributton.grid(row=1,column=2)
        Akalibutton.grid(row=1,column=3)
        Alistarbutton.grid(row=1,column=4)
        Amumubutton.grid(row=1,column=5)
        Aniviabutton.grid(row=2, column = 1)
        Anniebutton.grid(row=2,column=2)
        ashebutton.grid(row=2,column=3)
        Aurelion_Solbutton.grid(row=2, column=4)
        Azirbutton.grid(row=2, column=5)
        Bardbutton.grid(row=3, column= 1)
        Blitzcrankbutton.grid(row=3, column=2)
        Brandbutton.grid(row=3, column=3)
        Braumbutton.grid(row=3, column=4)
        canvas.grid()

    def return_Aatrox(self):
        self.champ = "Aatrox"

    def return_Akali(self):
        self.champ = "Akali"

    def return_Alistar(self):
        self.champ = "Alistar"

    def return_Amumu(self):
        self.champ ="Amumu"

    def return_Anivia(self):
        self.champ ="Anivia"

    def return_Annie(self):
        self.champ ="Annie"

    def return_Aurelion(self):
        self.champ = "Aurelion_Sol"

    def return_Azir(self):
        self.champ = "Azir"

    def return_Bard(self):
        self.champ = "Bard"

    def return_Blitzcrank(self):
        self.champ = "Blitzcrank"

    def return_Brand(self):
        self.champ = "Brand"

    def return_Braum(self):
        self.champ ="Braum"

    def return_Ahri(self):
        self.champ = "Ahri"

    def return_Ashe(self):
        self.champ = "Ashe"


Tool = ChampionTool()
Tool.mainloop()
