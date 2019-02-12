# ALJI
The Active Listening Journal Interaction project.  Detecting and intervening in mental health crises from journal entry analysis.  

**Setup**:
```console
virtualenv env
env/Scripts/activate
pip -r requirements.txt
```


### Scholastic Pull:

For pulling journal entries off of the scholastic awards website
`python 'Scholastic Pull'/ScholasticPull.py`


Uses: 
- Python3.6
- [Selenium WebDriver](https://docs.seleniumhq.org/) (Firefox) 
  - Be sure to [install gecko](https://github.com/mozilla/geckodriver/releases) 
  - Add the .exe file to your system path
- [Beautiful Soup 4](https://pypi.org/project/beautifulsoup4/)
  - Uses the lxml 4.3 parser


### SOON: Journal ANA:

For the preliminary journal entry analysis (sentiment, LWIC, etc...)

Uses:
- LIWC
- ANEW
- VaderSentiment

### SOON: Label Helper:

For expert labeling of language signaling mental health crises

### SOON: ALJI:

For real use of mental health crisis detection of one individual

### Old:

Archived code that may be useful later.  Not functional or tested.  
