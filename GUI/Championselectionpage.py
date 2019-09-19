""" the frame for which the selection of champion happens"""
import tkinter as tk

from GUI.mainpage import ChampionPage


class Championselectionpage(tk.Frame):
    """ the frame that selects for champion for each champion slot in main frame"""

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
        aatroxbutton = tk.Button(self, image=photo1, command=lambda: [self.set_champ("Aatrox"), ChampionPage.get_champ(CP),
                                                                      controller.show_frame(ChampionPage)])
        ahributton = tk.Button(self, image=photo2, command=lambda: [self.set_champ("Ahri"), ChampionPage.get_champ(CP),
                                                                    controller.show_frame(ChampionPage)])
        akalibutton = tk.Button(self, image=photo3, command=lambda: [self.set_champ("Akali"), ChampionPage.get_champ(CP),
                                                                     controller.show_frame(ChampionPage)])
        alistarbutton = tk.Button(self, image=photo4,
                                  command=lambda: [self.set_champ("Alistar"), ChampionPage.get_champ(CP),
                                                   controller.show_frame(ChampionPage)])
        amumubutton = tk.Button(self, image=photo5, command=lambda: [self.set_champ("Amumu"), ChampionPage.get_champ(CP),
                                                                     controller.show_frame(ChampionPage)])
        aniviabutton = tk.Button(self, image=photo6, command=lambda: [self.set_champ("Anivia"), ChampionPage.get_champ(CP),
                                                                      controller.show_frame(ChampionPage)])
        anniebutton = tk.Button(self, image=photo7, command=lambda: [self.set_champ("Annie"), ChampionPage.get_champ(CP),
                                                                     controller.show_frame(ChampionPage)])
        ashebutton = tk.Button(self, image=photo8, command=lambda: [self.set_champ("Ashe"), ChampionPage.get_champ(CP),
                                                                    controller.show_frame(ChampionPage)])
        aurelion_solbutton = tk.Button(self, image=photo9,
                                       command=lambda: [self.set_champ("Aurelion_Sol"), ChampionPage.get_champ(CP),
                                                        controller.show_frame(ChampionPage)])
        azirbutton = tk.Button(self, image=photo10, command=lambda: [self.set_champ("Azir"), ChampionPage.get_champ(CP),
                                                                     controller.show_frame(ChampionPage)])
        bardbutton = tk.Button(self, image=photo11, command=lambda: [self.set_champ("Bard"), ChampionPage.get_champ(CP),
                                                                     controller.show_frame(ChampionPage)])
        blitzcrankbutton = tk.Button(self, image=photo12,
                                     command=lambda: [self.set_champ("Blitzcrank"), ChampionPage.get_champ(CP),
                                                      controller.show_frame(ChampionPage)])
        brandbutton = tk.Button(self, image=photo13, command=lambda: [self.set_champ("Brand"), ChampionPage.get_champ(CP),
                                                                      controller.show_frame(ChampionPage)])
        braumbutton = tk.Button(self, image=photo14, command=lambda: [self.set_champ("Braum"), ChampionPage.get_champ(CP),
                                                                      controller.show_frame(ChampionPage)])
        aatroxbutton.image = photo1
        ahributton.image = photo2
        akalibutton.image = photo3
        alistarbutton.image = photo4
        amumubutton.image = photo5
        aniviabutton.image = photo6
        anniebutton.image = photo7
        ashebutton.image = photo8
        aurelion_solbutton.image = photo9
        azirbutton.image = photo10
        bardbutton.image = photo11
        blitzcrankbutton.image = photo12
        brandbutton.image = photo13
        braumbutton.image = photo14
        aatroxbutton.grid(row=1, column=1)
        ahributton.grid(row=1, column=2)
        akalibutton.grid(row=1, column=3)
        alistarbutton.grid(row=1, column=4)
        amumubutton.grid(row=1, column=5)
        aniviabutton.grid(row=2, column=1)
        anniebutton.grid(row=2, column=2)
        ashebutton.grid(row=2, column=3)
        aurelion_solbutton.grid(row=2, column=4)
        azirbutton.grid(row=2, column=5)
        bardbutton.grid(row=3, column=1)
        blitzcrankbutton.grid(row=3, column=2)
        brandbutton.grid(row=3, column=3)
        braumbutton.grid(row=3, column=4)
        canvas.grid()

    def set_champ(self, name):
        self.champ = name
