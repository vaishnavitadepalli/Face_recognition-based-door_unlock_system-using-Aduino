#include<Servo.h>
#include <LiquidCrystal.h>
Servo myservo;
const int pin=10;
String a;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
void setup() {
  // put your setup code here, to run once:
  lcd.begin(16, 2);
myservo.attach(pin);
myservo.write(0);
Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
if (Serial.available()>0)
{
   a=Serial.readString();
  if (a.equals("open")){
  myservo.write(90);
  lcd.clear();
    lcd.setCursor(3,0);
    lcd.print("Please Enter");
 }
  else if (a.equals("close")){
   
    lcd.clear();
    
    lcd.setCursor(3,0);
    lcd.print("Access denied");
   }
    else if(a.equals("done")){
    myservo.write(0);
  lcd.clear();
    lcd.setCursor(4,0);
    lcd.print("Welcome");
    lcd.setCursor(3,1);
    lcd.print("Look here");
  
  }
   else if (a.equals("sent")){
    lcd.clear();
    lcd.setCursor(3,0);
    lcd.print("Message sent");
    lcd.setCursor(0,1);
    lcd.print("Please wait");}
}
}
