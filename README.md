# Database Technology course
Hi and welcome to the course in databases!
This repo is structured like the labs should be handed in.
If any instructions are unclear please create an Issue and assign Alexander Dahl (aleda145) to it.

## The labs
This course has 4 labs. The first two are introductions to MySQL and database design.

Lab 3 is about functional dependencies.

And lab 4 is a bigger project where everything you've learned in the three previous labs will be used.

## Lab instructions
The lab compendium is available on the course webpage. 

In this repo there are four folders, each corresponding to a lab.

**Check the folders for hand in instructions for each lab**


## Gitlab
All labs should be handed in through gitlab.ida.liu.se. 
Create a new project in gitlab and name it "Course Code_liu_id 1_liu_id 2". So for the course TDDD37 and your LiU IDs are aleda145 and aleda146 name your repo "TDDD37_aleda145_aleda146".
After a project has been created click "members" under options in the top right corner. 
Add your lab assistant as a developer in the members tab.

<img src="/clarifying_pictures/members.jpg"  width="300">


### Handing in labs
**Labs do not need to be demonstrated during the lab session**. The lab sessions are for helping, not examination. 

When you have completed a lab and confirmed that everything is according to the corresponding lab instructions in gitlab you can hand it in.
Labs that are handed in incorrectly will be denied and your assistant will ask for a correctly done hand in. 

You hand in the labs by creating an issue, specifying which lab you are handing in and then assigning your lab assistant to the issue.
When your lab assistant has looked at the lab, the feedback will be put on WebReg and you will get an email to your student email about it. The issue will also be closed. 

<img src="/clarifying_pictures/issue.jpg"  width="300">

### When you need help
Create an issue and assign your lab assistant and describe your problem. A good description will result in better help!
If you have question about the course in general or if you can't make it to a mandatory seminar you should email your lab assistant.

## How to use git
There are numerous guides online how to use git, but what follows is a basic guide to get started.

After you have created a new gitlab repo start by:

Cloning your project to your machine using the terminal. example: `git clone git@gitlab.ida.liu.se:aleda145/TDDD37_aleda145_aleda146.git` 

Code!

Add your changes to git with `git add lab1.sql` (type git status to see which files you've changed)

Write commit message by `git commit -m "good thoughtful commit message"`

Push the code when you're done with your coding session `git push -u origin master`


How you use branches, commit messages etc. is not part of the examination. Do as you please, but it is recommended to write good and thoughtful commit messages for lab 4 so you don't forget what you've done. 


