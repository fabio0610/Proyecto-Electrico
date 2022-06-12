from Pro2 import ToExcel

ToExcel=ToExcel("COM3", 9600)

ToExcel.iterations=5
ToExcel.sensor=7
ToExcel.readfromport()


ToExcel.data_sensor.to_excel('Data.xlsx')