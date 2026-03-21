


#
#
#
# this silly program is designed to correct the time on a cheap chinese digital clock that runs slow
#
# logic
#
# button presses
#	three of the original buttons on the clock were remove
#	those three buttons, labeled SET, UP and DOWN are now connected to a relay board
#
#	button presses can be short of long
#	long press is 2.5 seconds
#	short press will be defined in a constant, but probably 500 msec
#
# to advance the clock
#	press the set button for 2 seconds
#	press the set button 
#
#	the original version used the lower level GPIO library
#	this one uses the easier one, gpiozero


from gpiozero import OutputDevice
import time
import sys
from datetime import datetime

# press durations in milliseconds
SHORT = 0.60
LONG = 2.500
PAUSE = 0.5

PINS = {}

PINS['set'] = OutputDevice(26)
PINS['up'] = OutputDevice(19)
PINS['down'] = OutputDevice(13)
PINS['boot'] = OutputDevice(6)

def setModeHours():
   press('set',LONG);

def setModeMinutes():
   press('set',SHORT);

def endSetMode():
   press('set',SHORT)

def press(pname,duration):
   pin = PINS[pname]
   print(f'Pressing {pin} for {duration} seconds')
   pin.on()
   time.sleep(duration)
   pin.off()
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

def rebootClock():
   PINS['boot'].on()
   time.sleep(0.75)
   PINS['boot'].off()
   time.sleep(LONG)

if __name__ == '__main__':

   rebootClock()   
   
   now = datetime.now()

   deltaHours = now.hour - 12
   deltaMinutes = now.minute

   setModeHours()
   adjustTime(deltaHours)

   setModeMinutes()
   adjustTime(deltaMinutes)

   #press('set',2)
   #press('up',1)
   #press('down',1)

   endSetMode()

   




