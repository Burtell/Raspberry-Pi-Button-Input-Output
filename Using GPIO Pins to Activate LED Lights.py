#Test loops and booleans for LED's

# button presses and their ports
from gpiozero import Button, LED
from signal import pause
import time

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

# if either racking buttons are pressed (so these are actually supposed to activate when the button is held
# for 3 seconds and deactivate when an outside signal is received)
while racking_in.when_held:
    start_time = time.time()
    if time.time() - start_time >= 3:
        racking_led.on()

while racking_out.when_held:
    start_time = time.time()
    if time.time() - start_time >= 3:
        racking_led.on()

if permissive.when_held and power_on.when_held:
    connect_led.on()

#power_on button press
pause()



