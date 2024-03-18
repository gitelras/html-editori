from tkinter import Tk, Frame, Label, Button, OptionMenu, StringVar, colorchooser
from tkinter.font import Font, families

class MainApplication(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.font_family = StringVar(self)
        self.font_family.set(families(self)[0]) 
        self.font_menu = OptionMenu(self, self.font_family, *families(self))
        self.font_menu.pack()

        self.font_size = StringVar(self)
        self.font_size.set("12")
        self.font_size_menu = OptionMenu(self, self.font_size, *(str(x) for x in range(8, 49, 2)))
        self.font_size_menu.pack()

        self.color_button = Button(self, text="Valitse väri", command=self.choose_color)
        self.color_button.pack()

        self.create_button = Button(self, text="Luo dokumentti", command=self.create_document)
        self.create_button.pack()

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Valitse väri")
        print(color_code)  # aseta tekstielementin väri

    def create_document(self):
        pass