objects = IntroWidget.py LabelingWidget.py DelCrisisDialog.py
scripts = ../env/Scripts

all: $(objects)

run: all
	python Controller.py

%.py: %.ui
	$(scripts)/pyuic5.exe $^ -o $@

dev: all
	start ../devProject.sublime-project -WindowStyle Hidden

designer:
	start $(scripts)/designer.exe -WindowStyle Hidden

clean:
	rm $(objects)
