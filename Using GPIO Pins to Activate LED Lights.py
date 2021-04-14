#Test loops and booleans for LED's

# button presses and their ports
from gpiozero import Button, LED
from signal import pause
import time


def ledTimer(ledName, timeVar):
    while timeVar != -1:
        time.sleep(1)
        if timeVar == 0:
            ledName.on()
        timeVar -= 1



racking_in = Button(2)
racking_out = Button(3)
power_on = Button(4)
power_off = Button(17)
permissive = Button(27)
e_stop = Button(22)

# led and their ports
racking_led = LED(5)
test_led = LED(6)
open_led = LED(13)
close_led = LED(19)
connect_led = LED(26)
disconnect_led = LED(12)

# if either racking buttons are pressed (so these activate when the button is held for 3 seconds and deactivate when an outside signal is received)
while racking_in.when_held:
    ledTimer(racking_led, 3)
#i would assume some code needs to go here to tell it when to shut off the LED
while racking_out.when_held:
    ledTimer(racking_led, 3)
    
#holding both the permissive and the close should activate this sequence
if permissive.when_held and power_on.when_held:
    close_led.on()

#when the open button is pressed, this LED should come on (but for how long?)
power_off.when_pressed = open_led.on

#need to add a stop LED or figure out how the light will be activated when power is sent to the button
e_stop.when_released = stop.off
e_stop.when_pressed = stop.on

pause()



