The Innovation University of Australia (IUA) wants to allow a lecturer to enter the marks of a number of students (instead of just a single student) and store the information permanently in a text file on their computer. They also want to allow a lecturer to search details of a student in the text file by the student ID.

The main program should first display a menu as follows. A lecturer needs to select an operation from the main menu.

================================================
Welcome to the AGoS System of IUA

Please select an option from the following.
<A>dd details of a student.
<S>earch student details for a student.
<Q>uit.

================================================

If a lecturer chooses the option <A> the program then asks them to enter a student’s ID, name, and the Assignment 1, Assignment 2 and Final Exam mark one by one. Once all marks for a student are entered it will display the student ID, name, weighted mark for each assignment, the total weighted mark of the assignments, weighted mark for the Final Exam, total weighted mark of the subject, bonus mark and total mark with bonus.

The system will then ask the lecturer 'Do you want to enter marks for another student (Y/N)?' If they enter 'Y' the system will allow them to enter details and marks for another student as before, if they enter 'N' the system will display the main menu again, otherwise it will ask the same question again.

A typical example of the display of the program (once a lecturer chooses the option <A>) can be as follows. Your program MUST follow the same display style.

-----------------------------------------------------------------------------------------
The Innovation University of Australia (IUA) Grade System
-----------------------------------------------------------------------------------------
Please enter all marks out of 100.

Please enter the student ID: 1111
Please enter the student name: Alice Furner
Please enter the marks for Assignment 1: 80
Please enter the marks for Assignment 2: 90
Please enter the marks for the Final Exam: 74

Thank You!

Weighted mark for Assignment 1: 16
Weighted mark for Assignment 2: 27
Total weighted mark of the assignments: 43

Weighted mark for the Final Exam is: 37
Total weighted mark for the subject: 80

Bonus mark: 3.5
Total mark with bonus: 83.5

Do you want to enter marks for another student (Y/N)? z
Do you want to enter marks for another student (Y/N)? Y

Please enter the student ID: 1112
Please enter the student name: Bob Siers
Please enter the marks for Assignment 1: 68
Please enter the marks for Assignment 2: 68
Please enter the marks for the Final Exam: 92

Thank You!

Weighted mark for Assignment 1: 13.6
Weighted mark for Assignment 2: 20.4
Total weighted mark of the assignments: 34

Weighted mark for the Final Exam: 46
Total weighted mark for the subject: 80

Bonus mark: 3.5
Total mark with bonus: 83.5

Do you want to enter marks for another student (Y/N)? N

================================================
Welcome to the AGoS System of IUA
Please select an option from the followings.
<A>dd details of a student.
<S>earch student details for a student.
<Q>uit.
================================================

The system will also store the details and marks of each student in a file called IUA.txt in the same folder as the Python code of the AGoS system. Every time a student's details are entered the system should append them in the text file.

For example, the IUA.txt file will have the following content after the details of Alice Furner are entered.

 

However, the file content will be as follows after the details of Bob Siers are entered.

If a lecturer chooses the option <S> from the main menu then the program asks the lecturer to enter the student number for whom they want to see details. To facilitate the search option you need to use an appropriate data structure such as List. The program then collects the student details from the IUA.txt file and displays it as follows (assuming the following student was searched for).

After displaying the student information the program prompts the lecturer with the following message, 'Do you want to search for another student (Y/N)?' If a lecturer enters 'Y' then the program asks them to enter the student number for whom the information needs to be searched and displayed, else if the lecturer enters 'N' then the program displays the main menu, otherwise the program prompts the same message again.

Finally, the program quits if the user chooses the option < Q>.

You need to develop the system by completing the following three tasks::


Instructions to follow.

1.Use the concepts: Exceptions and logging and oops.
2.Follow the modular approach.
3.Write at least 5 unit test cases.
4.Write proper comments.
5. pep8 error free code.
6. Pylint grade > 8.5

Give two solutions.
1. Using files 
2. Use postgres database for storage media