#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>


Adafruit_PWMServoDriver pwm1 = Adafruit_PWMServoDriver(0x40);
Adafruit_PWMServoDriver pwm2 = Adafruit_PWMServoDriver(0x41);
Adafruit_PWMServoDriver pwm3 = Adafruit_PWMServoDriver(0x42);
// you can also call it with a different address you want
//Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x41);

// Depending on your servo make, the pulse width min and max may vary, you 
// want these to be as small/large as possible without hitting the hard stop
// for max range. You'll have to tweak them as necessary to match the servos you
// have!
#define SERVOMIN  150 // This is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  600 // This is the 'maximum' pulse length count (out of 4096)
#define USMIN  600 // This is the rounded 'minimum' microsecond length based on the minimum pulse of 150
#define USMAX  2400 // This is the rounded 'maximum' microsecond length based on the maximum pulse of 600
#define SERVO_FREQ 50 // Analog servos run at ~50 Hz updates

#define KEYBOARD_WIDTH 38

bool servoArray[38]; //change this to use constants
bool newMSG = true;


int tryParseSerial()
{
  char receivedChar;
  if (Serial.available() > 0) 
  {
    receivedChar = Serial.read();
    newMSG = true;
  }
  else
  {
    return -1;
  }
  
  //next three lines could be done in one line, but is left as is for readability.
  bool onOff = true;
  if(((int)receivedChar)<64)
    onOff = false; // if it is an OFF message
  
  receivedChar = receivedChar & '?'; //mask off front part using question mark's ascii number
  if(0<=(int)receivedChar && (int)receivedChar<38)
    servoArray[receivedChar] = onOff;
  
  return (int)receivedChar;
}

void setServos(Adafruit_PWMServoDriver pwm1, Adafruit_PWMServoDriver pwm2, Adafruit_PWMServoDriver pwm3, int index)
{
  if(0<=index && index < 16)
  {
    if(servoArray[index])
      pwm1.setPWM(index, 0, SERVOMAX);
    else
      pwm1.setPWM(index, 0, SERVOMIN);
  }
  else if(16<=index && index < 32)
  {
    if(servoArray[index])
      pwm2.setPWM(index-16, 0, SERVOMAX);
    else
      pwm2.setPWM(index-16, 0, SERVOMIN);
  }
  else if(32<=index && index < 38)
  {
    if(servoArray[index])
      pwm3.setPWM(index-32, 0, SERVOMAX);
    else
      pwm3.setPWM(index-32, 0, SERVOMIN);
  }
}


void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB
  }
  pwm1.begin();
  // In theory the internal oscillator is 25MHz but it really isn't
  // that precise. You can 'calibrate' by tweaking this number till
  // you get the frequency you're expecting!
  pwm1.setOscillatorFrequency(27000000);  // The int.osc. is closer to 27MHz  
  pwm1.setPWMFreq(SERVO_FREQ);  // Analog servos run at ~50 Hz updates
  // 2
  pwm2.begin();
  pwm2.setOscillatorFrequency(27000000);
  pwm2.setPWMFreq(SERVO_FREQ);
  // 3
  pwm3.begin();
  pwm3.setOscillatorFrequency(27000000);
  pwm3.setPWMFreq(SERVO_FREQ);
  delay(10);

  for(int i=0; i < 38; i++)
  {
    servoArray[i] = false;
    setServos(pwm1, pwm2, pwm3, i);
  }
}

void loop() {
  int index = tryParseSerial();
  if(newMSG)
  {
    setServos(pwm1, pwm2, pwm3, index);
    newMSG = false;
  }
}
