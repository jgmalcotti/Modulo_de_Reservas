import re
from datetime import datetime


class ExpReg:
    """El modulo exp_reg es para verificar
    el correcto ingreso de datos
    """
    
    def mail(self, val_mail):
        """El metodo "mail" es para verificar 
        el correcto formato del mismo
        """
        patron = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        resultado = True    
        if re.match(patron, val_mail):
            resultado = True

        else:
            resultado = False
        return resultado

    def fecha_eg(self, fecha):
        """Los metodos "fecha_eg" y "fecha_ing" son para verificar 
        el correcto formato de las fechas de reserva
        """
        try:
            datetime.strptime(fecha, '%Y-%m-%d')
            resultado = True
        except:
            resultado = False

        return resultado

    def fecha_ing(self, fecha):
        try:
            datetime.strptime(fecha, '%Y-%m-%d')
            resultado = True
        except:
            resultado = False

        return resultado
    