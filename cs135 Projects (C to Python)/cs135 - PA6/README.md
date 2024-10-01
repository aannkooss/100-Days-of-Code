# ProgrammingAssignment6

## Project Goals
The goal of this project is to:
1. Provide students with continued practice with **modularization**
2. Familiarize students with the use of **File IO**
### Important Notes:
1.	**Formatting**: Make sure that you follow the precise recommendations for the output content and formatting. For your testing purposes, the autograder will be comparing your output to that of the example executable.
2.	**Comments**: Header comments are required on all files and recommended for the rest of the program. Points will be deducted if no header comments are included.
3.	**Filename**: Save your program as ```sandwich_order.c```
## Program
*This is the way* to Mando's Sandos!  

Write a program for a sandwich ordering system. The program should get a single sandwich order from the ```sando.txt``` file that is already in this repository. It should save the receipt to a ```receipt.txt``` file.

## Requirements
In addition to the main function, there must be 2 additional functions: one to get the order from the order file and one to save the receipt to a different file. 

All opening and closing of files **must be done in the main function**. 

**TIPS!**
- Nothing should display to the screen when you run your program!
- You can open the order file and change the order with gedit!
  - As you're finishing up your program, you should change the values in the file to test that your program works for different orders!
- Open the receipt file with gedit to see what your program saved (or use the ```cat``` command in the terminal)!
- Sales tax in Washoe County is 8.27%.
- My program included 3 more functions for calculating the sandwich price, the order subtotal, and the order total.

### Input File Format
The order input file is called ```sando.txt``` and is included in this repository. It already contains an order in the following format.
```
H 6
Y
M
12
```
- the first line contains the sandwich information (type and size)
  - 6 inch sandwiches cost $6.99
  - 12 inch sandwiches cost $9.99
  - 'C' is for cold sandwiches
  - 'H' is for hot sandwiches, and they cost $1.50 extra!
- the second line contains whether or not the order includes chips
  - 'Y' is for chips, they cost $1.99
  - 'N' is for no chips
- the third line is the size of the drink
  - 'S' is for a small drink, they cost $0.99
  - 'M' is for a small drink, they cost $1.99
  - 'L' is for a small drink, they cost $2.99
- the fourth line is the tip amount
  - this should be a whole number representing the percent
  - it can be 0!

### Output File Format
The receipt output file should be called ```receipt.txt```. 
If your program is run with the inital values in the order file, your receipt file should have the following format:
```
*****Your SANDIWCH Order******
6 inch HOT sandwich: $8.49
CHIPS: $1.99
MEDIUM drink: $1.99
______________________________
SUBTOTAL: $12.47
plus 8.27% tax and 12% tip
==============================
the TOTAL is $15.00
```
### More Testing!
If you change the order to:
```
C 12
N
L
0
```
then your receipt should look like this:
```
*****Your SANDIWCH Order******
12 inch COLD sandwich: $9.99
LARGE drink: $2.99
______________________________
SUBTOTAL: $12.98
plus 8.27% tax and 0% tip
==============================
the TOTAL is $14.05
```
Keep testing with different values!  

## Submission details
To submit your project, you will have to use git on your VirtualBox installation:
1.	After accepting the assignment invitation, copy the clone URL
2.	Type 
```git clone clone_URL```
3.	cd into your new assignment directory
4.	After working on your files
5.	When you’re ready, type the following commands: 
```
git add .
git commit -m “a descriptive message!”
git push
```
## Academic Honesty
Academic dishonesty is against university as well as the system community standards. Academic dishonesty includes, but is not limited to, the following:
Plagiarism: defined as submitting the language, ideas, thoughts or work of another as one's own; or assisting in the act of plagiarism by allowing one's work to be used in this fashion.
Cheating: defined as (1) obtaining or providing unauthorized information during an examination through verbal, visual or unauthorized use of books, notes, text and other materials; (2) obtaining or providing information concerning all or part of an examination prior to that examination; (3) taking an examination for another student, or arranging for another person to take an exam in one's place; (4) altering or changing test answers after submittal for grading, grades after grades have been awarded, or other academic records once these are official.
Cheating, plagiarism or otherwise obtaining grades under false pretenses constitute academic
dishonesty according to the code of this university. Academic dishonesty will not be tolerated and
penalties can include cancelling a student’s enrolment without a grade, giving an F for the course, or for the assignment. For more details, see the University of Nevada, Reno General Catalog.
