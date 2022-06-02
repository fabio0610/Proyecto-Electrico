from Pro2 import ToExcel

ToExcel=ToExcel("COM3", 9600)

ToExcel.iterations=30
ToExcel.sensor=5
ToExcel.readfromport()

ToExcel.data_sensor.to_excel('Data.xlsx')