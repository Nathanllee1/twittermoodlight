int redPin = 11;
int greenPin = 10;
int bluePin = 9;


void setup() {
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
    if (Serial.available()) {
        char serialListener = Serial.read();

        if (serialListener == 's') {
            analogWrite(redPin, red);
        }
        else if (serialListener == 'h') {
            digitalWrite(LED, LOW);
        }
    }
}
