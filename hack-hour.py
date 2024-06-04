from machine import Pin
import rp2
import display

# Main Code
# make a loading animation where it goes ....0.1.2.3.4
loadingAnimation = ["0000", "0001", "0012", "0123", "1234"]
for item in loadingAnimation:
    display.displayLED(item, 0.5)

# wait until the button on the pico is pressed
while rp2.bootsel_button() == 0:
    display.displayLED("AAAA", 0.5)

display.displayLED("    ", 0.5)
# start the hack hour
