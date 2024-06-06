import display
import urequests


def getHackHourTime():
    hackHourTime = urequests.get(
        url="http://hackhour.hackclub.com/api/clock/U062UG485EE")
    return hackHourTime.text


# start listening for the hack hour
minutesLeft = 0
while True:
    # get the hack hour from the server
    # find the minutes left as hack hour gives the end time in unix timestamp
    minutesLeft = getHackHourTime()
    timeToDisplay = (int(minutesLeft) / 60000 -
                     (int(minutesLeft) // 60000)) * 60 + 1
    print(timeToDisplay)
    if minutesLeft == "-1":
        display.displayLED("0000", 0.5)
        break
    display.displayLED(round(int(minutesLeft) / 60000),
                       timeToDisplay)
