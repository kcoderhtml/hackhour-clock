import time
import tm1637
from machine import Pin
tm = tm1637.TM1637(clk=Pin(5), dio=Pin(4))


def decimalPlace(displayString):
    currentPosition = 4
    for character in displayString:
        if character == '.':
            break
        currentPosition = currentPosition - 1
    return currentPosition


def displayLED(displayNumber, displayTimer):
    try:
        outputDisplay(displayNumber, displayTimer)
    except:
        print("Error")
        tm.show('Error')
        time.sleep(0.0005)


def outputDisplay(displayNumber, displayTimer):
    displayTimer = displayTimer * 1000  # Convert to milliseconds
    displayString = str(displayNumber)

    # Left Pad with blanks
    noDecimal = displayString.replace('.', '')    # Remove decimal point
    stringLength = len(noDecimal)
    if stringLength == 3:
        displayString = ' ' + displayString
    if stringLength == 2:
        displayString = '  ' + displayString
    if stringLength == 1:
        displayString = '   ' + displayString
    print("displayString="+displayString)

    # see https://docs.micropython.org/en/latest/library/time.html for docs on ticks_ms()
    startTime = time.ticks_ms()
    while time.ticks_add(startTime, displayTimer) > time.ticks_ms():
        time.sleep(0.0005)
        tm.show(displayString)

    # Once finished blank out the fist left most digit
    # as it's the only one that sticks
    tm.show('    ')
    time.sleep(0.0005)
