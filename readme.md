# Robot Orchestra

This code is pre-flashed onto [Arduino](https://www.arduino.cc) or [Huzzah](https://www.adafruit.com/product/2471) microcontrollers used in [Think Physics](http://thinkphysics.org)' 'Robot Orchestra' workshop and drop-in session. Participants build a simple blink circuit to learn their way around breadboard, then add a servo – which immediately starts twitching with a regular beat pattern. They then use glue, masking tape, cardboard, chopsticks, and other craft materials to mount their servo so it 'plays' (ie. hits) a musical instrument. Over the course of the workshop, a 'robotic orchestra' of variously ridiculous contraptions is assembled by participants as a collective endeavour.

Extensions include editing the code and reflashing the Arduino to amend the beat pattern, and introducing a second servo per Arduino. A more advanced version of the orchestra uses wifi-enabled Huzzah- or Wemos D1 mini-based robots, an [MQTT](http://mqtt.org) broker for networked message-passing, and a Python script to distribute beat patterns to individual robots and cue playback.

The resulting working is chaotic, noisy, collaborative, whimsical, and features participants contributing towards a shared goal.

## Versions

**June 2017**: Extension to feature live control of Wemos D1 mini-driven robots from a (Raspberry Pi-connected) [Adafruit HELLA UNTZtrument](https://www.adafruit.com/product/1999). Each robot has a 3-bit input to specify which UNTZtrument channel to follow, which is read during the loop and hence can be amended during run.

Future plans include building a browser-based analogue of the UNTZtrument so multiple users can define beat sequences for the orchestra and take turns to play back their composition.

**February 2017**: minor tweaks and changes in preparation for a bigger overhaul shortly.

**November 2016**: more new features! Thanks to @Auraxis012, the Python controller for the wireless version of the Orchestra now handles input files, which read rather like punched cards, and the Python controller can be used to patch specific beat sequences to groups of robots.

There's also a simple test script, which makes debugging wifi robots easier during assembly.

**October 2016**: we've checked in a whole new tree, which targets [Adafruit Huzzah](https://learn.adafruit.com/adafruit-huzzah-esp8266-breakout/overview) as the robot instrument microcontrollers. The robots connect to a wifi network, and through that to an MQTT server (typically [Mosquitto](https://mosquitto.org) running on a Mac or Raspberry Pi). The server is then scripted via the included Python code to issue beat patterns and playback cues to the connected robot instruments.

The other directories are effectively version 2 of the code, with stubs/loops for handling more than two servos per Arduino. This is more complex than prior versions, but the added flexibility extends the workshop for more able students.

For drop-in, family and primary school sessions we expect to continue with the Arduino-based v2 code. Our next objective is to test the Huzzah robots and codebase to see how successful the Python programming exercise is for secondary workshops.

### Past version history -- changes from 1.0 to 2.0

* Beats per minute / tempo calculations actually do what they're supposed to, rather than leading to negative delays. Which don't work so well, funnily enough.
* Servo twitch code is now rolled into the main loop rather than incorporated in the helper function. While we liked the neatness of the latter, it made synchronised movement of two servos impossible to wrap our heads around. This does render the helper function more-or-less pointless, but I'm too proud of the object dereferencing to delete it just yet.
* In principle, extending the code to handle >2 servos should be very straightforward.
* Main loop is much cleaner.

## Notes

Since we want a beat and 'no beat' (a 'miss') to take the same amount of time, each servo is called to move on each possible beat. What changes is the deflection angle requested. This appears to work well.

TODO: Upload Fritzing diagrams used in workshop  
TODO: Provide some example results!

## Next steps

* Looping of playback for wifi robots. This could be done at the Python end (by calculating beat sequence playback time, which may be prone to error), or within the Huzzah code (which presents challenges for updating the sequence while staying in sync). The objective is to be able to live-update the beat sequences during playback.
* Port to WeMos D1 mini boards
* 'Patch board' functionality to assign individual robots to groups/tracks. This already exists as named lists in the Python code (eg. `DRUMS`), but group/track assignment could be broken out into a language grammar like the sequence script.
* Interface for patch board - assign robots to groups interactively.
* Sequencing controller, based on the [UNTZtroment](https://www.adafruit.com/product/1999).
* Playback start/stop button controls, via GPIOZero on controlling Pi.

## Credits

Workshop and code by Jonathan Sanderson, Northumbria University, 2015-16, with contributions by @Auraxis012. Based on an idea I first saw at [Maker Faire UK](http://www.makerfaireuk.com) in about 2011, by Alistair MacDonald ([@alistair](https://twitter.com/alistair)).

Funding to support this aspect of Think Physics came from the [Reece Foundation](http://www.reece-foundation.org "Reece Foundation | Supporting engineering in the region").
