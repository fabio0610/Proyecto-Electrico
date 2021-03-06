# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OrderData.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from ToExcel import ToExcel

class Ui_Data(object):
    def setupUi(self, Data):
        Data.setObjectName("Data")
        Data.resize(375, 183)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Data.setPalette(palette)
        self.ExcelButton = QtWidgets.QRadioButton(Data)
        self.ExcelButton.setGeometry(QtCore.QRect(290, 80, 82, 17))
        self.ExcelButton.setObjectName("ExcelButton")
        self.CSVButton = QtWidgets.QRadioButton(Data)
        self.CSVButton.setGeometry(QtCore.QRect(290, 100, 82, 17))
        self.CSVButton.setObjectName("CSVButton")
        self.Mediciones = QtWidgets.QLabel(Data)
        self.Mediciones.setGeometry(QtCore.QRect(10, 10, 111, 21))
        self.Mediciones.setObjectName("Mediciones")
        self.sensores = QtWidgets.QLabel(Data)
        self.sensores.setGeometry(QtCore.QRect(10, 60, 101, 16))
        self.sensores.setObjectName("sensores")
        self.Puerto = QtWidgets.QLabel(Data)
        self.Puerto.setGeometry(QtCore.QRect(160, 10, 41, 20))
        self.Puerto.setObjectName("Puerto")
        self.Velocidad = QtWidgets.QLabel(Data)
        self.Velocidad.setGeometry(QtCore.QRect(150, 60, 51, 20))
        self.Velocidad.setObjectName("Velocidad")
        self.VelocidadBox = QtWidgets.QComboBox(Data)
        self.VelocidadBox.setGeometry(QtCore.QRect(140, 80, 71, 21))
        self.VelocidadBox.setObjectName("VelocidadBox")
        self.VelocidadBox.addItem("")
        self.VelocidadBox.addItem("")
        self.VelocidadBox.addItem("")
        self.VelocidadBox.addItem("")
        self.VelocidadBox.addItem("")
        self.VelocidadBox.addItem("")
        self.VelocidadBox.addItem("")
        self.PuertoBox = QtWidgets.QComboBox(Data)
        self.PuertoBox.setGeometry(QtCore.QRect(140, 30, 71, 22))
        self.PuertoBox.setObjectName("PuertoBox")
        self.PuertoBox.addItem("")
        self.PuertoBox.addItem("")
        self.PuertoBox.addItem("")
        self.PuertoBox.addItem("")
        self.PuertoBox.addItem("")
        self.PuertoBox.addItem("")
        self.PuertoBox.addItem("")
        self.PuertoBox.addItem("")
        self.PuertoBox.addItem("")
        self.PuertoBox.addItem("")
        self.Archivo = QtWidgets.QLabel(Data)
        self.Archivo.setGeometry(QtCore.QRect(280, 60, 81, 20))
        self.Archivo.setObjectName("Archivo")
        self.MedicionestEdit = QtWidgets.QPlainTextEdit(Data)
        self.MedicionestEdit.setGeometry(QtCore.QRect(40, 30, 41, 31))
        self.MedicionestEdit.setObjectName("MedicionestEdit")
        self.SensoresEdit = QtWidgets.QPlainTextEdit(Data)
        self.SensoresEdit.setGeometry(QtCore.QRect(40, 80, 41, 31))
        self.SensoresEdit.setObjectName("SensoresEdit")
        self.Generate = QtWidgets.QPushButton(Data)
        self.Generate.setGeometry(QtCore.QRect(150, 150, 75, 23))
        self.Generate.setObjectName("Generate")
        self.listo = QtWidgets.QLabel(Data)
        self.listo.setGeometry(QtCore.QRect(120, 120, 181, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.listo.setPalette(palette)
        self.listo.setText("")
        self.listo.setObjectName("listo")
        self.NombreEdit = QtWidgets.QPlainTextEdit(Data)
        self.NombreEdit.setGeometry(QtCore.QRect(280, 30, 81, 31))
        self.NombreEdit.setObjectName("NombreEdit")
        self.Nombre = QtWidgets.QLabel(Data)
        self.Nombre.setGeometry(QtCore.QRect(280, 10, 91, 20))
        self.Nombre.setObjectName("Nombre")
        self.NombreArchivo="Data"
        self.Generate.clicked.connect(self.ejecucion)
        self.retranslateUi(Data)
        QtCore.QMetaObject.connectSlotsByName(Data)

    def retranslateUi(self, Data):
        _translate = QtCore.QCoreApplication.translate
        Data.setWindowTitle(_translate("Data", "Data Generator"))
        self.ExcelButton.setText(_translate("Data", "Tipo Excel "))
        self.CSVButton.setText(_translate("Data", "Tipo CSV"))
        self.Mediciones.setText(_translate("Data", "Cant. de mediciones"))
        self.sensores.setText(_translate("Data", "Cant. de sensores"))
        self.Puerto.setText(_translate("Data", "Puerto"))
        self.Velocidad.setText(_translate("Data", "Velocidad"))
        self.VelocidadBox.setItemText(0, _translate("Data", "9600"))
        self.VelocidadBox.setItemText(1, _translate("Data", "1200"))
        self.VelocidadBox.setItemText(2, _translate("Data", "2400"))
        self.VelocidadBox.setItemText(3, _translate("Data", "4800"))
        self.VelocidadBox.setItemText(4, _translate("Data", "19200"))
        self.VelocidadBox.setItemText(5, _translate("Data", "38400"))
        self.VelocidadBox.setItemText(6, _translate("Data", "115200"))
        self.PuertoBox.setItemText(0, _translate("Data", "COM1"))
        self.PuertoBox.setItemText(1, _translate("Data", "COM2"))
        self.PuertoBox.setItemText(2, _translate("Data", "COM3"))
        self.PuertoBox.setItemText(3, _translate("Data", "COM4"))
        self.PuertoBox.setItemText(4, _translate("Data", "COM5"))
        self.PuertoBox.setItemText(5, _translate("Data", "COM6"))
        self.PuertoBox.setItemText(6, _translate("Data", "COM7"))
        self.PuertoBox.setItemText(7, _translate("Data", "COM8"))
        self.PuertoBox.setItemText(8, _translate("Data", "COM9"))
        self.PuertoBox.setItemText(9, _translate("Data", "COM10"))
        self.Archivo.setText(_translate("Data", "Tipo de Archivo"))
        self.Generate.setText(_translate("Data", "Generate"))
        self.Nombre.setText(_translate("Data", "Nombre de archivo"))

    def ejecucion(self):
        self.ToExcel = ToExcel(str(self.PuertoBox.currentText()), int(self.VelocidadBox.currentText()))
        self.ToExcel.iterations = int(self.MedicionestEdit.toPlainText())
        self.ToExcel.sensor = int(self.SensoresEdit.toPlainText())
        self.ToExcel.readfromport()
        self.NombreArchivo=str(self.NombreEdit.toPlainText())
        if (self.ExcelButton.isChecked()):
            self.ToExcel.data_sensor.to_excel(self.NombreArchivo +'.xlsx')
            self.listo.setText("Archivo de Excel generado")
        elif (self.CSVButton.isChecked()):
            self.ToExcel.data_sensor.to_csv(self.NombreArchivo +'.csv')
            self.listo.setText("Archivo CSV generado")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Data = QtWidgets.QDialog()
    ui = Ui_Data()
    ui.setupUi(Data)
    Data.show()
    sys.exit(app.exec_())
