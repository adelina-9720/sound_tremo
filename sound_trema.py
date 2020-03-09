const uint8_t  pinSensor   = A0;                     
const uint16_t varVolume   = 10;                     
const uint16_t varDuration = 2000;                    
const uint8_t  pinLED[3]  = {9, 6, 3};                
const uint8_t  varLED[3]  = {2, 3, 4};               
bool           flgLED[3]  = {0, 0, 0};              
uint8_t        varSum;                               
uint32_t       varTimeOut;                            
void setup() {
  for (uint8_t i = 0; i < sizeof(pinLED); i++) {      
    pinMode      (pinLED[i], OUTPUT);                 
    digitalWrite (pinLED[i], flgLED[i]);              
}
void loop() {
 
  if (analogRead(pinSensor) > varVolume) {            
    varSum = 0;                                       
    varTimeOut = millis() + varDuration;              
    while (varTimeOut > millis()) {                  
      if (analogRead(pinSensor) > varVolume) {        
        while (analogRead(pinSensor) > varVolume) {   
          delay(50);                                  
        }
        varSum++;                                    
        delay(50);                                    
      }
    }
    
    for (uint8_t i = 0; i < sizeof(varLED); i++) {    
      if (varSum == varLED[i]) {                      
        flgLED[i] = ! flgLED[i];                      
        digitalWrite(pinLED[i], flgLED[i]);           
      }
    }
  }
}
