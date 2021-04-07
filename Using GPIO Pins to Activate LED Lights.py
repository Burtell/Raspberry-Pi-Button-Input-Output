# Test branch of the code has GPIO and signal import removed

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
# for 3 seconds and deactivate when an outside signal is recieved)
racking_in.when_pressed = racking_led.on
time.sleep(3)
racking_in.when_released = racking_led.off
racking_out.when_pressed = racking_led.on
time.sleep(3)
racking_out.when_released = racking_led.off

#power_on button press
pause()
