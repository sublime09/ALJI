# ALJI
The **A**ctive **L**istening **J**ournal **I**nteraction project.  ALJI aims to detect and intervene in mental health crises by analyzing a personal journal entry while maintaining the author's privacy.  

### [Main Webpage](https://sublime09.github.io/ALJI/)

**Developer Setup**: 
1. Install [Python](https://www.python.org/) 3.7 and then upgrade pip to 19.  Newer versions of software and packages may work, but are not tested. 
1. **Recommended**: Install and use [virtualenv](https://virtualenv.pypa.io/en/stable/) for easy python package management in projects.  
    - Easy to setup with: `virtualenv env`  Activate with either `env/Scripts/activate`   Deactivate with: `deactivate` 
    - *Powershell*: You may need to `Set-ExecutionPolicy RemoteSigned` due to [this update](https://virtualenv.pypa.io/en/stable/changes/#v16-2-0-2018-12-31)
1. `pip install -r requirements.txt`  This installs the required for packages for ***every*** component of the ALJI project.  Some components need some minor additions or configuration (see below).  Navigating to and focusing on one component is advisable. 


#### Legal Notice:
This open-source project uses the LGPLv3 license, but has connections to other projects, each with their own licenses.  Please refer and abide by the license agreements of those projects as well as this one. 

## Folders / Components of ALJI

### Scholastic Pull:
For pulling journal entries off of the scholastic awards website.  Uses: 
- [Selenium WebDriver for Firefox](https://docs.seleniumhq.org/projects/webdriver/) to automate browser control. ([Apache2.0 license](https://raw.githubusercontent.com/SeleniumHQ/selenium/master/LICENSE))
  - Be sure to [install Gecko](https://github.com/mozilla/geckodriver/releases) and add it to your PATH.  ([Mozilla Public Lecense](https://www.mozilla.org/en-US/MPL/2.0/))
- [Beautiful Soup 4](https://pypi.org/project/beautifulsoup4/) to handle html parsing. ([MIT license](https://bazaar.launchpad.net/~leonardr/beautifulsoup/bs4/view/head:/LICENSE))
  - Needs the [lxml](https://github.com/lxml/lxml) 4.3 parser. ([BSD license](https://raw.githubusercontent.com/lxml/lxml/master/doc/licenses/BSD.txt))

### Journal ANA:
For the preliminary journal entry analysis (sentiment, negativity, etc...) and model training.  Uses:
- [Empath](https://github.com/Ejhfast/empath-client) to give broad labels to text. ([MIT License](https://raw.githubusercontent.com/Ejhfast/empath-client/master/LICENSE.txt))

Considered for future use:
- [LIWC](https://liwc.wpengine.com/) (Linguistic Inquiry and Word Count)
- [ANEW](https://csea.phhp.ufl.edu/Media.html#bottommedia) (Affective Norms for English Words)
- [VaderSentiment](https://github.com/cjhutto/vaderSentiment) (Valence Aware Dictionary and sEntiment Reasoner)

### ALJI Label Helper:
For enabling experts to label journal texts for language that signals a mental health crisis.  Uses: 
- [PyQt5](https://www.riverbankcomputing.com/software/pyqt/) to design the GUI. ([GPLv3 license](https://www.riverbankcomputing.com/static/Docs/PyQt5/introduction.html#license))
- [PyInstaller](http://www.pyinstaller.org/) to build a single executable. ([GPLv2 license](https://raw.githubusercontent.com/pyinstaller/pyinstaller/develop/COPYING.txt))
	- Warning: [UPX](https://upx.github.io/) can help compress the executable, but can also break builds if not configured correctly.  PyInstaller tries to use UPX by default if available
- (Optional) [Make](https://www.gnu.org/software/make/) for quicker development process. 
	- See `LabelHelper\Makefile` for valid commands. Also see: [Make for Windows](http://gnuwin32.sourceforge.net/packages/make.htm) and [MinGW](http://mingw.org/)


### Soon: ALJI Trainer:
For the training of machine learning models that can predict a mental heath crisis through journal language

### SOON: ALJI:
For real use of mental health crisis detection of one individual

### Old:
Archived code that may be useful later.  Not functional or tested.  
