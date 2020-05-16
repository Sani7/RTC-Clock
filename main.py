from clock import *

try:
        while (1):
                (Digit1, Digit2, Digit3, Digit4, Leds) = GetTimeToDigit()
                DisplayDigit(Digit1, 1)
                wachten()
                DisplayDigit(Digit2, 2)
                wachten()
                DisplayDigit(Digit3, 3)
                wachten()
                DisplayDigit(Digit4, 4)
                wachten()
                DisplayLeds(Leds)

except KeyboardInterrupt:
        GPIO.cleanup()
