
from tkinter import Tk, Canvas, Entry, Frame, Button, OptionMenu, StringVar, colorchooser, Label, Toplevel, Scrollbar
from services.draw_node import DrawNode
from entities.node import Node
from services.html_builder import HtmlBuilder
import tkinter.font as tkFont
import webbrowser
import tempfile
import os

# generoitu koodi alkaa

class MainApplication(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
        self.canvas = Canvas(self, bg="white", width=800, height=600)
        self.canvas.pack(fill="both", expand=True, side="left")
        self.create_entry()
        self.create_html_name_entry()
        self.draw_node = DrawNode(self.canvas, self.entry)
        self.create_widgets()
        self.draw()
        self.html_builder = HtmlBuilder()

    def create_entry(self):
        instruction_label = Label(self, text=("Klikkaa ensin haluamaasi aluetta, kirjoita teksti kenttään ja paina enter"),
                                     width=60,
                                     anchor='w')
        instruction_label.pack(side="top", padx=0, pady=10)
        self.entry = Entry(self, bd=0.5, width=60)
        self.entry.pack(side="top", padx=0, pady=10)
        self.entry.bind("<Return>", lambda event: self.draw_node.on_entry_return(event))

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Valitse väri")[1]
        if color_code:
            self.draw_node.selected_color = color_code

    def create_widgets(self):
        font_family_var = StringVar(self)
        fonts = ["Times New Roman", "Arial", "Georgia", "Garamond", "Courier"]
        font_family_var.set(self.draw_node.font)
        self.font_menu = OptionMenu(self, font_family_var, *fonts, command=self.update_font_family)
        self.font_menu.pack(side="top", fill="x")

        font_size_var = StringVar(self)
        font_size_var.set(str(self.draw_node.font_size))
        self.font_size_menu = OptionMenu(self, font_size_var, *(str(x) for x in range(8, 49, 2)), command=self.update_font_size)
        self.font_size_menu.pack(side="top", fill="x")

        self.color_button = Button(self, text="Valitse väri", command=self.choose_color)
        self.color_button.pack(side="top", fill="x")

        self.html_button = Button(self, text="Näytä HTML", command=self.show_html)
        self.html_button.pack(side="top", fill="x")
        self.show_links()

    def show_links(self):
        def callback(url):
            webbrowser.open_new(url)

        instruction_label = Label(self, text="Luodut dokumentit:", width=60, anchor='w')
        instruction_label.pack(side="top", padx=0, pady=10)

        # Creating a canvas and a vertical scrollbar
        canvas = Canvas(self)
        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas)

        # Configure the canvas
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        files = HtmlBuilder.all_files(self)
        files.reverse()
        font_style = tkFont.Font(size=16, underline=True)

        for file in files:
            file_name = file[1].split('/')[-1]
            link1 = Label(scrollable_frame, text=file_name, fg="white", cursor="hand2", font=font_style)
            link1.pack()
            link1.bind("<Button-1>", lambda e, f='file://' + file[1]: callback(f))

        # Pack everything
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def update_font_family(self, new_family):   
        self.draw_node.font = new_family
        self.draw()

    def update_font_size(self, new_size):
        self.draw_node.font_size = int(new_size)
        self.draw()

    def draw(self):
        self.draw_node.draw_tree()
    
    def clear_error_message(self, _):
        # Clear any text in the message label
        self.message_label.config(text="")
    
    def create_html_name_entry(self):
        instruction_label = Label(self, text="Kirjoita dokumentille nimi", width=60, anchor='w')
        instruction_label.pack(side="top", padx=0, pady=10)

        self.entry_html_name = Entry(self, bd=0.5, width=60)
        self.entry_html_name.pack(side="top", padx=0, pady=10)
        self.entry_html_name.bind("<KeyRelease>", self.clear_error_message)
        
    def show_html(self):
        try:
            self.entered_text = self.entry_html_name.get().strip()
            if not self.entered_text:
                self.message_label = Label(self, text="")
                self.message_label.pack()
                raise ValueError("Dokumentin nimi puuttuu")

            html_content = self.html_builder.html_document(self.draw_node.root_node, self.entered_text)

            with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as f:
                f.write(html_content)
                webbrowser.open('file://' + f.name)
        
        except Exception as e:
            self.message_label.config(text="Virhe: " + str(e), fg="red")
            print(f"Error: {e}")

def main():
    root = Tk()
    root.title("Kodokaze")
    app = MainApplication(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()

# generoitu koodi päättyy

