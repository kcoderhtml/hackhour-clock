# The home of the Hack Hour clock firmware

This should work! To try it on your pico clock download the repo and create a new file called `secrets.py` in the root directory. Add the following lines to the file:

```python
SSID = "YOUR_WIFI_SSID"
PASSWORD = "YOUR_WIFI_PASSWORD"
```

then modify the main.py file to change the slack id to your slack id this should be on line 51:

```python
 def getHackHourTime():
    hackHourTime = urequests.get(
        url="http://hackhour.hackclub.com/api/clock/{edit this part to your slack id}")

    return hackHourTime.text
```