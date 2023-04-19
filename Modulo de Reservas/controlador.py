from tkinter import Tk
import vista
import observer
"""En este modulo se ejecuta la aplicacion de Reservas
"""


class Controller:
    def __init__(self, master):
        self.master_controler = master
        self.objeto_vista = vista.MiVista(self.master_controler)
        self.el_observador = observer.ConcreteObserverA(self.objeto_vista.obj )


if __name__ == "__main__":
    master = Tk()
    Controller(master)
    master.mainloop()
