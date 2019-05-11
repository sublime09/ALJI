objects = IntroWidget.py LabelingWidget.py 
scripts = ../env/Scripts
outName = ALJILabelHelper
oneExe = dist/$(outName).exe
manyExe = dist/$(outName)/$(outName).exe
upx = --noupx

run: all
	python Controller.py

distRun: dist
	$(manyExe)

all: $(objects)

%.py: %.ui
	$(scripts)/pyuic5.exe $^ -o $@

$(oneExe): all
	pyinstaller --windowed --onefile Controller.py --name $(outName) $(upx)

$(manyExe): all
	pyinstaller --windowed Controller.py --name $(outName) $(upx)

distOne: $(oneExe) distResources
dist: $(manyExe) distResources

distResources:
	cp --recursive --force Journals dist/
	cp --recursive --force images dist/

dev: all
	start ../devProject.sublime-project -WindowStyle Hidden

designer:
	$(scripts)/designer.exe &

clean:
	rm -f $(objects) &
	rm -f Controller.spec &
	rm -rf __pycache__ &
	rm -rf build/ &
	rm -rf dist/ &
