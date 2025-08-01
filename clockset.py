


#
#
#
# this silly program is designed to correct the time on a cheap chinese digital clock that runs slow
#
# logic
#
# on a schedule
#	take a picture of the clock face (7-segment display)
#	use OCR to convert the screen to a set of numbers
#	convert that to local time
#	get the actual local time
#	compute the delta between the clock time and the actual time (in minutes)
#	advance the clock by delta minutes (negative number retards the clock)
#
# button presses
#	three of the original buttons on the clock were remove
#	those three buttons, labeled SET, UP and DOWN are now connected to a relay board
#		SET = Relay 1
#		UP = Relay 2
#		DOWN = Relay 3
#
#	button presses can be short of long
#	long press is 2.5 seconds
#	short press will be defined in a constant, but probably 500 msec
#
# to advance the clock
#	press the set button for 2 seconds
#	press the set button 




import RPi.GPIO as GPIO
import time

# press durations in milliseconds
SHORT = 0.60
LONG = 2.500
PAUSE = 0.5


PINS = {}

PINS['set'] = 11
PINS['up'] = 13
PINS['down'] = 15

def initializeGPIO():
   GPIO.setmode(GPIO.BOARD)
   for x in PINS.items():
      # print(x,x[0],x[1])
      GPIO.setup(x[1],GPIO.OUT)

def setModeHours():
   press('set',LONG);

def setModeMinutes():
   press('set',SHORT);

def endSetMode():
   press('set',SHORT)

def press(pin,duration):
   print(f'Pressing {pin} for {duration} seconds')
   GPIO.output(PINS[pin],1)
   time.sleep(duration)
   GPIO.output(PINS[pin],0)
   time.sleep(PAUSE)

def adjustTime(kminutes):
   if kminutes > 0:
      pin = 'up'
   else:
      pin = 'down'

   npresses = abs(kminutes)
   while npresses >0:
      press(pin,SHORT)
      npresses = npresses - 1


if __name__ == '__main__':

   initializeGPIO()

   setModeHours()
   adjustTime(1)

   setModeMinutes()
   adjustTime(-20)

   #press('set',2)
   #press('up',1)
   #press('down',1)

   endSetMode()

   




