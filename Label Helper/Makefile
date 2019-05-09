objects = IntroWidget.py LabelingWidget.py 
scripts = ../env/Scripts

run: all
	python Controller.py

all: $(objects)

%.py: %.ui
	$(scripts)/pyuic5.exe $^ -o $@

dist: all testupx
	pyinstaller --windowed --onefile Controller.py --name ALJILabelHelper
	cp --recursive --force Journals dist/
	cp --recursive --force images dist/

testupx:
	@echo "Testing for UPX..."
	@hash upx 2>/dev/null || { echo "WARNING: Missing UPX! Bloated .exe file should be expected";}

dev: all
	start ../devProject.sublime-project -WindowStyle Hidden

designer:
	start $(scripts)/designer.exe 

clean:
	rm -f $(objects)
	rm -f Controller.spec
	rm -rf __pycache__
	rm -rf build/
	rm -rf dist/

