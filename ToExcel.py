import pandas as pd
import serial
from time import sleep
from datetime import datetime


class ToExcel:
    def __init__(self,port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.data_sensor = pd.DataFrame(columns=['ID', 'Fecha', 'Hora'])
        self.number = 1000
        self.iterations=0
        self.sensor=0
        self.index=0
        self.delay = 2



    def readfromport(self):
        ser = serial.Serial(self.port, self.baudrate, timeout=1)

        for index in range(self.iterations):
            sleep(self.delay)
            now = datetime.now()
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            date_time = date_time.split(',')
            line = str(ser.readline())
            line.find(",")
            info = line.split(",")
            self.data_sensor.at[index, 'ID'] = index+1
            self.data_sensor.at[index, 'Fecha'] = date_time[0]
            self.data_sensor.at[index, 'Hora'] = date_time[1]
            for number in range(self.sensor):
                label = "Sensor_"+str(number+1)
                self.data_sensor.at[index, label] = info[number].replace("b'",'').replace("\\r\\n'",'')