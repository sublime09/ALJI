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

defaultLabels = '''
Consistent depressed mood
Loss of interest/pleasure
Change in weight/appetite
Insomnia / Hypersomnia
Psychomotor agitation/retardation
Fatigue
Feelings of worthlessness/guilt
Diminished concentration/solving ability
Recurrent thoughts of death
Stressful traumatic event
Intrusive memories of past trauma
Avoidance of stimuli associated with trauma
Negative alterations in cognition/mood
Excessive Anxiety and worry over 6 months
'''.strip().split('\n')
defaultLabels = [d.strip() for d in defaultLabels]

