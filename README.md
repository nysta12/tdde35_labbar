# Computer Networks
Welcome to the repository of the Computer Networks courses!

[TDDE35: Large-Scale Distributed Systems and Networks](https://www.ida.liu.se/~TDDE35/labs/)

This course has 4 lab assignments:
* [Assignment 1: Wireshark lab. Getting started + HTTP](./lab1-wireshark)
* [Assignment 2: Net Ninny. A Web Proxy Based Service](./lab2-proxy)
* [Assignment 3: Transmission Control Protocol (TCP)](./lab3-tcp)
* [Assignment 4: Distance Vector Routing](./lab4-routing)

**Read this file till the end! Assignments that are handed in incorrectly will be automatically rejected.**

Assignment instructions could be found on the web-page of your course code (e.g. [TDDE35](https://www.ida.liu.se/~TDDE35/labs/)).
Additional submission and report requirements are located in the respected folders (e.g. [networks/lab1-wireshark](./lab1-wireshark), [networks/lab2-proxy](./lab2-proxy), etc.).


Submit solutions and reports into **your gitlab repository, which must be a *private* fork of the repository [nikko22/networks](https://gitlab.liu.se/nikko22/networks)**. A fork is essentially a copy of a repository that is cloned into your own account.

These instructions describe the process of i) creating such a forked repository and ii) handing in solutions via a repository.



## Getting started

### 0. Log into gitlab.liu.se with your LiU-ID

### 1. Fork the repository [nikko22/networks](.)

Press the "Fork" button on the top of this page to copy this repository to your account.

<img src="/clarifying_pictures/fork_image.png"  width="500">
---

Then, on the next page that pops up, choose your account:

<img src="/clarifying_pictures/fork2_image.png"  width="500">
---

After successfully forking the repository, you will see a message such as the following:

<img src="/clarifying_pictures/fork3_image.png"  width="500">
---

### 2. Make your fork private!

Your forked repository **must be made private** so that others do not have access to it.

Find the "Settings" button on the left of the page about your forked repository, and click 'General' to change the permissions for your project.

<img src="/clarifying_pictures/change_permission1.png"  width="500">

Expand 'Permissions', set 'Project visibility' to 'Private', and then save changes.

<img src="/clarifying_pictures/change_permission2.png"  width="500">

### 3. **Provide "Maintainer" access to your fork for your lab partner and for your lab assistant**

Find the "Settings" button on the left of the page about your forked repository, and click 'Members' to add people who can access your repository.

<img src="/clarifying_pictures/add_member1.png"  width="500">

Follow the steps as shown in the screenshot below to provide **"Maintainer"** access to your lab partner and to your lab assistant

<img src="/clarifying_pictures/add_member2.png"  width="500">


### 4. Work on the lab assignments

You may want to download the content of your repository to the computer at which you are working on the lab assignments. If you are familiar with git, this may be done by cloning the repository on the computer. Another, perhaps easier alternative is to simply use the download option on the page about your repository as illustrated in the following screenshot; this option allows you to download a package that you have to unpack.

<img src="/clarifying_pictures/download.png"  width="500">

After you have the content of your repository on your computer, you can start working on the lab assignments. Notice that the repository contains four folders, one for each of the four lab assignments. **Check these folders for more detailed instructions about what needs to be handed in for the corresponding lab assignment.**

### 5. Place your code and a report into the repository
After completing an assignment, edit/upload the files to your GitLab repository.

If there exists an example report in the directory (e.g., lab1-report.txt in the directory lab1), you may open and edit the file in the browser as illustrated in the following screenshot (of course, you may also use git to push updates to this file from your computer).

<img src="/clarifying_pictures/edit.png"  width="500">

If there is no such file in the directory, you may upload files from your computer into the directory as the following screenshot illustrates (or, again, you may use git).

<img src="/clarifying_pictures/upload.png"  width="500">

### 6. Submit by sending an email with a link to the repository
To submit a solution to your lab assignment, *email a link of your repository* to your lab assistant; the subject for that email *must* adhere to the following pattern: **CourseCode_Year_labNumber_userName1_userName2** 
(e.g., TDDE35_2020_lab4_hrsdv94_dgjjt92).

