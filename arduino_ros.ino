
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

// the loop function runs over and over again forever
char incomingByte = 0;
void loop() {
  if (Serial.available() > 0) {

    incomingByte = Serial.read(); // read the incoming byte:
    if(incomingByte=='s'){
      digitalWrite(13, HIGH);
    }
    else if(incomingByte=='f'){
      digitalWrite(13, LOW);
    }
    else if(incomingByte=='b'){
      digitalWrite(13, HIGH);
    }
    else if(incomingByte=='r'){
      digitalWrite(13, LOW);
    }
    else if(incomingByte=='l'){
      digitalWrite(13, HIGH);
    }
  }
}