from tkinter import StringVar
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import ttk
from tkinter import Frame
from tkinter import RAISED
from tkinter import CENTER
from tkinter.messagebox import showerror
import sqlite3
from modelo import Abmc


class MiVista:
    """En este modulo se encuentra todo lo relacionado a la visualizacion de
    la aplicacion. Se utiliza Tkinter
    """
    def __init__(self, window):
        self.master = window

        self.obj = Abmc()

        ################################################################
        #   VISUZLIZACION DE LA RESERVA A MODIFICAR
        ################################################################

        def funcion_vm():
            con = sqlite3.connect("reserva.db")

            if not tree.selection():
                showerror(
                    "No selecciono ninguna reserva",
                    "Seleccione una y vuelvalo a intentar",
                )

            else:
                self.cursor = con.cursor()

                item = tree.focus()
                e_ap_y_nom.insert(0, tree.item(item)["values"][0])
                e_documento.insert(0, tree.item(item)["values"][1])
                e_domicilio.insert(0, tree.item(item)["values"][2])
                e_telefono.insert(0, tree.item(item)["values"][3])
                e_mail.insert(0, tree.item(item)["values"][4])
                e_fecha_ing.insert(0, tree.item(item)["values"][5])
                e_fecha_eg.insert(0, tree.item(item)["values"][6])

        def funcion_vb():
            con = sqlite3.connect("reserva.db")

            if not tree.selection():
                showerror(
                    "No selecciono ninguna reserva",
                    "Seleccione una y vuelvalo a intentar",
                )

            else:
                self.cursor = con.cursor()

                for selected_item in tree.selection():
                    item = tree.item(selected_item)
                    record = item["values"]

                self.obj.funcion_b(record, tree)

        ################################################################
        #   TKINTER
        ################################################################

        self.master.geometry("680x500")

        ventana = Frame(self.master, height=22, relief=RAISED)
        ventana.grid(row=10, column=1, columnspan=4, padx=1, pady=1, sticky="w")

        var_ap_y_nom = StringVar()
        var_documento = StringVar()
        var_domicilio = StringVar()
        var_telefono = StringVar()
        var_mail = StringVar()
        var_fecha_ing = StringVar()
        var_fecha_eg = StringVar()

        self.master.title("MODULO DE RESERVAS")

        marco_principal = Frame()
        marco_principal.grid(row=0, column=0, columnspan=4)
        marco_principal.config(width="600", height="25", bg="#2C7AFF")

        marco1 = Frame()
        marco1.grid(row=1, column=0, columnspan=4)
        marco1.config(width="600", height="22")

        marco2 = Frame()
        marco2.grid(row=8, column=0, columnspan=4)
        marco2.config(width="600", height="22")

        marco3 = Frame()
        marco3.grid(row=10, column=0, columnspan=4)
        marco3.config(width="600", height="22")

        marco4 = Frame()
        marco4.grid(row=6, column=0, columnspan=4)
        marco4.config(width="600", height="22")

        ingreso = Label(self.master, text="INGRESAR LA RESERVA")
        ingreso.grid(row=0, column=0, columnspan=4)
        ingreso.config(bg="#2C7AFF", font="bold")

        ap_y_nom = Label(self.master, text="  Ap. y Nombre:")
        ap_y_nom.grid(row=2, column=0, sticky="w")
        e_ap_y_nom = Entry(
            self.master, textvariable=var_ap_y_nom, background="turquoise"
        )
        e_ap_y_nom.grid(row=2, column=1)

        documento = Label(self.master, text="Documento:")
        documento.grid(row=2, column=2, sticky="w")
        e_documento = Entry(
            self.master, textvariable=var_documento, background="turquoise"
        )
        e_documento.grid(row=2, column=3)

        domicilio = Label(self.master, text="  Domicilio:")
        domicilio.grid(row=3, column=0, sticky="w")
        e_domicilio = Entry(
            self.master, textvariable=var_domicilio, background="turquoise"
        )
        e_domicilio.grid(row=3, column=1)

        telefono = Label(self.master, text="Telefono:")
        telefono.grid(row=3, column=2, sticky="w")
        e_telefono = Entry(
            self.master, textvariable=var_telefono, background="turquoise"
        )
        e_telefono.grid(row=3, column=3)

        mail = Label(self.master, text="  Mail:")
        mail.grid(row=4, column=0, sticky="w")
        e_mail = Entry(self.master, textvariable=var_mail, background="turquoise")
        e_mail.grid(row=4, column=1)

        fecha_ing = Label(self.master, text="Fecha Ing. (AAAA-MM-DD):")
        fecha_ing.grid(row=4, column=2, sticky="w")
        e_fecha_ing = Entry(
            self.master, textvariable=var_fecha_ing, background="turquoise"
        )
        e_fecha_ing.grid(row=4, column=3)

        fecha_eg = Label(self.master, text="Fecha Eg. (AAAA-MM-DD):")
        fecha_eg.grid(row=5, column=2, sticky="w")
        e_fecha_eg = Entry(
            self.master, textvariable=var_fecha_eg, background="turquoise"
        )
        e_fecha_eg.grid(row=5, column=3)

        ################################################################
        #   TREEVIEW
        ################################################################

        tree = ttk.Treeview(self.master)
        estilo = ttk.Style()
        estilo.configure("Treeview.Heading", font=("Arial", 8))

        tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6", "col7")
        tree.column("#0", width=80, minwidth=80, anchor=CENTER)
        tree.column("col1", width=80, minwidth=80, anchor=CENTER)
        tree.column("col2", width=80, minwidth=80, anchor=CENTER)
        tree.column("col3", width=80, minwidth=80, anchor=CENTER)
        tree.column("col4", width=80, minwidth=80, anchor=CENTER)
        tree.column("col5", width=80, minwidth=80, anchor=CENTER)
        tree.column("col6", width=80, minwidth=80, anchor=CENTER)
        tree.column("col7", width=80, minwidth=80, anchor=CENTER)

        tree.heading("#0", text="Cod.Res.", anchor=CENTER)
        tree.heading("col1", text="Ap. y Nom.", anchor=CENTER)
        tree.heading("col2", text="Documento", anchor=CENTER)
        tree.heading("col3", text="Domicilio", anchor=CENTER)
        tree.heading("col4", text="Telefono", anchor=CENTER)
        tree.heading("col5", text="Mail", anchor=CENTER)
        tree.heading("col6", text="Fecha Ing", anchor=CENTER)
        tree.heading("col7", text="Fecha Eg", anchor=CENTER)

        tree.grid(padx=15, column=0, row=11, columnspan=40)

        alta = Button(
            self.master,
            text="ALTA",
            command=lambda: self.obj.funcion_a(
                var_ap_y_nom,
                var_documento,
                var_domicilio,
                var_telefono,
                var_mail,
                var_fecha_ing,
                var_fecha_eg,
                tree,
            ),
        )
        alta.grid(row=7, column=0)
        alta.config(bg="#5EFF89")

        baja = Button(
            self.master,
            text="BAJA",
            command=lambda: funcion_vb(),
        )
        baja.grid(row=7, column=1)
        baja.config(bg="#5EFF89")

        ver_reservas = Button(
            self.master, text="VER RESERVAS", command=lambda: self.obj.funcion_v(tree)
        )
        ver_reservas.grid(row=7, column=2)
        ver_reservas.config(bg="#5EFF89")

        borrar_tree = Button(
            self.master, text="REFRESH", command=lambda: self.obj.funcion_bt(tree)
        )
        borrar_tree.grid(row=9, column=2)
        borrar_tree.config(bg="#5EFF89")

        vmodificar = Button(self.master, text="VER MODIF", command=funcion_vm)
        vmodificar.grid(row=7, column=3)
        vmodificar.config(bg="#5EFF89")

        modificar = Button(
            self.master,
            text="MODIFICAR",
            command=lambda: self.obj.funcion_m(
                var_ap_y_nom,
                var_documento,
                var_domicilio,
                var_telefono,
                var_mail,
                var_fecha_ing,
                var_fecha_eg,
                tree,
            ),
        )
        modificar.grid(row=9, column=3)
        modificar.config(bg="#5EFF89")

        salir = Button(self.master, text="SALIR", command=ventana.quit)
        salir.grid(row=7, column=4)
        salir.config(bg="#5EFF89")
