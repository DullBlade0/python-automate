#! python3
#  stopwatch.py - A simple stopwatch

import time, pyperclip
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1
text = ''
# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = str(round(time.time() - lastTime, 2))
        totalTime = str(round(time.time() - startTime, 2))
        lap = 'Lap #'+ str(lapNum).rjust(1) + '' + totalTime.rjust(6) + ' (' + lapTime.rjust(6) + ')\n'
        print(lap)
        text.join(lap)
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    print('\nDone.')
pyperclip.copy(text)