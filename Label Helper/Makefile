uisFold = ui/
uis = $(uisFold)IntroWidget.py $(uisFold)LabelingWidget.py
uiRes = $(uisFold)images/icons_rc.py
scripts = ../env/Scripts
outName = ALJILabelHelper
manyExe = dist/$(outName)/$(outName).exe
upx = --noupx

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
	pyinstaller --windowed Controller.py --name $(outName) $(upx)
# oneDist: all 
# 	pyinstaller --onefile --windowed Controller.py --name $(outName) $(upx)

distResources: all
	cp --recursive --force Journals dist/
# 	mkdir dist/ui
# 	cp --recursive --force images dist/ui
# 	cp --recursive --force Journals dist/$(outName)/
# 	cp --recursive --force images dist/$(outName)/

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
