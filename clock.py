#library for RTC clock
import time
import datetime
import math
import RPi.GPIO as GPIO # Importing the GPIO library
GPIO.setmode(GPIO.BCM)	# Setting the right Board layout that is used.
GPIO.setup(5, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(18, GPIO.OUT) #LEDS

Digit = (5, 26, 16, 13, 19, 21, 20, 6) # LB, LO, RB, RO, MO, MM, MB, DP
Select = (4, 17, 27, 22) # D1, D2, D3, D4

t = GPIO.HIGH
f = GPIO.LOW

def SetDigits(Decimal, DP):
        global Digit
        if Decimal == 0:
                GPIO.output(Digit, (f, f, f, f, f, t, f, t))
        elif Decimal == 1:
                GPIO.output(Digit, (t, t, f, f, t, t, t, t))
        elif Decimal == 2:
                GPIO.output(Digit, (t, f, f, t, f, f, f, t))
        elif Decimal == 3:
                GPIO.output(Digit, (t, t, f, f, f, f, f, t))
        elif Decimal == 4:
                GPIO.output(Digit, (f, t, f, f, t, f, t, t))
        elif Decimal == 5:
                GPIO.output(Digit, (f, t, t, f, f, f, f, t))
        elif Decimal == 6:
                GPIO.output(Digit, (f, f, t, f, f, f, f, t))
        elif Decimal == 7:
                GPIO.output(Digit, (t, t, f, f, t, t, f, t))
        elif Decimal == 8:
                GPIO.output(Digit, (f, f, f, f, f, f, f, t))
        elif Decimal == 9:
                GPIO.output(Digit, (f, t, f, f, f, f, f, t))
        else:
                raise ValueError('Value Decimal is out of range')
        if DP == 1:
                GPIO.output(6, f)
        else:
                GPIO.output(6, t)

def DisplayDigit(InDecimal, DP, InDigit):
        global Select
        SetDigits(InDecimal, DP)
        if InDigit == 1:
                GPIO.output(Select, (t, f, f, f))
        elif InDigit == 2:
                GPIO.output(Select, (f, t, f, f))
        elif InDigit == 3:
                GPIO.output(Select, (f, f, t, f))
        elif InDigit == 4:
                GPIO.output(Select, (f, f, f, t))
        else:
                raise ValueError('Value InDigit is out of range')

def Delay():
        time.sleep(.001)

def DisplayLeds(StatusLeds):
        if StatusLeds:
                GPIO.output(18, t)
        else:
                GPIO.output(18, f)

def GetTimeToDigit():
        now = datetime.datetime.now()		# Getting the time to a variable called now
        hour = now.hour					
        hour10 = math.floor(hour / 10)		# Calculating the first digit of the hour variable
        hour1 = hour % 10					# Calculating the seccond digit of the hour variable
        minute = now.minute
        minute10 = math.floor(minute / 10)	# Calculating the first digit of the minute variable
        minute1 = minute % 10				# Calculating the seccond digit of the minute variable
        Leds = now.second % 2 == 0
        return (hour10, hour1, minute10, minute1, Leds)
