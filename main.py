import tkinter

from domain_frame.window.domain_window import DomainWindow


def main():
    root = tkinter.Tk()
    window = DomainWindow(root, width=800, height=800)
    window.pack(fill=tkinter.BOTH, expand=1)

    root.mainloop()


if __name__ == "__main__":
    main()
