import evdev

# seccond controller would be /dev/input/event1
controllerDev = evdev.InputDevice('/dev/input/event0')

# wait for events
for event in controllerDev.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        # Print some debug informations to the console
        print(evdev.categorize(event))
        print(controllerDev.active_keys())

        for key_id in controllerDev.active_keys():
            if (key_id == 293):
                # Do stuff if specific button is pressed
                print("button pressed")
            if (key_id == 292):
                print("other button pressed")
        
        # Do other stuff here when any button is pressed
        