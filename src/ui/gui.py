from tkinter import Frame, Button, OptionMenu, StringVar, colorchooser, Canvas, Entry, Tk
from tkinter.font import families
from services.html_builder import HTML_builder

class MainApplication(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.html_builder = HTML_builder()
        self.pack(fill="both", expand=True)
        self.create_widgets()
        self.create_fixed_frame()
        self.selected_color = "black"  # Oletusarvoinen tekstiväri
        self.latest_text = ""
        self.clicked_x = 0  # Alustetaan klikkauksen x-koordinaatti
        self.clicked_y = 0

    def create_widgets(self):
        self.font_family = StringVar(self)
        self.font_family.set(families(self)[0])  # Asetetaan oletusfontti
        self.font_menu = OptionMenu(self, self.font_family, *families(self))  # Fonttivalikko
        self.font_menu.pack(side="top", fill="x")

        self.font_size = StringVar(self)
        self.font_size.set("12")  # Oletusfontin koko
        self.font_size_menu = OptionMenu(self, self.font_size, *(str(x) for x in range(8, 49, 2)))  # Fonttikokovalikko
        self.font_size_menu.pack(side="top", fill="x")

        self.color_button = Button(self, text="Valitse väri", command=self.choose_color)  # Värinvalintanappi
        self.color_button.pack(side="top", fill="x")

        self.canvas = Canvas(self, bg="white")  # Canvas-alue, jonne teksti lisätään
        self.canvas.pack(fill="both", expand=True, side="left")
        self.canvas.bind("<Button-1>", self.create_text_widget)  # Reagoidaan hiiren klikkaukseen

        self.create_button = Button(self, text="Luo dokumentti", command=self.create_document)  # Dokumentinluontinappi
        self.create_button.pack(side="bottom", fill="x")

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Valitse väri")[1]  # Värinvalintaikkuna
        if color_code:
            self.selected_color = color_code  # Tallennetaan valittu väri

    def create_text_widget(self, event):
        entry_widget = Entry(self.canvas, fg=self.selected_color, font=(self.font_family.get(), int(self.font_size.get())))
        entry_widget.place(x=event.x, y=event.y)

        # Tallennetaan klikkauksen koordinaatit
        self.clicked_x = event.x
        self.clicked_y = event.y

        def save_entry(event=None):
            text = entry_widget.get()
            if text:
                # Käytetään tallennettuja koordinaatteja tekstiä lisättäessä
                self.canvas.create_text(self.clicked_x, self.clicked_y, text=text, anchor="nw", fill=self.selected_color, font=(self.font_family.get(), int(self.font_size.get())))
                self.latest_text = text  # Tallennetaan käyttäjän kirjoittama teksti
                self.html_builder.import_text(text)  # Oikea kohta kutsua HTML_builder-metodia
            entry_widget.destroy()

        entry_widget.bind("<Return>", save_entry)
        entry_widget.focus()

    def create_fixed_frame(self):
        fixed_frame = Frame(self.master, width=400, height=200, background="red")
        fixed_frame.pack_propagate(False)  # Prevents the frame from resizing to fit its contents
        fixed_frame.pack(side="top", fill="both", expand=False)

    def create_document(self):
        # Tähän tulee toiminnallisuus dokumentin luomiselle
        pass
