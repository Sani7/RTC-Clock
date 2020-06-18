from clock import *

try:
        while (1):
                (Digit1, Digit2, Digit3, Digit4, Leds) = GetTimeToDigit()
                DisplayDigit(Digit1, 1)
                Delay()
                DisplayDigit(Digit2, 2)
                Delay()
                DisplayDigit(Digit3, 3)
                Delay()
                DisplayDigit(Digit4, 4)
                Delay()
                DisplayLeds(Leds)

except KeyboardInterrupt:
        GPIO.cleanup()
