import tkinter

from domain_frame.window.domain_window import DomainWindow
from new_try.frame.new_battle_field_unit_card_frame import NewBattleFieldUnitCardFrame


# def main():
#     root = tkinter.Tk()
#     # root.attributes('-fullscreen', True)
#     root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
#
#     window = DomainWindow(root)
#     window.pack(fill=tkinter.BOTH, expand=1)
#
#     toggle_button = tkinter.Button(root, text="Toggle Visibility", command=window.toggle_visibility)
#     toggle_button.place(x=100, y=10)
#
#     # def toggle_fullscreen(event):
#     #     root.attributes('-fullscreen', not root.attributes('-fullscreen'))
#     #
#     # root.bind('<Double-Button-1>', toggle_fullscreen)
#
#     root.mainloop()

def main():
    root = tkinter.Tk()
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
    root.deiconify()

    window = NewBattleFieldUnitCardFrame(root)
    window.pack(fill=tkinter.BOTH, expand=1)

    toggle_button = tkinter.Button(root, text="Toggle Visibility", command=window.toggle_visibility)
    toggle_button.place(x=100, y=10)

    root.mainloop()


if __name__ == "__main__":
    main()
