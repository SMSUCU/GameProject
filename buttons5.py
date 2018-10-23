def buttons():
    import tkinter
    top = tkinter.Tk()

    def parne():
        global value
        value = 1
        top.destroy()

    def happy():
        global value
        value = 2
        top.destroy()

    def ulama():
        global value
        value = 3
        top.destroy()

    def nothing():
        global value
        value = 4
        top.destroy()

    b = tkinter.Button(top, text='Even', fg='black', width=10, command=parne)
    c = tkinter.Button(top, text='Happy', fg='red', width=10, command=happy)
    d = tkinter.Button(top, text='Ulam', fg='green', width=10, command=ulama)
    e = tkinter.Button(top, text='None of given',
                       fg='blue', width=10, command=nothing)

    top.geometry('100x124+600+300')
    b.pack()
    c.pack()
    d.pack()
    e.pack()
    top.mainloop()
    return value