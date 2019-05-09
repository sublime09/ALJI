objects = IntroWidget.py LabelingWidget.py DelCrisisDialog.py
scripts = ../env/Scripts

all: $(objects)

run: all
	python Controller.py

dist: all
	pyinstaller --windowed --onefile Controller.py
	cp -R Journals dist/Journals
	cp -R images dist/images
	mv dist/Controller.exe dist/ALJILabelHelper.exe
# 	links don't work... :(
# 	cmd /d dist /c mklink runController.exe Controller//Controller.exe
# 	ln --symbolic --force dist/runLink dist/Controller/Controller.exe
# 	New-Item -Path "runLink" -ItemType "SymbolicLink" -Value "./Controller/Controller.exe"
# 	cp --symbolic-link ./Controller/Controller.exe ./runLink

%.py: %.ui
	$(scripts)/pyuic5.exe $^ -o $@

dev: all
	start ../devProject.sublime-project -WindowStyle Hidden

designer:
	start $(scripts)/designer.exe 

clean:
	rm $(objects)
	rm -f Controller.spec
	rm -rf __pycache__
	rm -rf build/
	rm -rf dist/

