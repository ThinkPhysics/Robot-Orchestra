# Trying to parse mouse cliks on a guizero waffle element
# This almost works, amazingly (given that I'm just throwing stuff
# at the screen), but the click positions are all wrong. Scaling is off.
# ...which isn't a great surprise, since the numbers are all made up.

from guizero import App, Waffle
from tkinter import Frame

app = App()


def callback(event):
    print("Clicked at: ", event.x, event.y)


# Set the waffle to have a memory
my_waffle = Waffle(App, remember=True)

my_waffle.set_pixel(2, 1, "red")

# Now your waffle will remember what colour each pixel is!
print(my_waffle.get_pixel(2, 1))

# Even the ones aut0-set at the start (which are white by default)
print(my_waffle.get_pixel(1, 1))

frame = Frame(my_waffle, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()


app.display()
