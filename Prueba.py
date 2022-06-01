from Proyecto import ToExcel

ToExcel = ToExcel("COM3",9600)

columnas = ["Nro Lectura","Valor"]

ToExcel.addColumns(["Nro Lectura","Valor"])
ToExcel.addData(10)
ToExcel.readFromPort()

ToExcel.writeFile("archivo1.xls")