uis = ui/IntroWidget.py ui/LabelingWidget.py
uiRes = ui/images/icons_rc.py
scripts = ../env/Scripts
outName = ALJILabelHelper
oneExe = dist/$(outName).exe
manyExe = dist/$(outName)/$(outName).exe
upx = --noupx

run: all
	python Controller.py

distRun: dist
	$(manyExe)

all: $(uis) $(uiRes)

%.py: %.ui
	$(scripts)/pyuic5.exe $^ -o $@ --import-from .images

%_rc.py: %.qrc
	$(scripts)/pyrcc5.exe $^ -o $@


# ui/images/icons_rc.py: ui/images/icons.qrc
# 	$(scripts)/pyrcc5.exe $^ -o $@

# rc: ui/images/icons_rc.py

# %_rc.py: %.qrc
# 	$(scripts)/pyrcc5.exe $^ -o $@

# uiResources: ui/uiResources.py

$(oneExe): all
	pyinstaller --windowed --onefile Controller.py --name $(outName) $(upx)

$(manyExe): all
	pyinstaller --windowed Controller.py --name $(outName) $(upx)

distOne: $(oneExe) distResources
dist: $(manyExe) distResources

distResources:
	cp --recursive --force Journals dist/
	cp --recursive --force ui/images dist/

dev: all
	start ../devProject.sublime-project -WindowStyle Hidden

designer:
	$(scripts)/designer.exe &

clean:
	rm -f $(uis) &
	rm -f $(uiRes) &
	rm -f Controller.spec &
	rm -rf __pycache__ &
	rm -rf build/ &
	rm -rf dist/ &
