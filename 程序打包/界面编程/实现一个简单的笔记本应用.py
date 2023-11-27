import tkinter as tk

...


def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Text files", "*.txt"),
            ("All files", "*.*")
        ]
    )
    if not file_path:
        window.title("无标题 - 记事本")
        return
    window.title(f"{file_path} - 记事本")
    txt_edit.delete("1.0",
                    tk.END)
    with open(
            file_path,
            mode="r",
            encoding="utf-8") as input_file:
        txt_edit.insert(
            tk.END,
            input_file.read()
        )


...

...

if __name__ == '__main__':
    window = tk.Tk()
    # 应用名称
    window.title("记事本")

    # 窗口布局
    window.rowconfigure(
        0,
        minsize=100,
        weight=1
    )
    window.columnconfigure(
        1,
        minsize=100,
        weight=1
    )
    # 盒子(框架)
    btn_frame = tk.Frame(
        master=window,
        bd=2
    )
    # 打开
    btn_open = tk.Button(
        master=btn_frame,
        text="打开"
    )
    # 保存
    btn_save_as = tk.Button(
        master=btn_frame,
        text="另存"
    )

    # 布局
    btn_open.grid(
        row=0,
        column=0,
        sticky="ew",
        padx=5,
        pady=5
    )

    btn_save_as.grid(
        row=1,
        column=0,
        sticky="ew",
        padx=5
    )

    btn_frame.grid(
        row=0,
        column=0,
        sticky="ns"
    )

    # 读写区
    txt_edit = tk.Text(master=window)
    txt_edit.grid(
        row=0,
        column=1,
        sticky="nsew"
    )

    btn_open = tk.Button(
        master=btn_frame,
        text="打开",
        command=open_file
    )

    window.mainloop()
