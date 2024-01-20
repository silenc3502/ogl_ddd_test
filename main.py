import tkinter

from domain_frame.window.domain_window import DomainWindow


def main():
    root = tkinter.Tk()
    window = DomainWindow(root, width=800, height=800)
    window.pack(fill=tkinter.BOTH, expand=1)

    toggle_button = tkinter.Button(root, text="Toggle Visibility", command=window.toggle_visibility)
    toggle_button.place(x=100, y=10)

    root.mainloop()


if __name__ == "__main__":
    main()
