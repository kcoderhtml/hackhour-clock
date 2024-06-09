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
    secondsLeftInThisMinute = (minutesLeft - (minutesLeft // 1)) * 60 + 1  # minutesLeft // 1 is the integer part of the minutes left
    print(f"{int(minutesLeft)}:{secondsLeftInThisMinute:02} remaining")
    if millisecondsLeft == "-1":
        display.displayLED("0000", 60)
    else:
        display.displayLED(int(minutesLeft), # floor the minutes left
                       secondsLeftInThisMinute)
