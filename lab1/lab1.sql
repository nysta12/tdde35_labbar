/*
Lab 1 report <Student_names and liu_id>

All non code should be within SQL-comments /* like this */ 


/*
Drop all user created tables that have been created when solving the lab
*/

DROP TABLE custom_table;


/* Have the source scripts in the file so it is easy to recreate!*/

SOURCE company_schema.sql;
SOURCE company_data.sql;

/*
Question 0: Print a message that says "hello world"
*/

SELECT 'hello world!' AS 'message';

/* Show the output for every question.
+--------------+
| message      |
+--------------+
| hello world! |
+--------------+
1 row in set (0.00 sec)
*/ 
