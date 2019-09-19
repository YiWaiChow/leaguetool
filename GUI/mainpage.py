"""the frist frame when you enter the progamn, main page with button of different function"""
import tkinter as tk

from Champion.Champ_List import ChampionList
import GUI.Championselectionpage
from GUI.recommandationpage import recommandationpage
from Game.CurrentGame import Game
from User.User import User


class ChampionPage(tk.Frame):
    """the main frame"""

    def __init__(self, parent, controller):
        """ initialized all the button"""
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
        background_image = tk.PhotoImage(file="character pic/XDXDXDXD.png")
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        "styling"
        "SET UP BUTTON FOR CHARACTER SELECTION"
        x = GUI.Championselectionpage.Championselectionpage
        achamp_1 = tk.Button(self, text="select Champ1", borderwidth=10,
                             command=lambda: [self.specific_position(1, 'a'),
                                              controller.show_frame(x)])
        achamp_2 = tk.Button(self, text="select Champ2",
                             command=lambda: [self.specific_position(2, 'a'),
                                              controller.show_frame(x)])
        achamp_3 = tk.Button(self, text="select Champ3",
                             command=lambda: [self.specific_position(3, 'a'),
                                              controller.show_frame(x)])
        achamp_4 = tk.Button(self, text="select Champ4",
                             command=lambda: [self.specific_position(4, 'a'),
                                              controller.show_frame(x)])
        echamp_1 = tk.Button(self, text="select enemy Champ1", borderwidth=10,
                             command=lambda: [self.specific_position(1, 'e'),
                                              controller.show_frame(x)])
        echamp_2 = tk.Button(self, text="select enemy Champ2",
                             command=lambda: [self.specific_position(2, 'e'),
                                              controller.show_frame(x)])
        echamp_3 = tk.Button(self, text="select enemy Champ3",
                             command=lambda: [self.specific_position(3, 'e'),
                                              controller.show_frame(x)])
        echamp_4 = tk.Button(self, text="select enemy Champ4",
                             command=lambda: [self.specific_position(4, 'e'),
                                              controller.show_frame(x)])
        echamp_5 = tk.Button(self, text="select enemy Champ5",
                             command=lambda: [self.specific_position(5, 'e'),
                                              controller.show_frame(x)])
        achamp_1.grid(row=0, column=0, padx=50, pady=50, sticky="nsew")
        achamp_2.grid(row=0, column=1, padx=50, pady=50, sticky="nsew")
        achamp_3.grid(row=0, column=2, padx=50, pady=50, sticky="nsew")
        achamp_4.grid(row=0, column=3, padx=50, pady=50, sticky="nsew")
        echamp_1.grid(row=1, column=0, padx=50, pady=50, sticky="nsew")
        echamp_2.grid(row=1, column=1, padx=50, pady=50, sticky="nsew")
        echamp_3.grid(row=1, column=2, padx=50, pady=50, sticky="nsew")
        echamp_4.grid(row=1, column=3, padx=50, pady=50, sticky="nsew")
        echamp_5.grid(row=1, column=4, padx=50, pady=50, sticky="nsew")

        poolbutton = tk.Button(self, text="MainChamp", command=lambda: [self.specific_position(0, 'm'),
                                                                        controller.show_frame(x)])
        poolbutton.grid(row=0, column=4, padx=50, pady=50)
        cpp = self.controller.get_page(recommandationpage)
        resultbutton = tk.Button(self, text="RESULT", command=lambda: [recommandationpage.outputrecommanded(cpp),
                                                                       controller.show_frame(recommandationpage)])
        resultbutton.place(relx=0.665, rely=0.75, anchor="c")

    """ set the current champion inorder for button to output the correct image"""

    def get_champ(self):
        """get back the result from championselection frame for the purpose of outputting correct champion icon"""
        y = GUI.Championselectionpage.Championselectionpage
        cp = self.controller.get_page(y)
        self.champ = cp.champ
        champ = self.CL.find_champ(self.champ)
        x = "character pic/{}Square.png".format(self.champ)
        photo = tk.PhotoImage(file=x)
        if self.a1 == 1:
            cb = tk.Button(self, image=photo, command=lambda: [self.specific_position(1, 'a'),
                                                               self.controller.show_frame(y)])
            cb.image = photo
            cb.grid(row=0, column=0, padx=50, pady=50)
            self.CG.add_champ(champ, 1, 'a')

        if self.a2 == 1:
            cb = tk.Button(self, image=photo, command=lambda: [self.specific_position(2, 'a'),
                                                               self.controller.show_frame(y)])
            cb.image = photo
            cb.grid(row=0, column=1, padx=50, pady=50)
            self.CG.add_champ(champ, 2, 'a')
        if self.a3 == 1:
            cb = tk.Button(self, image=photo, command=lambda: [self.specific_position(3, 'a'),
                                                               self.controller.show_frame(y)])
            cb.image = photo
            cb.grid(row=0, column=2, padx=50, pady=50)
            self.CG.add_champ(champ, 3, 'a')
        if self.a4 == 1:
            cb = tk.Button(self, image=photo, command=lambda: [self.specific_position(4, 'a'),
                                                               self.controller.show_frame(y)])
            cb.image = photo
            cb.grid(row=0, column=3, padx=50, pady=50)
            self.CG.add_champ(champ, 4, 'a')

        if self.e1 == 1:
            cb = tk.Button(self, image=photo, command=lambda: [self.specific_position(1, 'e'),
                                                               self.controller.show_frame(y)])
            cb.image = photo
            cb.grid(row=1, column=0, padx=50, pady=50)
            self.CG.add_champ(champ, 1, 'e')
        if self.e2 == 1:
            cb = tk.Button(self, image=photo, command=lambda: [self.specific_position(2, 'e'),
                                                               self.controller.show_frame(y)])
            cb.image = photo
            cb.grid(row=1, column=1, padx=50, pady=50)
            self.CG.add_champ(champ, 2, 'e')
        if self.e3 == 1:
            cb = tk.Button(self, image=photo, command=lambda: [self.specific_position(3, 'e'),
                                                               self.controller.show_frame(y)])
            cb.image = photo
            cb.grid(row=1, column=2, padx=50, pady=50)
            self.CG.add_champ(champ, 3, 'e')
        if self.e4 == 1:
            cb = tk.Button(self, image=photo, command=lambda: [self.specific_position(4, 'e'),
                                                               self.controller.show_frame(y)])
            cb.image = photo
            cb.grid(row=1, column=3, padx=50, pady=50)
            self.CG.add_champ(champ, 4, 'e')
        if self.e5 == 1:
            cb = tk.Button(self, image=photo, command=lambda: [self.specific_position(5, 'e'),
                                                               self.controller.show_frame(y)])
            cb.image = photo
            cb.grid(row=1, column=4, padx=50, pady=50)
            self.CG.add_champ(champ, 5, 'e')
        if self.a == 1:
            cb = tk.Button(self, image=photo, command=lambda: [self.specific_position(0, 'm'),
                                                               self.controller.show_frame(y)])
            cb.image = photo
            cb.grid(row=0, column=4, padx=50, pady=50)
            self.user.add_prefer(champ)

    def reset_pos(self):
        """ reset the value correspond to which champion slot should be output"""
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
        """ specific the current champion slot by setting the attribute of the current focused champion slot"""
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
