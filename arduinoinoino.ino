#include <Wire.h>

void requestEvents () {
// a função: <analogRead(analog_pin)> realiza leitura do pino analogico que se deseja receber
// dados
  int n = analogRead(A0);
  Wire.write(highByte(n));
  Wire.write(lowByte(n));
// <Wire.write(highByte(n)); > e <;> são funções usadas na chamada da
// função de envio de bytes pelo I2C por highByte e lowByte
}

void setup () {
// o parâmetro <Serial.begin(9600)> define a taxa de comunicação serial - 9600 bits por segundo,
// no caso
  Serial.begin(9600);
  Wire.onRequest(requestEvents);
  
//a função < Wire.onRequest(requestEvents)> é chamada quando o Arduino receber solicitações
//da Rasp
}



void loop() {
  delay(100);
}
