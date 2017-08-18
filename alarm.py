import sys
import string
from time import sleep

argument = sys.argv
lenofarg = len(sys.argv)

if lenofarg != 2 :
	print "Usage: [python] alarm.py duration in minutes"
	print "Example: [python] alarm.py 10"
	print "Write 0 to test alarm clock immediately"
	print "Press Ctrl+C to terminate alarm clock early"
	sys.exit(1)
try:
	minutes = int(argument[1])
except ValueError:
	print "Invalid numeric value (%s) for minutes" %argument[1]
	print "Should be an integer with value >= 0"
	sys.exit(1)

if minutes < 0 :
	print "Invalid value for minutes, should be >= 0"
	sys.exit(1)

seconds = minutes * 60
if minutes == 1 :
	mess = " minute"
else:
	mess = " minutes"

try:
	if minutes > 0:
		print "Sleeping for " + str(minutes) + mess
		sleep(seconds)
	print "Wake up"
	for i in range(5):
		print chr(7),
		sleep(1)
except KeyboardInterrupt:
	print "Interrupted by user"
	sys.exit(1)   