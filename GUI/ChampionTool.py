"""a starting frame to hold the main page"""
import tkinter as tk

import GUI.Championselectionpage as gc
from GUI.mainpage import ChampionPage
from GUI.recommandationpage import recommandationpage


class ChampionTool(tk.Tk):
    """a container to store all the frame and act as a frame switcher """

    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame()
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (recommandationpage, ChampionPage, gc.Championselectionpage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.champ = None
        self.show_frame(ChampionPage)

    def get_page(self, page_class):
        """ obtain the desire the page to be able to access the attribute store in each the desire page"""
        return self.frames[page_class]

    def show_frame(self, cont):
        """ nagviate to the desire frame(page)"""
        frame = self.frames[cont]
        frame.tkraise()
