# generoitu koodi alkaa
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
        self.selected_color = "black"
        self.clicked_x = 0
        self.clicked_y = 0
# generoitu koodi päättyy
        self.latest_text = ""

# generoitu koodi alkaa
    def choose_color(self): # services
        color_code = colorchooser.askcolor(title="Valitse väri")[1]
        if color_code:
            self.selected_color = color_code
# generoitu koodi päättyy

# generoitu koodi alkaa
    def create_widgets(self):
        self.font_family = StringVar(self)
        fonts = ["Times New Roman", "Arial", "Georgia", "Garamond", "Courier"]
        self.font_family.set(fonts[0])
        self.font_menu = OptionMenu(self, self.font_family, *fonts)
        self.font_menu.pack(side="top", fill="x")

        self.font_size = StringVar(self)
        self.font_size.set("12")
        self.font_size_menu = OptionMenu(
            self, self.font_size, *(str(x) for x in range(8, 49, 2)))
        self.font_size_menu.pack(side="top", fill="x")

        self.color_button = Button(
            self, text="Valitse väri", command=self.choose_color)
        self.color_button.pack(side="top", fill="x")

        self.canvas = Canvas(self, bg="white")
        self.canvas.pack(fill="both", expand=True, side="left")
        self.canvas.bind("<Button-1>", self.create_text_widget)

        self.create_button = Button(
            self, text="Luo dokumentti", command=self.create_document)
        self.create_button.pack(side="bottom", fill="x")
# generoitu koodi päättyy

# generoitu koodi alkaa
    def create_text_widget(self, event):
        entry_widget = Entry(self.canvas, fg=self.selected_color, font=(
            self.font_family.get(), int(self.font_size.get())))
        entry_widget.place(x=event.x, y=event.y)

        self.clicked_x = event.x
        self.clicked_y = event.y

        def save_entry(event=None):
            text = entry_widget.get()
            if text:
                self.canvas.create_text(self.clicked_x, self.clicked_y, text=text, anchor="nw", fill=self.selected_color, font=(
                    self.font_family.get(), int(self.font_size.get())))
                # generoitu koodi päättyy
                self.latest_text = text
                self.html_builder.import_text(text)
            # generoitu koodi alkaa
            entry_widget.destroy()

        entry_widget.bind("<Return>", save_entry)
        entry_widget.focus()
# generoitu koodi päättyy

# generoitu koodi alkaa
    def create_document(self):
        pass
# generoitu koodi päättyy
