const int trigpin=5;
const int echopin=7;

long duration;
int distance;

void setup() {
  // put your setup code here, to run once:
pinMode(trigpin, OUTPUT);
pinMode(echopin,INPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(trigpin, LOW);
delayMicroseconds(30);

digitalWrite(trigpin,HIGH);
delayMicroseconds(10);
digitalWrite(trigpin, LOW);

duration =pulseIn(echopin,HIGH);
distance=duration*0.034/2;

//Serial.print("Distance: ");
Serial.println(distance);
delay(10000);
}
