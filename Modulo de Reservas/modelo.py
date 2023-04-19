import sqlite3
import re
from exp_reg import ExpReg
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
from observer import Sujeto


def AvisoAlta(funcion):
    """Este es un decorador que se ejecuta cuando se da de alta una reserva por medio
    de la funcion "funcion_a"
    """
        
    def envoltura(*args, **kwargs):
        funcion(*args, **kwargs)
        print("Se acaba de ejecutar la funcion Alta de registro %s" % funcion.__name__)
    return envoltura


def AvisoBaja(funcion):
    """Este es un decorador que se ejecuta cuando se da de baja una reserva 
    por medio de la funcion "funcion_b"
    """
    def envoltura(*args, **kwargs):
        funcion(*args, **kwargs)
        print("Se acaba de ejecutar la funcion Baja de registro %s" % funcion.__name__)
    return envoltura


def AvisoModificar(funcion):
    """Este es un decorador que se ejecuta cuando se modica una reserva por
    medio de la funcion "funcion_m"
    """
    def envoltura(*args, **kwargs):
        funcion(*args, **kwargs)
        print("Se acaba de ejecutar la funcion modificacion de registro %s" % funcion.__name__)
    return envoltura


class Abmc(Sujeto):
    """La Clase Abmc es donde se encuentran las funciones para dar de alta,
    baja, modificacion y consulta de las reservas
    """
    def __init__(
        self,
    ):

        self.validacion = ExpReg()

        try:
            con = sqlite3.connect("reserva.db")
            cursor = con.cursor()
            sql = "CREATE TABLE mitabla(id integer PRIMARY KEY, ap_y_nom text, documento text, domicilio text, telefono text, mail text, fecha_ing date, fecha_eg date)"

            cursor.execute(sql)
            con.commit()

        except:
            pass

    def conexion(
        self,
    ):
        """Con esta funcion se logra la coneccion a la base de datos "reserva.db"
        """
        con = sqlite3.connect("reserva.db")
        return con

    ################################################################
    #   ALTA CON VALIDACION REGEX DEL MAIL
    ################################################################
    
    @AvisoAlta
    def funcion_a(
        self, ap_y_nom, documento, domicilio, telefono, mail, fecha_ing, fecha_eg, tree
    ):
        """Con esta funcion se logra dar de alta una reserva
        """
        verificacion1 = self.validacion.mail(mail.get())
        verificacion2 = self.validacion.fecha_eg(fecha_eg.get())
        verificacion3 = self.validacion.fecha_ing(fecha_ing.get())

        if verificacion1 is True:
            if verificacion2 is True:
                if verificacion3 is True:
                    
                    con = self.conexion()
                    cursor = con.cursor()

                    sql = "INSERT INTO mitabla (ap_y_nom, \
                            documento, domicilio, telefono, mail, \
                            fecha_ing, fecha_eg) VALUES \
                            (?, ?, ?, ?, ?, ?, ?)"

                    datos = (
                        ap_y_nom.get(),
                        documento.get(),
                        domicilio.get(),
                        telefono.get(),
                        mail.get(),
                        fecha_ing.get(),
                        fecha_eg.get(),
                    )
                    self.notificar(ap_y_nom.get(), fecha_ing.get())

                    cursor.execute(sql, datos)
                    con.commit()

                    tree.insert(
                        "",
                        "end",
                        text=(id),
                        values=(
                            ap_y_nom.get(),
                            documento.get(),
                            domicilio.get(),
                            telefono.get(),
                            mail.get(),
                            fecha_ing.get(),
                            fecha_eg.get(),
                        ),
                    )
                    ap_y_nom.set("")
                    documento.set("")
                    domicilio.set("")
                    telefono.set("")
                    mail.set("")
                    fecha_ing.set("")
                    fecha_eg.set("")

                    self.funcion_bt(tree)
                    self.funcion_v(tree)
                   
                    showinfo("", "Reserva ingresada correctamente")
                else:
                    showerror("Fecha de Ingreso no valida", "Ingresela nuevamente")
            else:
                showerror("Fecha de egreso no valida", "Ingresela nuevamente")
        else:
            showerror("Mail no valido", "Ingreselo nuevamente")

        

    ################################################################
    #   BAJA DE LA RESERVA SELECCIONADA
    ################################################################


    @AvisoBaja
    def funcion_b(self, record, tree):
        """Con esta funcion se logra dar de baja una reserva
        """
        con = self.conexion()
        cursor = con.cursor()

        sql = "DELETE FROM mitabla WHERE documento = ?"
        datos = (record[1],)

        cursor.execute(sql, datos)
        con.commit()

        self.funcion_v(tree)

        showinfo("", "Reserva eliminada correctamente")

    ################################################################
    #   MODIFICACION DE LA RESERVA
    ################################################################

    @AvisoModificar
    def funcion_m(self, ap_y_nom, documento, domicilio, telefono, mail, fecha_ing, fecha_eg, tree):
        """Con esta funcion se logra modificar una reserva
        """
        if not tree.selection():
            showerror(
                "No selecciono ninguna reserva", "Seleccione una y vuelvalo a intentar"
            )

        else:
            verificacion1 = self.validacion.mail(mail.get())
            verificacion2 = self.validacion.fecha_eg(fecha_eg.get())
            verificacion3 = self.validacion.fecha_ing(fecha_ing.get())

            if verificacion1 is True:
                if verificacion2 is True:
                    if verificacion3 is True:
          
                        con = self.conexion()
                        cursor = con.cursor()

                        for selected_item in tree.selection():
                            item = tree.item(selected_item)
                            id = item["text"]

                        sql = "UPDATE mitabla SET ap_y_nom=?, \
                                documento=?, domicilio=?, telefono=?, mail=?, \
                                fecha_ing=?, fecha_eg=? \
                                WHERE id = ?"

                        datos = (
                            ap_y_nom.get(),
                            documento.get(),
                            domicilio.get(),
                            telefono.get(),
                            mail.get(),
                            fecha_ing.get(),
                            fecha_eg.get(),
                            id,
                        )

                        cursor.execute(sql, datos)
                        con.commit()

                        ap_y_nom.set("")
                        documento.set("")
                        domicilio.set("")
                        telefono.set("")
                        mail.set("")
                        fecha_ing.set("")
                        fecha_eg.set("")

                        self.funcion_bt(tree)
                        self.funcion_v(tree)

                        showinfo("", "Modificacion efectuada correctamente")
                    else:
                        showerror("Fecha de Ingreso no valida", "Ingresela nuevamente")
                else:
                    showerror("Fecha de egreso no valida", "Ingresela nuevamente")
            else:
                showerror("Mail no valido", "Ingreselo nuevamente")

    ################################################################
    #   VISUALIZACION DE TODAS LAS RESERVAS
    ################################################################

    def funcion_v(self, tree):
        """Con esta funcion se logra visualizar las reservas
        """
        refresh = tree.get_children()
        for x in refresh:
            tree.delete(x)

        con = self.conexion()
        cursor = con.cursor()

        sql = "SELECT * FROM mitabla"

        cursor.execute(sql)

        resultado = cursor.fetchall()

        for x in resultado:
            tree.insert(
                "", "end", text=x[0], values=(x[1], x[2], x[3], x[4], x[5], x[6], x[7])
            )
        con.commit()

    def funcion_bt(self, tree):
        """Con esta funcion se refrescan las reservas
        """
        refresh = tree.get_children()
        for x in refresh:
            tree.delete(x)
