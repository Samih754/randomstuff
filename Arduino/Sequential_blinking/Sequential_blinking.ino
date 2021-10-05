int LED1 = 13;
int LED2 = 12;
int LED3 = 11;


void setup() {
  // put your setup code here, to run once:
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(LED1, HIGH); // turn on led
delay(200); //wait 200ms
digitalWrite(LED2, HIGH); // turn on led
delay(200); //wait 200ms
digitalWrite(LED3, HIGH); // turn on led
delay(200); //wait 200ms
digitalWrite(LED1, LOW); // turn off LED
delay(300); // wait 300ms
digitalWrite(LED2, LOW); // turn off LED
delay(300); // wait 300ms
digitalWrite(LED3, LOW); // turn off LED
delay(300); // wait 300ms


}
