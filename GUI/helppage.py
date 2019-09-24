""" instruction on how to use the program"""
import tkinter as tk
import GUI.mainpage
from Champion.Score.ScoreCalculator import Scorecalculator
from Champion.Score.decisionTree import ScoreAVLTree


class HelpPage(tk.Frame):
    """the recommandation frame"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_image = tk.PhotoImage(file="character pic/thonking.png")
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=200, y=0, relwidth=1, relheight=1)
        w = tk.Label(self, text="HOW TO USE")
        w.grid(row=0)
        insstruction = tk.Text(self, height=50, width=70)
        text = "each of the champion selection represent \n"+"the champions selected so far in the current game,\n"+" once you finish all the selection,\n press result button to enter the champion recommandation,\n each of the champion displayed has the attribute\n that needed the most in the current game\n"
        insstruction.grid(row=1)
        insstruction.insert(tk.END, text)
        endbutton = tk.Button(self, text="back to main",
                              command=lambda: controller.show_frame(GUI.mainpage.ChampionPage))
        endbutton.place(x=200,y= 200)

