from tkinter import *


class introducemodelo():  # interface to introduce the model, if the model is  blank the program will launch the calculation for all models
    def __init__(self):
        self.newWindow()

    def newWindow(self):
        # define your window
        root = Tk()
        root.geometry("400x100")
        root.resizable(False, False)
        root.title("Modelo Application")
        # add labels
        label1 = Label(text='Introduce el modelo')
        label1.pack()
        canvas1 = Canvas(root)
        canvas1.pack()
        entry1 = Entry(root)
        canvas1.create_window(200, 20, window=entry1)

        def addmodelo():
            global modelo_input
            modelo_input = entry1.get()
        button1 = Button(canvas1, text='Run Report', command=addmodelo)
        canvas1.create_window(200, 50, window=button1)
        root.mainloop()


def modelovar():
    modelovar = modelo_input
    return modelovar
