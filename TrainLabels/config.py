import sys

## check if in virtual environment or not
if not hasattr(sys, 'real_prefix'):
	print("WARNING: Not using a virtual environment...")
	resp = input("Continue?").strip().lower()
	if resp not in "yes y".split():
		print("Exiting...")
		exit()

import logging as log

logArgs = dict(filemode= 'w', filename='Trainer.log', level=log.DEBUG)
log.basicConfig(**logArgs)
