import display
import urequests


def getHackHourTime():
    print("Getting hack hour time")
    hackHourTime = urequests.get(
        url="http://hackhour.hackclub.com/api/clock/U062UG485EE")
    return hackHourTime.text


# start listening for the hack hour
millisecondsLeft = 0
while True:
    # get the hack hour from the server
    # find the minutes left as hack hour gives the end time in unix timestamp
    millisecondsLeft = getHackHourTime()
    minutesLeft = int(millisecondsLeft) / 1000 / 60
    # minutesLeft // 1 is the integer part of the minutes left
    secondsLeftInThisMinute = (minutesLeft - (minutesLeft // 1)) * 60 + 1
    print(f"{int(minutesLeft)}:{secondsLeftInThisMinute:02} remaining")
    if millisecondsLeft == "-1":
        display.displayLED("00:00", 60)
    else:
        display.displayLED(str(minutesLeft) + ":00",  # floor the minutes left
                           secondsLeftInThisMinute)
