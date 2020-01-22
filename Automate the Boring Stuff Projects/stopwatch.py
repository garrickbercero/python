#! /usr/bin/env python3
# stopwatch.py - A simple stopwatch program

import time

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input() # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1
lapNumjust = str(lapNum).rjust(2)

# TODO: Start tracking the lap times.

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        totalTimejust = str(totalTime).rjust(5)
        lapTimejust = str(lapTime).rjust(6)
        print('Lap #%s: %s (%s)' % (lapNumjust, totalTimejust, lapTimejust), end='')
        lapNum += 1
        lapNumjust = str(lapNum).rjust(2)
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt: 
    # Handle the Ctrl-C exception to keep its error message from displaying
    print('\nDone.')