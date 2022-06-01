# Se importan las librerias a utilizar
import serial
import xlwt

# se declara la clase que permitirá


class ToExcel:
    # se declara la función init que permite la creación del archivo Excel
    def __init__(self, port, baudrate):
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

    #Función encargada de leer los datos del puerto serial
    def readFromPort(self):
        ser = serial.Serial(self.port, self.baudrate, timeout=1)
        c = 0
        cont = 0
        for col in self.columns:
            self.ws.write(1, c, col)
            c = c + 1
        self.fila = 2

        i = 0
        while (i < self.number):
            line = str(ser.readline())
            if (len(line) > 0):

                cont = cont + 1
                if (line.find(",")):
                    c = 1
                    self.ws.write(self.fila, 0, cont)
                    columnas = line.split(",")
                    for col in columnas:
                        self.ws.write(self.fila, c, col)
                        c = c + 1

                i = i + 1
                self.fila = self.fila + 1

    def writeFile(self, archivo):
        self.wb.save(archivo)