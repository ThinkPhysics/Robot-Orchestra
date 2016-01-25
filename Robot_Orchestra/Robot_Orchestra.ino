#include <Servo.h>

// ServoTwitch v0.3 20/7/2015 Jonathan Sanderson / Think Physics / Northumbria University

// Start by setting up the servo and pinouts
Servo myServo1;
int servoPin1 = 9;  // Servo1 will be on pin 9

Servo myServo2;
int servoPin2 = 10; // Servo2 will be on pin 10

int ledPin1 = 3;    // LED is on pin 3

// Now to define the beat sequence
const int noBeats = 16; // Number of beats in measure
int beats1[noBeats] = {1, 0,0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0};
int beats2[noBeats] = {1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,};

// Define how far the servo moves (same for each servo)
const int angleRest = 0;          // Initial angle of servo
const int angleTwitch = 180;      // Deflection target angle if we're playing a beat
const int angleMiss = 05;         // Deflection target angle if we're playing a miss, not a beat
const int angleTwitchReverse = 0; // Not used

// Precalculate some playback speed stuff
float bpm = 160.0;  // Used to calculate delays. Can speed up playback by increasing, but
                    // servo may not have time to reach chosen deflection if >~120
int tempo = (int) ( (60 / bpm) * 1000 ); // cast result to integer


void setup() {
  myServo1.attach(servoPin1); // Attach servo
  myServo2.attach(servoPin2); // Attach servo2 
  pinMode(ledPin1, OUTPUT);   // Set LED output
  myServo1.write(angleRest);  // Set servo to neutral position
  myServo2.write(angleRest);  // Set servo to neutral position
  delay(200);                 // Wait for servo to reach neutral
}

void loop() {
  // Main loop is really nasty now, with nested if/else to handle both servos. There
  // are many better ways of doing this, doubtless.
  for ( int i = 0; i < noBeats ; i++) {
    if (beats1[i] == 1) {
      twitch(myServo1, angleTwitch);
      if (beats2[i] == 1) {
        twitch(myServo2, angleTwitch);
      } else {
        twitch(myServo2, angleMiss);
      }
    } else {
      twitch(myServo1, angleMiss);    // if we're not playing a beat, play a miss so code paths take same time
      if (beats2[i] == 1) {
        twitch(myServo2, angleTwitch);
      } else {
        twitch(myServo2, angleMiss);
      }
    }
    digitalWrite(ledPin1, HIGH);  // Flash LED
    delay(50);                    // ...briefly
    digitalWrite(ledPin1, HIGH);   // LED on
  }
}

// twitch function to handle servo deflection. Dereferences address of servo not-really-object
// ...which is one of those C things that makes little sense. Just leave the &theServo as it is,
// it works.
void twitch(Servo &theServo, int angle) {
  theServo.write(angle);      // Move towards chosen angle
  delay(100);
  theServo.write(angleRest);  // Return to rest position
  delay(tempo - 150); //trying to fudge to make up for the servo call time/delay
}
