import pandas as pd
import serial
from datetime import datetime
data_sensor = pd.DataFrame(columns=['ID', 'Fecha', 'Hora'], index = range(3))

it_is = True
iterations = 0
sensor = 0
while it_is:
    try:
        iterations = input("Escriba la cantidad de mediciones\n")
        iterations = int(iterations)
        it_is = False
    except ValueError:
        print("Esciba un numero entero\n")
        it_is = True
it_is = True
while it_is:
    try:
        sensor = input("Escriba la cantidad de sensores\n")
        sensor = int(sensor)
        it_is = False
    except ValueError:
        print("Esciba un numero entero\n")
        it_is = True

iterations = int(iterations)
sensor = int(sensor)
now = datetime.now()

for index in range(1, iterations):
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    date_time = date_time.split(',')
    data_sensor.at[index, 'ID'] = index
    data_sensor.at[index, 'Fecha'] = date_time[0]
    data_sensor.at[index, 'Hora'] = date_time[1]
    for number in range(sensor):
        label = "Sensor_"+str(number)
        data_sensor.at[index, label] = datos[number]

data_sensor.to_excel('Data.xlsx')