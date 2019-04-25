objects = IntroWidget.py LabelingWidget.py

all: $(objects)

IntroWidget.py: IntroWidget.ui
	echo "Building IntroWidget.py..."
	../env/Scripts/pyuic5.exe IntroWidget.ui -o IntroWidget.py

LabelingWidget.py: LabelingWidget.ui
	echo "Building LabelingWidget.py..."
	../env/Scripts/pyuic5.exe LabelingWidget.ui -o LabelingWidget.py

# LabelingWindow.py: LabelingWindow.ui
# 	echo "Building LabelingWindow.py..."
# 	../env/Scripts/pyuic5.exe LabelingWindow.ui -o LabelingWindow.py
# IntroWindow.py: IntroWindow.ui
# 	echo "Building IntroWindow.py..."
# 	../env/Scripts/pyuic5.exe IntroWindow.ui -o IntroWindow.py

run: all
	python Controller.py

clean :
	rm "$(objects)"
	echo "cleaned"
