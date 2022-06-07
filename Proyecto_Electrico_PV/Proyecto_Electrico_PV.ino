



// Librerías

#include <OneWire.h>
#include <DallasTemperature.h>



//Pines
const byte Sdat = A0;


//Constantes
int dt = 100;


//Objetos
OneWire oneWireObjetoOne(Sdat);
DallasTemperature sensorDS18B20(&oneWireObjetoOne);


void setup() {

Serial.begin(9600);
sensorDS18B20.begin();
}

void loop() {
sensorDS18B20.requestTemperatures();

/////////////////////////---Sensor 1////////////////////////////////////////////////////
   if (sensorDS18B20.getTempCByIndex(0) == -127.00){
    Serial.print("Error sensor 1");
   } else{
    Serial.print(sensorDS18B20.getTempCByIndex(0));
   }
   
   Serial.print(',');
   
/////////////////////////---Sensor 2////////////////////////////////////////////////////
   
   if (sensorDS18B20.getTempCByIndex(1) == -127.00){
    Serial.print("Error sensor 2");
   } else{
    Serial.print(sensorDS18B20.getTempCByIndex(1));
   }
   
   Serial.print(',');

/////////////////////////---Sensor 3////////////////////////////////////////////////////
   
   if (sensorDS18B20.getTempCByIndex(2) == -127.00){
    Serial.print("Error sensor 3");
   } else{
    Serial.print(sensorDS18B20.getTempCByIndex(2));
   }

   Serial.print(',');

/////////////////////////---Sensor 4////////////////////////////////////////////////////
   
   if (sensorDS18B20.getTempCByIndex(3) == -127.00){
    Serial.print("Error sensor 4");
   } else{
    Serial.print(sensorDS18B20.getTempCByIndex(3));
   }
   
   Serial.print(',');

/////////////////////////---Sensor 5////////////////////////////////////////////////////
   
   if (sensorDS18B20.getTempCByIndex(4) == -127.00){
    Serial.print("Error sensor 5");
   } else{
    Serial.print(sensorDS18B20.getTempCByIndex(4));
   }
  
   Serial.print(',');


/////////////////////////---Sensor 6////////////////////////////////////////////////////   
   if (sensorDS18B20.getTempCByIndex(5) == -127.00){
    Serial.print("Error sensor 6");
   } else{
    Serial.print(sensorDS18B20.getTempCByIndex(5));
   }
  
   Serial.print(',');

/////////////////////////---Sensor 7////////////////////////////////////////////////////
   
   if (sensorDS18B20.getTempCByIndex(6) == -127.00){
    Serial.println("Error sensor 7");
   } else{
    Serial.println(sensorDS18B20.getTempCByIndex(6));
   }


delay(dt);




}
