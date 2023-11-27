import tkinter as tk
from tkinter.ttk import *


def test1():
    window = tk.Tk()
    window.title("hello world !")
    window.mainloop()


def test2():
    window = tk.Tk()

    lbl = tk.Label(
        master=window,
        text="display text with tkinter framework",
        fg="white",
        bg="black",
        width=40,
        height=10
    )
    lbl.pack()

    window.mainloop()


def test3():
    window = tk.Tk()

    # 显示文本
    var_lbl = tk.StringVar()
    var_lbl.set("display text with tkinter framework")

    lbl = tk.Label(
        master=window,
        fg="white",
        bg="black",
        width=40,
        height=10,
        textvariable=var_lbl
    )

    lbl.pack()
    print(f"{var_lbl.get()}")
    window.mainloop()


def test4():
    window = tk.Tk()

    btn = tk.Button(
        text="Click me!",
        width=10,
        height=5,
        bg="blue",
        fg="yellow"
    )
    btn.pack()

    window.mainloop()


def test5():
    window = tk.Tk()

    frame = tk.Frame()
    label = tk.Label(
        master=frame,
        text="I'm a label in Frame"
    )
    label.pack()

    button = tk.Button(
        master=frame,
        text="I'm a button in Frame"
    )

    button.pack()
    frame.pack()

    window.mainloop()


def test6():
    window = tk.Tk()

    frame = tk.Frame()

    label = tk.Label(
        master=frame,
        text="I'm a label in Frame"
    )

    button = tk.Button(
        master=frame,
        text="I'm a button in Frame"
    )

    button.pack()
    label.pack()
    frame.pack()

    window.mainloop()


def test7():
    window = tk.Tk()
    entry = tk.Entry(
        fg="black",
        bg="white",
        width=50
    )
    entry.pack()
    window.mainloop()


def test8():
    window = tk.Tk()

    text = tk.Text(
        fg="black",
        bg="white",
        width=50
    )

    text.insert("1.1", "Hello")
    text.insert("2.1", "Hi")
    text.insert("3.1", "Fuck")

    text.pack()
    window.mainloop()


def test9():
    window = tk.Tk()
    spinbox = tk.Spinbox(
        master=window,
        from_=0,
        to=100,
        increment=1
    )
    spinbox.pack()
    window.mainloop()


def test10():
    window = tk.Tk()
    scale = tk.Scale(
        master=window,
        orient=tk.VERTICAL,
        length=150,
        from_=0,
        to_=200
    )
    scale.pack()
    window.mainloop()


def test11():
    window = tk.Tk()
    contents = ["贵爷", "蔡礼佛", "梁老师", "鸡毛", "胖子"]
    listvar = tk.StringVar(value=contents)
    listbox = tk.Listbox(
        window,
        bd=2,
        bg="#dddddd",
        listvariable=listvar
    )
    listbox.grid()

    contents.append("助班")
    listvar.set(contents)

    window.mainloop()


def test12():
    window = tk.Tk()
    btn = tk.Button(
        text="Click me!",
        width=25
    )
    btn.pack()
    window.mainloop()


if __name__ == '__main__':
    test12()
