int buzzerPin = 8;
int ledPin = 12;
int mq5Pin = A0;

int gasThreshold = 800;

void setup() {
  pinMode(buzzerPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int gasLevel = analogRead(mq5Pin);
  Serial.print("Gas level: ");
  Serial.println(gasLevel);

  if (gasLevel < gasThreshold) {
    digitalWrite(buzzerPin, HIGH);
    digitalWrite(ledPin, LOW);
  } 
  else {
    digitalWrite(buzzerPin, LOW);
    digitalWrite(ledPin, HIGH);
  }

  delay(500);
}



