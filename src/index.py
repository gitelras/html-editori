from tkinter import Tk
from ui.gui import MainApplication


def main():
    root = Tk()
    root.title("Kodokaze")
    app = MainApplication(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
