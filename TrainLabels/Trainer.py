import fileIO
from pprint import pprint
# from collections.abc import Iterable
from collections import namedtuple
from box import Box

defaults = '''
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
'''.split('\n')
defaults = [d for d in defaults if d.strip() != ""]


def main():
	print("Started Trainer main....")
	for r in fileIO.readResultsGen():
		for markedJournal in r['marks']:
			for l in markedJournal['labels']:
				if l not in defaults:
					print("Custom:", l)
	print("Done with main")


# from inspect import signature
# pprint(signature(pprint))

if __name__ == '__main__':
	main()
