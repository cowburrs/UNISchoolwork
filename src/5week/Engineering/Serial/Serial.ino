// this constant won't change. It's the pin number of the sensor's output:
const int trigPin = 11;
const int echoPin = 6;
const int ledPin = 3;
float printLong = 0;
float previcm = 0;

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.println("Begin");
}

void loop() {
  // establish variables for duration of the ping, and the distance result
  // in inches and centimeters:
  float length;

  // The PING))) is triggered by a HIGH pulse of 2 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // The same pin is used to read the signal from the PING))): a HIGH pulse
  // whose duration is the time (in microseconds) from the sending of the ping
  // to the reception of its echo off of an object.
  length = microsecondsToCentimeters(pulseIn(echoPin, HIGH));

  // convert the time into a distance
  printLong = length/5+printLong*4/5;
  //Serial.println(round(printLong));
  Serial.println((printLong));

  analogWrite(ledPin, printLong*10);
  delay(100);
}

float microsecondsToCentimeters(float microseconds) {
  // The speed of sound is 340 m/s or 29 microseconds per centimeter.
  // The ping travels out and back, so to find the distance of the object we
  // take half of the distance travelled.
  return microseconds / 29 / 2;
}

