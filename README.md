# ALJI
The Active Listening Journal Interaction project.  Detecting and intervening in mental health crises from journal entry analysis.  

**Setup**: 
1. Install [Python](https://www.python.org/) 3.6 and then upgrade pip
1. **Recommended**: Use [virtualenv](https://virtualenv.pypa.io/en/stable/) for easy python package management in projects.  
    - Easy as `virtualenv env` and then `env/Scripts/activate`.  `deactivate` when done working. 
1. `pip -r requirements.txt`

### Scholastic Pull:

For pulling journal entries off of the scholastic awards website
```python ScholasticPull.py```

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
- [LIWC](https://liwc.wpengine.com/)
- [Empath](https://github.com/Ejhfast/empath-client)
- ANEW
- VaderSentiment

### SOON: Label Helper:

For expert labeling of language signaling mental health crises

### SOON: ALJI:

For real use of mental health crisis detection of one individual

### Old:

Archived code that may be useful later.  Not functional or tested.  
