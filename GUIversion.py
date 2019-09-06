import tkinter as tk


class ChampionTool(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame()
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight= 1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (ChampionPage, Championselectionpage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky="nsew")
        self.champ = None
        self.show_frame(ChampionPage)


    def get_page(self, page_class):
        return self.frames[page_class]

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



class ChampionPage(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        self.champ = None
        tk.Frame.__init__(self, parent)
        achamp_1 = tk.Label(self, text="champ1")
        achamp_2 = tk.Label(self, text="champ2")
        achamp_3 = tk.Label(self, text="champ3")
        achamp_4 = tk.Label(self, text="champ4")
        echamp_1 = tk.Label(self, text="enemy champ1")
        echamp_2 = tk.Label(self, text="enemy champ2")
        echamp_3 = tk.Label(self, text="enemy champ3")
        echamp_4 = tk.Label(self, text="enemy champ4")
        echamp_5 = tk.Label(self, text="enemy champ5")
        achamp_1.grid(row=0, padx=50, pady=50)
        achamp_2.grid(row=1, padx=50, pady=50)
        achamp_3.grid(row=2, padx=50, pady=50)
        achamp_4.grid(row=3, padx=50, pady=50)

        echamp_1.grid(row=0, column=2, padx=50, pady=50)
        echamp_2.grid(row=1, column=2, padx=50, pady=50)
        echamp_3.grid(row=2, column=2, padx=50, pady=50)
        echamp_4.grid(row=3, column=2, padx=50, pady=50)
        echamp_5.grid(row=3, column=2, padx=50, pady=50)
        reloadbutton = tk.Button(self, text="reload", command=self.get_champ)
        if self.champ is None:
            poolbutton = tk.Button(self, text="MainChamp", command=lambda: controller.show_frame(Championselectionpage))
            poolbutton.grid(row=4, padx=50, pady=50)
        else:
            photo = tk.PhotoImage(file="AhriSquare.png")
            canvas = tk.Canvas(self, width=160, height=160)
            canvas.grid(row=1)
            ahributton = tk.Button(self, image=photo)
            ahributton.grid(row=4, padx=50, pady=50)
        reloadbutton.grid(row=4, column=2, padx=50, pady=50)

    def get_champ(self):
        champpage = self.controller.get_page(Championselectionpage)
        self.champ = champpage.champ
        x = "{}Square.png".format(self.champ)
        photo = tk.PhotoImage(file=x)
        canvas = tk.Canvas(self, width=160, height=160)
        canvas.grid(row=1)
        ahributton = tk.Button(self, image=photo)
        ahributton.image = photo
        ahributton.grid(row=4, padx=50, pady=50)

    def print_selected_x(champ):
        print(champ.champ)


class Championselectionpage(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        self.champ = None
        tk.Frame.__init__(self, parent)
        photo = tk.PhotoImage(file="AhriSquare.png")
        canvas = tk.Canvas(self, width=160, height=160)
        canvas.grid(row=1)
        ahributton = tk.Button(self, image=photo, command=self.return_Ahri)
        printbutton = tk.Button(self, text="print", command=self.print_selected_x)
        ChampionPage.champ= self.champ
        printbutton.grid(row=4, column=2, padx=50, pady=50)
        ahributton.image = photo
        backbutton = tk.Button(self, text="Back to Main", command=lambda: controller.show_frame(ChampionPage))
        backbutton.grid()
        canvas.grid(row=1)
        ahributton.grid(row=1)


    def print_selected_x(champ):
        print(champ.champ)

    def return_Ahri(x):
        x.champ = "Ahri"


Tool = ChampionTool()
Tool.mainloop()