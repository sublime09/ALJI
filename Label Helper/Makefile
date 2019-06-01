uis = ui/IntroWidget.py ui/LabelingWidget.py
uiRes = ui/images/icons_rc.py
scripts = ../env/Scripts
outName = ALJILabelHelper
manyExe = dist/$(outName)/$(outName).exe
pyInstallOpts = --windowed --name $(outName) --noupx

run: all 
	python Controller.py

all: $(uis) $(uiRes) Controller.py
dist: all exe distResources
$(manyExe): exe

distRun: $(manyExe)
	cd dist/$(outName)/; $(outName).exe

%.py: %.ui
# 	$(scripts)/pyuic5.exe $^ -o $@ 
	$(scripts)/pyuic5.exe $^ -o $@ --import-from .images

%_rc.py: %.qrc
	$(scripts)/pyrcc5.exe $^ -o $@

exe: $(outName).spec all
	pyinstaller $(outName).spec

spec: all
	pyinstaller Controller.py $(pyInstallOpts)
oneSpec: all 
	pyinstaller Controller.py $(pyInstallOpts) --onefile

distResources: all
	cp --recursive --force Journals dist/

dev: all 
	start ../devProject.sublime-project -WindowStyle Hidden

designer:
	$(scripts)/designer.exe &

clean:
	rm -f $(uis) &
	rm -f $(uiRes) &
	rm -rf __pycache__ &
	rm -rf build/ &
	rm -rf dist/ &
	rm -rf LabelResults
