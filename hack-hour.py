import rp2
import display

import secrets
import network

# make a loading animation where it goes ....0.1.2.3.4
loadingAnimation = ["0000", "0001", "0012", "0123", "1234"]

# Connect to the WiFi network
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(secrets.SSID, secrets.PASSWORD)

# Wait until the connection is established
itemCounter = 0
while not wifi.isconnected():
    display.displayLED(loadingAnimation[itemCounter], 0.25)
    itemCounter = (itemCounter + 1) % len(loadingAnimation)

# Display the IP address
display.displayLED(wifi.ifconfig()[0], 3)

# wait until the button on the pico is pressed
while rp2.bootsel_button() == 0:
    display.displayLED("AAAA", 0.5)

display.displayLED("    ", 0.5)
# start the hack hour
