import pandas as pd
import serial
from datetime import datetime


class ToExcel:
    def __init__(self,port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.data_sensor = pd.DataFrame(columns=['ID', 'Fecha', 'Hora'], index=range(3))
        self.number = 1000
        self.iterations=0
        self.sensor=0


    now = datetime.now()
    def readfromport(self):
        ser = serial.Serial(self.port, self.baudrate, timeout=1)

        for index in range(1,self.iterations):
            date_time = self.now.strftime("%m/%d/%Y, %H:%M:%S")
            date_time = date_time.split(',')
            line = str(ser.readline())
            line.find(",")
            info = line.split(",")
            self.data_sensor.at[index, 'ID'] = index
            self.data_sensor.at[index, 'Fecha'] = date_time[0]
            self.data_sensor.at[index, 'Hora'] = date_time[1]
            for number in range(self.sensor):
                label = "Sensor_"+str(number)
                self.data_sensor.at[index, label] = info[number]

