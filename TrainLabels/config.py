import sys
if not hasattr(sys, 'real_prefix'):
	print("WARNING: Not using a virtual environment...")
	resp = input("Continue?").strip().lower()
	if resp not in "yes y".split():
		print("Exiting...")
		exit()

# import cutie
# askYN = cutie.prompt_yes_or_no

import logging as log
# from inspect import getmembers # helps explore

logArgs = dict(filemode= 'w',
	filename='Trainer.log',
	level=log.DEBUG)
log.basicConfig(**logArgs)
