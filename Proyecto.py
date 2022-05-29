# Se importan las librerias a utilizar
import serial
import xlwt

# se declara la clase que permitirá
class ToExcel:
    # se declara la función init que permite la creación del archivo Excel
    def __int__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate


        self.wb = xlwt.Workbook()
        self.ws = self.wb.add_sheet("Datos del Arduino", cell_overwrite_ok=True)
        self.ws.write(0, 0, "Datos del Arduino")
        self.columns = ["Sensor"]
        self.number = 1000

    #Función encargada de argregar las columnas extras necesarias además de la principal
    def addColumns(self, col):
        self.columns.extend(col)

    #Función encargada de recibir el número de datos que desean recibirse
    def addData(self, number):
        self.number = number

