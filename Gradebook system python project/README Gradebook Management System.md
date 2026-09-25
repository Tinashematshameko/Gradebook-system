Gradebook Management System- Python project

Name: Tinashe Laone Matshameko

The program allows the user to manage students across multiple subjects, calculate averages, search and sort students, handle incorrect inputs properly and showcase the evolution to an OOP design from a procedural design. It evolves from stage A to F

How to run 

Save the file in a desired name e.g.. gradebook_system.py
Open the file in an IDE
Run the program

Brief description of section A to F

Section A
The program allows user to enter number of students and uses a for loop to ask each of those students  their names and grades of just one subject. It also calculates the total grade and average for the class and also displays each name, grade for each student and overall class average. Validation checks are in place to make sure they enter valid grades and the program will encourage them to re enter a valid grade if they enter an invalid grade


Section B
The program can now handle multiple grades per student now by using lists  it can now store and receive grades for different subjects and also display a student's name and grades using a tuple
It can now also find and display the highest and lowest grade for each subject and display the average grade, name and grades for each student across all subjects


Section C
Dictionaries have been used to replace tuples and  to store student names and their grades and the program can now add new students, update existing grades and remove students. They are also used to store the grades of a subject as well
Users now have the option search for a specific student using their name and get all their grades and averages, they can also view grades for specific subject as well

Section D
The entire code has been broken down into functions that perform a single task e.g. displaying results, adding students, getting grades etc. .
The functions are broken down in a way that it can be reused throughout the program to do different things e.g. adding math and science grade with the same function
It is now possible to search for a student and update their grades as well by using a function now and all possible errors that could crash program like invalid inputs and students that don't exist are gracefully handled and will still execute after the error has happened by raising errors like value error etc.

Section E 
There is a student class that has the student's name and their grades along with methods for adding, calculating the average and printing out student details as well

There is also a gradebook class that also has the student's name and their grades along with methods for adding, removing and searching for students. It also has the ability to also sort students by their average grade and by specific subjects

Both classes and their methods have been tested to make sure that they work as expected on their own and together as one 


Section F
Testing and documentation are provided in the comments
There is use of a sorting algorithm (bubble sort) and one can search for students using their name and average grade 
There is successful implementation of exception handling through use of custom exceptions as well the program does not crash and can handle errors gracefully Abd still execute after the error occurred 

Example input and output

Input

Enter student name: Bob
Enter Maths grade: 67
Enter English grade: 87
Enter science grade: 56

Output

Students sorted by  subject:
Bob - Maths: 67
Kirk - Maths: 46
Andrew - Maths: 27

Trying to remove a student that is not there
Student "Randy" was not found




Assumptions and limitations

students have exactly 3 subjects
grades are between 0 and 100
No database storage as data is lost after the program ends
It is console based
