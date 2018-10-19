def buttons():
    import tkinter
    from tkinter import messagebox

    top = tkinter.Tk()

    value = True

    def yes():
        global value
        value = True
        top.destroy()

    def no():
        global value
        value = False
        top.destroy()

    b = tkinter.Button(top, text='YES', fg='green', command=yes)
    c = tkinter.Button(top, text='NO', fg='red', command=no)

    b.pack()
    c.pack()
    top.mainloop()
    return value
