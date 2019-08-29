frames = Frames/sentFrame.pickle Frames/journalFrame.pickle Frames/resultsFrame.pickle

run: sent

sent: SentTrainer.py Frames/sentFrame.pickle
	python SentTrainer.py

doc: DocTrainer.py Frames/journalFrame.pickle
	python DocTrainer.py

frames: $(frames)

%.pickle: Framing.py LabelResults/*
	python Framing.py

dev: 
	start ../devProject.sublime-project -WindowStyle Hidden

clean:
	rm -rf __pycache__ &
	rm -rf $(frames)
