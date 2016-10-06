"""Trying to wrap my head around iterating over tuples.

Turns out, a single-element tuple still needs a closing comma,
or it's not a tuple at all. So: robots = ("00",) is a tuple,
but robots = ("00") isn't. Sheesh.
"""
# robots = ("00", "01", "02", "03", "04")
robots = ("00",)

for robot in robots:
    print robot

instruments = {"00": "skutter_18:FE:34:FD:91:AD",
               "01": "skutter_5C:CF:7F:01:5B:22",
               "02": "skutter_18:FE:34:FD:92:D1",
               "03": "skutter_18:FE:34:F4:D3:BD",
               "04": "skutter_18:FE:34:FD:93:33"
               }

print

for instrument in instruments:
    print instrument

print

for instrument in instruments:
    print instruments[instrument]

print

for robot in robots:
    print instruments[robot]
