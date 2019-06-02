---
title: ALJI Label Helper Instructions
layout: default
---

# ALJI Label Helper Instructions

* [Goals of ALJI](#goals-of-alji)
* [Task Structure](#task-structure)
* [Task Labeling](#task-labeling)
* [Project Details](#project-details)
* [About Me](#about-me)


## Goals of ALJI

The ​ **A**ctive ​ **L**​istening ​ **J**​ournal ​ **I**​nteraction (​ **ALJI**​) project aims to create a program designed to support the counseling of young students with depression by privately responding to their expressive writing or personal journal entries. ALJI may be used as a widely accessible entry point into clinical mental health support systems, providing critical guidance to those with suffering health.

To achieve this, a crisis detection model must be created and tested on a number of personal journal texts. This model is designed to align as closely as possible to your judgment of the personal journal text (see the ​Machine Learning​ section). You are given the ALJI Label Helper program to help label the dataset, which will be used in the training and testing of the final ALJI program.

The texts in the current dataset are publicly sourced from the ​Scholastic Awards website​. The “Personal Essay and Memoir” category encourages a large amount of creativity and expressiveness from the authors, and is promising as a preliminary dataset. While this dataset may prove to be dissimilar to than actual private journal entries, the numerous benefits of a passive (non-interactive) ALJI program can outweigh the risks (see the ​Expressive Writing​ and ​Human-Computer Interaction sections).

The ALJI project is open-source to ensure transparency, encourage collaboration, and to respect the goals of the project. You can see all components and code related to the project here: [​https://github.com/sublime09/ALJI](​https://github.com/sublime09/ALJI)


## Task Structure

Your task has been designed to take roughly 30 minutes to complete. The program automatically saves your task progress periodically and on a normal close of the program. You will be shown about 6 journal entries to read and label, using the ALJI Label Helper program (links are below). Your participation and responses will be kept confidential.

You may withdraw from this task at any time, for any reason. Deleting all files associated with ALJI is simple: delete the file you downloaded and the folder you uncompressed from it.

**<span style="color:red">Warning</span>​**:
The journals you will see may contain stressful and graphic content. They may depict domestic violence, sexual violence, substance abuse, and other sensitive events and topics. Be aware of your own health and wellbeing before beginning the labeling task. Your health is more important than this project.

Take note of the group number assigned to you by the researcher (Patrick Sullivan). Make sure to select the group number on the very first screen that is shown. This number affects which journals you are assigned to label.


- [**Download Link for Windows**](https://github.com/sublime09/ALJI/releases/latest/download/ALJI_Label_Helper_Windows.zip)
     - Tested on Windows 10. Other systems may vary in results.
- [**Download Link for OSX**](https://github.com/sublime09/ALJI/releases/latest/download/ALJI_Label_Helper_Mac.zip)
     - **Note**: Macs may prevent you from starting the program because I am not registered as an "Apple Developer". Move the 'ALJI Label Helper' program to your Applications folder to reveal an option to open the unrecognized program and run it normally.  
	 - Tested on OSX 10.4 (Mojave). Other systems may may vary in results.
	 - Known bug: sometimes the main view appears frozen and unresponsive.
	   - Workaround: Scrolling in the main view will refresh the view.

**Troubleshooting / Reporting errors:**
- Contact the researcher through email and describe the error you encountered.
- A screenshot of the error is usually very helpful
- Attaching the “err.log” file found near the program may help as well.

## Task Labeling

**It is important you follow this guide when labeling journal entries to remain consistent with the other contributors:**

1. Read the entire passage as if it is an entry in someone's personal journal or diary
2. Consider the mental wellness of the author (assume the author is a high school senior in the USA, age 18)
3. Based off of the information in the entry, estimate the author’s ​CGI-S rating (Clinician Global Impression of Severity Scale). Input this rating into the box alongside the journal entry.
4. Take note of any sentences that are alarming or concerning (if any). If you believe the author of this journal may need professional mental health support / counseling, do the following:
	- Clarify the reason of your concern by applying a label to the journal entry ('checking' the checkbox). Some default labels are provided, and you may create custom labels as you see fit.
5. Continue labeling all journals within your group.
**After labeling all journals within your group, report your results:**
1. Locate the label results
- Find the folder named “LabelResults” in the same location where you ran the program.
- Inside the folder should be files similar to “Group1Labels.json”. These are the label results you created by using the program. You can read their contents like a normal text file. 
2. Email the researcher (Patrick Sullivan): [​sublime@vt.edu]
- Attach the JSON file you located to the email
- Feel free to add any thoughts, concerns, questions about the ALJI project.
- The researcher may respond through email at a later date asking for some clarifications about any custom labels, or errors that can occur.

## Project Details
There are three major components that ALJI blends together: Expressive Writing, Machine Learning, and Human-Computer Interaction.

### Expressive Writing
Disclosure and reflection have had a fundamental role in many therapies to promote healing. Personal journals are an excellent way of promoting some degree of disclosure and reflection in the absence of a mental health professional. Clinical studies of expressive writing find that there are several health benefits that come at nearly zero cost <sup>1</sup> <sup>2</sup>. The additions that ALJI places on top of expressive writing may extend this further. For ALJI to act as a platform for expressive writing, it must first provide an acceptable space where authors can share deeply personal information. Transparency is the most direct way to build trust in software, so ALJI has been founded as an open-source project. This lets anyone view and scrutinize all portions of the software for any breaches of confidentiality. In addition, ALJI has been designed to never communicate over the internet, restricting ownership and access to solely the author of the personal journal.


### Machine Learning
Machine Learning is the use of computers to learn a task by finding patterns and inferring information, instead of following explicit instructions. As a very simple example: a computer can detect that the word ‘tired’ was used ten times in one journal and two times in another journal of a similar length. From this pattern, it may infer (without certainty) that the first journal author is more tired than the second. A computer could understand very natural language when equipped with a much larger vocabulary and a more nuanced interpretation. If you are curious to learn more about Machine Learning, these two short, enjoyable videos are informative: [​here](https://youtu.be/R9OHn5ZF4Uo) and [here](https://youtu.be/wvWpdrfoEv0). A longer, more detailed video about the inner mechanics (for one specific type of machine learning) can be found [here](https://youtu.be/aircAruvnKk). 

### Human-Computer Interaction
Interaction design has a great effect on the effectiveness of a program. ALJI’s communication with the journal author must be centered around improving their well-being through non-judgmental feedback. This feedback is critical, since it is the primary addition that ALJI uses to go beyond acting as a basic personal journal. To align with a typical personal journal as closely as possible, feedback is kept minimal during regular use. However, when a mental health crisis is detected and confirmed, then a response is given to the author guiding them towards clinical mental health support systems. This response will be carefully crafted by mental health professionals to encourage the author to contact these support systems.

## About Me
I am Patrick Sullivan, a graduate student within Virginia Tech’s Computer Science Department. I have a Bachelor’s in Computer Science along with a minor in Psychology. My research on the ALJI project is advised by Dr. Bert Huang (CS), Dr. Tanushree Mitra (CS), and Dr. Lee Cooper (Psych). There are four major passions that I have dedicated my life toward: teaching, computers, psychology, and music (in no particular order). I thoroughly enjoy mixing them together when I can.

> <sup>1</sup> Lepore, S. J. & Smyth, J. M. (2002). The writing cure: How expressive writing promotes health and emotional well-being. Washington, D.C.: American Psychological Association.

> <sup>2</sup> Pennebaker, J. W., & Chung, C. K. (2011). Expressive writing and its links to mental and physical health. In H. S. Friedman (Ed.), ​ _Oxford handbook of health psychology_ ​ (pp.417- 437). New York, NY: Oxford University Press.
