# Robot Orchestra

This code is pre-flashed onto Arduinos used in [Think Physics](http://thinkphysics.org)' 'Robot Orchestra' workshop and drop-in session. Participants build a simple blink circuit to learn their way around breadboard, then add a servo – which immediately starts twitching with a regular beat pattern. They then use glue, masking tape, cardboard, chopsticks, and other craft materials to mount their servo so it 'plays' (ie. hits) a musical instrument. Over the course of the workshop, a 'robotic orchestra' of variously ridiculous contraptions is assembled by participants as a collective endeavour.

Extensions include editing the code and reflashing the Arduino to amend the beat pattern, and introducing a second servo per Arduino.

The resulting working is chaotic, noisy, collaborative, whimsical, and features participants contributing towards a shared goal.

## Codebase & version history

This is effectively version 2 of the code, with stubs/loops for handling more than two servos per Arduino. The resulting array assignment is slightly less clean than previous versions of the code, which may lead to more confusion/errors during workshops. We expect the code to evolve further.

New features over the (unpublished) version 1 code:

* beats per minute / tempo calculations actually do what they're supposed to, rather than leading to negative delays. Which don't work so well, funnily enough.
* Servo twitch code is now rolled into the main loop rather than incorporated in the helper function. While we liked the neatness of the latter, it made synchronised movement of two servos impossible to wrap our heads around. This does render the helper function more-or-less pointless, but I'm too proud of the object dereferencing to delete it just yet.
* In principle, extending the code to handle >2 servos should be very straightforward.
* Main loop is much cleaner.

## Notes

Since we want a beat and 'no beat' (a 'miss') to take the same amount of time, each servo is called to move on each possible beat. What changes is the deflection angle requested. This appears to work well.

TODO: Upload Fritzing diagrams used in workshop  
TODO: Provide some example results!

## Credits

Workshop and code by Jonathan Sanderson, Northumbria University, 2015-16. Based on an idea I first saw at [Maker Faire UK](http://www.makerfaireuk.com) in about 2011, by Alistair MacDonald ([@alistair](https://twitter.com/alistair)).

Funding to support this aspect of Think Physics came from the [Reece Foundation](http://www.reece-foundation.org "Reece Foundation | Supporting engineering in the region").