import tkinter


def buttons():
    '''
    This function creates buttons for levels from 1 to 4 to give player a possibility to choose answers
    '''
    top = tkinter.Tk()

    def yes():
        global value
        value = True
        top.destroy()

    def no():
        global value
        value = False
        top.destroy()

    b = tkinter.Button(top, text='YES', fg='green', width=20, command=yes)
    c = tkinter.Button(top, text='NO', fg='red', width=20, command=no)

    top.geometry('100x60+800+500')
    b.pack()
    c.pack()
    top.mainloop()
    return value


def buttons5():
    '''
    This function creates buttons for levels from 1 to 4 to give player a possibility to choose answers
    '''
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

    b = tkinter.Button(top, text='Even', fg='black', width=20, command=parne)
    c = tkinter.Button(top, text='Happy', fg='red', width=20, command=happy)
    d = tkinter.Button(top, text='Ulam', fg='green', width=20, command=ulama)
    e = tkinter.Button(top, text='None of given',
                       fg='blue', width=20, command=nothing)

    top.geometry('100x124+800+500')
    b.pack()
    c.pack()
    d.pack()
    e.pack()
    top.mainloop()
    return value
