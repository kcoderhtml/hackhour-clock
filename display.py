from machine import Pin, SPI
import time

MOSI = 11
SCK = 10
RCLK = 9

THOUSANDS = 0xFE
HUNDREDS = 0xFD
TENS = 0xFB
UNITS = 0xF7
Dot = 0x80

SEG8Code = [
    0x3F,  # 0
    0x06,  # 1
    0x5B,  # 2
    0x4F,  # 3
    0x66,  # 4
    0x6D,  # 5
    0x7D,  # 6
    0x07,  # 7
    0x7F,  # 8
    0x6F,  # 9
    0x77,  # A (10)
    0x7C,  # b (11)
    0x39,  # C (12)
    0x5E,  # d (13)
    0x79,  # E (14)
    0x71,  # F (15)
    0x00,  # Blank (16)
    0x00  # Decimal Point (17)
]


class LED_8SEG():
    def __init__(self):
        self.rclk = Pin(RCLK, Pin.OUT)
        self.rclk(1)
        self.spi = SPI(1)
        self.spi = SPI(1, 1000_000)
        self.spi = SPI(1, 10000_000, polarity=0, phase=0,
                       sck=Pin(SCK), mosi=Pin(MOSI), miso=None)
        self.SEG8 = SEG8Code
    '''
    function: Send Command
    parameter: 
        Num: bit select
        Seg: segment select       
    Info:The data transfer
    '''

    def write_cmd(self, Num, Seg):
        self.rclk(1)
        self.spi.write(bytearray([Num]))
        self.spi.write(bytearray([Seg]))
        self.rclk(0)
        time.sleep(0.002)
        self.rclk(1)


def decodeString(displayString):
    displayList = []
    for character in displayString:
        if character == '0':
            code = 0
        if character == '1':
            code = 1
        if character == '2':
            code = 2
        if character == '3':
            code = 3
        if character == '4':
            code = 4
        if character == '5':
            code = 5
        if character == '6':
            code = 6
        if character == '7':
            code = 7
        if character == '8':
            code = 8
        if character == '9':
            code = 9
        if character == 'A' or character == 'a':
            code = 10
        if character == 'B' or character == 'b':
            code = 11
        if character == 'C' or character == 'c':
            code = 12
        if character == 'D' or character == 'd':
            code = 13
        if character == 'E' or character == 'e':
            code = 14
        if character == 'F' or character == 'f':
            code = 15
        if character == ' ':
            code = 16
        if character == '.':
            code = 17
        if code != 17:
            displayList.append(code)
    return displayList


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
        LED = LED_8SEG()
        LED.write_cmd(THOUSANDS, LED.SEG8[14])    # Display E
        time.sleep(0.0005)


def outputDisplay(displayNumber, displayTimer):
    displayTimer = displayTimer * 110  # Convert timer to seconds
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

    displayList = decodeString(displayString)
    decimalPosition = decimalPlace(displayString)

    LED = LED_8SEG()
    while displayTimer > 0:
        time.sleep(0.0005)
        if decimalPosition == 0:
            LED.write_cmd(UNITS, LED.SEG8[displayList[3]] | Dot)
        else:
            LED.write_cmd(UNITS, LED.SEG8[displayList[3]])
        time.sleep(0.0005)
        if decimalPosition == 1:
            LED.write_cmd(TENS, LED.SEG8[displayList[2]] | Dot)
        else:
            LED.write_cmd(TENS, LED.SEG8[displayList[2]])
        time.sleep(0.0005)
        if decimalPosition == 2:
            LED.write_cmd(HUNDREDS, LED.SEG8[displayList[1]] | Dot)
        else:
            LED.write_cmd(HUNDREDS, LED.SEG8[displayList[1]])
        time.sleep(0.0005)
        if decimalPosition == 3:
            LED.write_cmd(THOUSANDS, LED.SEG8[displayList[0]] | Dot)
        else:
            LED.write_cmd(THOUSANDS, LED.SEG8[displayList[0]])
        time.sleep(0.0005)
        displayTimer = displayTimer-1

    # Once finished blank out the fist left most digit
    # as it's the only one that sticks
    LED.write_cmd(UNITS, LED.SEG8[16])
    time.sleep(0.0005)
