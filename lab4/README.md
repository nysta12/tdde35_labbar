# Lab 4 

Lab 4 is a big project that contains different parts. 

## Part 1
For the first part the following should be handed in:

* EER-diagram
* Relational Model
* Functional dependencies for all relations

### EER-diagram and Relational Model
Same as in lab 2, do it in draw.io and add it to gitlab

### Functional depdencies 
Find the Candidate keys, primary keys and whether the table is in BCNF or not. If it is not in BCNF, motivate why! 

## Part 2
This is the coding phase of the project. Do not start coding until your EER and RM is approved!

The following should be handed in: 

* EER-diagram 
* Relational Model 
* Functional dependencies for all relations
* Project code as a file named lab4.sql
* Answers to the non code questions as comments in the lab4.sql file, place them at the end of the file
* An identified secondary index as a comments in the lab4.sql file (do not implement it), place at the end of the file

### Code
Please delete all your created tables and views in the beginning of the file!

You can do this by temporarily disabling Foreign Keys in MySQL. Do not forget to enable it again!

`
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE XXX;
SET FOREIGN_KEY_CHECKS=1;`

## Part 3
Is just sending in the code to urkund. Change the file ending from lab4.sql to lab4.txt! Send it to urkund when you have passed lab4c) on WebReg! Details are on course website.


