// Robot Orchestra workshop code
// Shrimp version, with pinouts amended for easier construction on
// mini breadboard.
// Drives one, two (or more, potentially) servos in a repeating beat pattern
// Author: Jonathan Sanderson, for Think Physics, Northumbria University
// Version: 1, 2016-02-15

#include <Servo.h>

// Pin setup and generate servo objects
int ledPin = 6;
const byte N_SERVOS = 1; 
const byte servoPin[N_SERVOS] = {9};
Servo servo[N_SERVOS];

// Beat configuration. Edit the arrays to alter the beat/miss pattern.
// Ensure number of beats matches N_BEATS or there'll be an error.
const int N_BEATS = 16;
int beats[N_SERVOS][N_BEATS] = { { 1, 0, 0, 0, 
                                   1, 0, 0, 0,
                                   1, 0, 0, 0, 
                                   1, 0, 0, 0} };

// Define how far the servo moves (same for each servo)
// Fiddling with this is rare, and note that the servo rarely has time to reach angleTwitch
const int angleRest = 0;          // Initial angle of servo
const int angleTwitch = 180;      // Deflection target angle if we're playing a beat
const int angleMiss = 05;         // Deflection target angle if we're playing a miss, not a beat
const int angleTwitchReverse = 0; // Not used in this code version

// Define playback speed in beats per minute, and a tempo (beat duration) from that
const int bpm = 120;
const int tempo = (int) ( 1000 / (bpm/60) ); // milliseconds

void setup() {
  // Initialise the servo objects, and send them to the rest position
  for (int i = 0; i < N_SERVOS; i++) {
    servo[i].attach(servoPin[i]);
    servo[i].write(angleRest);
  }  
  pinMode(ledPin, OUTPUT); // Set up the LED pin
  delay(200);              // Brief pause to give servos time to move to rest
}

void loop() {
  // Loop through the beat array
  for ( int beat = 0 ; beat < N_BEATS ; beat++ ) {

    // Loop through the servos
    for ( int channel = 0 ; channel < N_SERVOS ; channel++ ) {
      if ( beats[channel][beat] == 1 ) {
        twitch(servo[channel], angleTwitch); // Play a hit
      } else {
        twitch(servo[channel], angleMiss);   // Play a miss
      }
    } 
    
    delay(150); // Give the servos time to move

    // Return the servos to rest position
    for ( int channel = 0 ; channel < N_SERVOS ; channel++ ) {
      twitch(servo[channel], angleRest);
    }

    delay(tempo-(200)); // give the servos time to move back, correcting for desired tempo

    // Now flash the LED
    digitalWrite(ledPin, HIGH); // LED ON
    delay(50);                  // Pause so we see flash
    digitalWrite(ledPin, LOW);  // LED OFF
  }
}

// twitch function to handle servo deflection. Dereferences address of servo not-really-object
// ...which is one of those C things that makes little sense. 
// In an earlier version, this function paused and returned the servo to angleRest, but that
// made simultaneous movement of multiple servos impossible. So that aspect was pulled back
// into the main loop. An observer might claim that this function is, therefore, completely pointless.
void twitch(Servo &theServo, int angle) {
  theServo.write(angle); // Move towards chosen angle
}

