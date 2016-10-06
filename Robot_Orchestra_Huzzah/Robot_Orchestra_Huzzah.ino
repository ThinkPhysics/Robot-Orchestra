// Robot Orchestra workshop code – for Adafruit Huzzah network-enabled devices
// 
// This version pulls Adafruit Huzzah and MQTT code from the Wishing Well repo,
// to produce a network-aware robot orchestra which receives beat patterns from
// a central MQTT server.

// Author: Jonathan Sanderson, for Think Physics, Northumbria University
// Version: 2016-09-27 First working version

#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <Servo.h>

const char* ssid = "thinkphysics";
const char* password = "thinkphysics1";
// Stick the IP address of the MQTT server in the line below.
// Find it by entering `ifconfig` at a Terminal prompt, and looking for
// the wlan0 ipv4 address.
const char* mqtt_server = "10.0.1.4";

// Each robot has a unique name, generated from the hardware MAC address.
// These variables will store those names.
String huzzahMACAddress;
String skutterNameString;
char skutterNameArray[60];

// String variables in which to store the received messages
String subsTargetString;
char subsTargetArray[60];

// Is this Skutter robot currently selected as active, or not?
bool active = false;

// Variables for the wifi and MQTT clients
WiFiClient espClient;
PubSubClient client(espClient);

// Pin definitions
#define PIN_SERVO 12

Servo myservo;


// Number of beats in sequence (two bytes, so we'll run out of string storage first)
unsigned int nbeats = 16;
// Storage for beats array, to be stepped through
String beatsString;

// Define how far the servo moves
// Fiddling with this is rare, and note that the servo rarely has time to reach angleTwitch
const int angleRest = 0;          // Initial angle of servo
const int angleTwitch = 180;      // Deflection target angle if we're playing a beat
const int angleMiss = 05;         // Deflection target angle if we're playing a miss, not a beat
const int angleTwitchReverse = 0; // Not used in this code version

// Define playback speed in beats per minute, and a tempo (beat duration) from that
// Note that fast tempos give less time for the servo to move, so may lead to weak hits.
const int bpm = 120;
const int tempo = (int) ( 1000 / (bpm/60) ); // milliseconds

void setup() {
    // Setup code, runs once only:
    Serial.begin(115200);
    setup_wifi();
    
    // Set up on-board LEDs for diagnostics
    pinMode(00, OUTPUT);
    pinMode(02, OUTPUT);

    // Get this Huzzah's MAC address and use it to register with the MQTT server
    huzzahMACAddress = WiFi.macAddress();
    skutterNameString = "skutter_" + huzzahMACAddress;
    Serial.println(skutterNameString);
    skutterNameString.toCharArray(skutterNameArray, 60);
    subsTargetString = "orchestra/" + skutterNameString;
    subsTargetString.toCharArray(subsTargetArray, 60);
    for (int i = 0; i < 60; i++) {
        Serial.print(subsTargetArray[i]);
    }
    Serial.println();

    client.setServer(mqtt_server, 1883);
    client.setCallback(callback);

    myservo.attach(PIN_SERVO);
    myservo.write(angleRest); // Set to zero speed so there's no servo kick on boot. Doesn't work.

}

void loop() {
    // Call the MQTT client to poll for updates, reconnecting if necessary
    // Handle messages via the callback function
    if (!client.connected()) {
        reconnect();
    }
    client.loop();
}


// CALLBACK function; parses received messages and acts upon them.
void callback(char* topic, byte* payload, unsigned int length) {

    // Convert topic and message to C++ String types, for ease of handling

    // message length gives us the length of the payload
    String payloadString;
    for (int i = 0; i < length; i++) {
        payloadString += String((char)payload[i]);
    }

    // for the topic, we need to call strlen to find the length
    String topicString;
    for (int i = 0; i < strlen(topic); i++) {
        topicString += String((char)topic[i]);
    }

    // Debug: print the (processed) received message to serial
    Serial.print(F("Message arrived ["));
    Serial.print(topicString);
    Serial.print(F("] "));
    Serial.println(payloadString);

    // Now handle the possible messages, matching on topic

    /* TARGET CHANGED ********************************************/
    if (topicString == subsTargetString) {
        Serial.println(F("Skutter target signal"));
        // Check to see if this Skutter is disabled, else enable
        if (payloadString == "0") {
            active = false;
            Serial.println(F("This Skutter is now inactive"));
        } else {
            active = true;
            Serial.println(F("This Skutter is now ACTIVE!"));
        }
    }

     /* HANDLE TWITCH *******************************************/
    // This is mostly for testing purposes, but does allow entirely
    // server-driven playback rather than transferring beat patterns
    // and triggering playback in sync.
    if ( (topicString == "orchestra/twitch") && active ) {
        if ( payloadString == "1" ) {
            Serial.println(F("BONG!"));
            twitch(myservo, angleTwitch);
        } else if ( payloadString == "0" ) {
            twitch(myservo, angleMiss);
            Serial.println(F("pish!"));
        }
        delay(150); // Give the servo time to move
        // Return the servo to rest position
        twitch(myservo, angleRest);        
    }

    /* HANDLE RECEIVED BEAT SEQUENCE ****************************/
    if ( (topicString == "orchestra/beats") && active ) {
        // Store received beat pattern in global String
        beatsString = payloadString;
        nbeats = payloadString.length();
        Serial.print("Sequence length received: ");
        Serial.println(nbeats);
    }

    /* HANDLE PLAYBACK CUE **************************************/
    // trigger playback of stored beat pattern.
    if ( (topicString == "orchestra/play") && active ) {
        // Confirm the beat pattern we're going to play
        Serial.print("Playing pattern: ");
        Serial.println(beatsString);
        // Loop through the beat array
        for ( int beat = 0 ; beat < nbeats ; beat++ ) {
            // Get the individual beat (NB. neat to cast to String, since .charAt returns char
            String thisBeat = String(beatsString.charAt(beat));
            // Print the beat index and value      
            Serial.print(beat);
            Serial.print(":");
            Serial.print(thisBeat);
            if ( thisBeat == "1" ) {
                digitalWrite(02, HIGH);
                twitch(myservo, angleTwitch); // Play a hit
                Serial.println(F(" BONG!"));
            } else {
                digitalWrite(02, HIGH);
                twitch(myservo, angleMiss);  // Play a miss
                Serial.println(F(" pish!"));
            }
            delay(150); // Give the servos time to move
            digitalWrite(02, LOW);
            // Return the servos to rest position
            twitch(myservo, angleRest);
            delay(tempo-(200)); // give the servos time to move back, correcting for desired tempo
        } 
    
    
  }

}


void twitch(Servo &theServo, int angle) {
    theServo.write(angle); // Move towards chosen angle
}
