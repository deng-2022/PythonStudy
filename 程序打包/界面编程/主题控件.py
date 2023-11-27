from tkinter import *
from tkinter.ttk import *


def test1():
    window = Tk()
    btn = Button(
        text="Click me!",
        width=25
    )
    btn.pack()
    window.mainloop()


def test2():
    window = Tk()
    style = Style()
    print(style.theme_names())
    print(style.theme_use())
    btn = Button(
        text="Click me!",
        width=25
    )
    btn.pack()
    window.mainloop()


def test3():
    window = Tk()
    progressbar = Progressbar(
        master=window,
        maximum=50,
        value=35
    )
    progressbar.pack()
    window.mainloop()


if __name__ == '__main__':
    test3()
