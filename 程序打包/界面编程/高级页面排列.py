import tkinter as tk


def test1():
    window = tk.Tk()

    lbl_1 = tk.Label(
        master=window,
        text="label 1",
        fg="black",
        bg="red",
        width=10,
        height=5
    )
    lbl_1.pack()

    lbl_2 = tk.Label(
        master=window,
        text="label 2",
        fg="black",
        bg="yellow",
        width=10,
        height=5
    )
    lbl_2.pack()

    lbl_3 = tk.Label(
        master=window,
        text="label 3",
        fg="black",
        bg="blue",
        width=10,
        height=5
    )
    lbl_3.pack(side=tk.LEFT)

    window.mainloop()


def test2():
    window = tk.Tk()

    lbl_1 = tk.Label(
        master=window,
        text="label 1",
        fg="black",
        bg="red",
        width=10,
        height=5
    )
    lbl_1.pack(side=tk.LEFT)

    lbl_2 = tk.Label(
        master=window,
        text="label 2",
        fg="black",
        bg="yellow",
        width=10,
        height=5
    )
    lbl_2.pack(side=tk.LEFT)

    lbl_3 = tk.Label(
        master=window,
        text="label 3",
        fg="black",
        bg="blue",
        width=10,
        height=5
    )
    lbl_3.pack(side=tk.LEFT)

    window.mainloop()


def test3():
    window = tk.Tk()

    lbl_1 = tk.Label(
        master=window,
        text="label 1",
        fg="black",
        bg="red",
        width=10,
        height=5
    )
    lbl_1.pack(fill=tk.BOTH, expand=tk.TRUE)

    lbl_2 = tk.Label(
        master=window,
        text="label 2",
        fg="black",
        bg="yellow",
        width=10,
        height=5
    )
    lbl_2.pack(fill=tk.BOTH, expand=tk.TRUE)

    lbl_3 = tk.Label(
        master=window,
        text="label 3",
        fg="black",
        bg="blue",
        width=10,
        height=5
    )
    lbl_3.pack(fill=tk.BOTH, expand=tk.TRUE)

    window.mainloop()


def test4():
    window = tk.Tk()

    for i in range(3):
        for j in range(3):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.grid(row=i, column=j)
            label = tk.Label(
                master=frame,
                text=f"Row {i}\nColumn {j}"
            )
            label.pack()

    window.mainloop()


def test5():
    window = tk.Tk()

    for i in range(3):
        window.rowconfigure(i, weight=1)
        window.columnconfigure(i, weight=1)

        for j in range(3):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.grid(row=i, column=j)
            label = tk.Label(
                master=frame,
                text=f"Row {i}\nColumn {j}"
            )
            label.pack()

    window.mainloop()


def test6():
    window = tk.Tk()

    label1 = tk.Label(
        master=window,
        text="place (0, 0)",
        bg="yellow"
    )
    label1.place(x=0, y=0)

    label2 = tk.Label(
        master=window,
        text="place (40, 40)",
        bg="green"
    )
    label2.place(x=40, y=40)

    window.mainloop()


def test7():
    def handle_keypress(event):
        print(event.char)

    window = tk.Tk()
    window.bind("<Key>", handle_keypress)
    window.mainloop()


def test8():
    def handle_keypress():
        print("clicked")

    window = tk.Tk()
    button = tk.Button(
        master=window,
        text="click me!",
        command=handle_keypress
    )
    button.pack()
    window.mainloop()


if __name__ == '__main__':
    test7()
