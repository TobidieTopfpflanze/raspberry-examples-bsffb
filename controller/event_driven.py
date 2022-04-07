import evdev

# seccond controller would be /dev/input/event1
controllerDev = evdev.InputDevice('/dev/input/event0')

while True:
    for key_id in controllerDev.active_keys():
        if (key_id == 293):
            # Do stuff if specific button is pressed
            print("button pressed")
        if (key_id == 292):
            print("other button pressed")

    # Do other stuff here