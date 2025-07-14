// Arduino Buzzer Control via Serial
const int buzzerPin = 8;
void setup() {
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);
}
void loop() {
  if (Serial.available() > 0) {
    char signal = Serial.read();
    if (signal == '1') {
      digitalWrite(buzzerPin, HIGH);
      delay(3000); // Buzzer on for 3 seconds
      digitalWrite(buzzerPin, LOW);
    }
  }
}
