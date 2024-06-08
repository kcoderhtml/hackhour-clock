# The home of the Hack Hour clock firmware

This should work! To try it on your pico clock download the repo and create a new file called `secrets.py` in the root directory. Add the following lines to the file:

```python
SSID = "YOUR_WIFI_SSID"
PASSWORD = "YOUR_WIFI_PASSWORD"
```

then modify the main.py file to change the slack id to your slack id this should be on line 7:

```python
 def getHackHourTime():
    hackHourTime = urequests.get(
        url="http://hackhour.hackclub.com/api/clock/{edit this part to your slack id}")

    return hackHourTime.text
```

now hold down the button on the back of your pico and plug in your pico. Then download [this micropython uf2 file](https://micropython.org/resources/firmware/RPI_PICO_W-20240602-v1.23.0.uf2) and copy it onto your pico. Once the pico restarts silently and the usb drive disappears you can go to vscode and (if you have the micropico extension installed which you should) run the command "MicroPico: upload project to Pico" once it finishes uploading unplug your pico and plug it back in. You should now see the time on the screen! If you have any questions feel free to ask in the #arcade-hour-bts channel on slack and I would be more than happy to help! 
