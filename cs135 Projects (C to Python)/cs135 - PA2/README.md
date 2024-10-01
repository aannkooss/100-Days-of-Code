# ProgrammingAssignment2

## Project Goals
The goal of this project is to:
1.	Familiarize students with **selection**.
### Important Notes:
1.	**Formatting**: Make sure that you follow the precise recommendations for the output content and formatting. For your testing purposes, the autograder will be comparing your output to that of the example executable.
2.	**Comments**: Header comments are required on all files and recommended for the rest of the program. Points will be deducted if no header comments are included.
3.	**Filename**: Save your program as ```discount_flowers.c```

## Program
Which one will smell sweeter?  

We’re going to extend our program for managing flower orders to incorporate discounts for larger orders.  

**The program should behave as follows:**  
We’ll still be getting the customer’s number of flowers and we’ll also be getting the type of flower, which should be one of the following letters: R (for roses), I (for irises), or L (for lillies). We’ll do that for two different orders. For example (the highlighted part is what the program displays and the italicized part is the user input):  
```Flower Order 1 (#flowers type): ``` *3 R*

We want to reward customers for larger flower orders, so we'll be applying a discount to their overall orders. 

Finally, we need to let the user know which order is the cheapest or if they're the same cost.  

### Requirements
The starting price of each rose will always be $4.99. The starting price of each iris will always be $2.99. The starting price of each lily will always be $1.75. 

For every additional flower over 6, a 3% discount should be applied. For example, if the customer orders 8 roses then a 6% discount would be applied to the overall price. The discount should never be more than 50% off.  

The user should be prompted for a set of two values which represent the number of flowers and the flower type for the first order. The user should enter both values on one line, separated by spaces. The user should then be prompted for the remaining flower order.

### Example Program Execution:
***These are just a few example of how the program should run. Your program should be able to handle any input that is entered in the correct format.*** 

![flowers_discountExecutable1](https://user-images.githubusercontent.com/2504089/213605076-08560c8f-9f9c-4f3e-a198-5a5c0c9a050a.png)
  
![flowers_discountExecutable2](https://user-images.githubusercontent.com/2504089/213605081-0198a662-f925-4530-9d15-a56e9aa51e03.png)  

![flowers_discountExecutable3](https://user-images.githubusercontent.com/2504089/213605084-c56a7be5-54cc-4aea-b5cc-e6278520e308.png)

### Hints:
- Make sure you try out different test cases!
- Plan out your calculations and comparisons, then implement them in code.
- Play close attention to using scanf with variables.
- Make sure you control the formatting of any floating-point output.

## Submission details
To submit your project, you will have to use git on your VirtualBox installation:
1.	After accepting the assignment invitation, copy the clone URL
2.	Type 
```git clone clone URL```
3.	cd into your new assignment directory
4.	After working on your files
5.	When you’re ready, type the following commands: 
```
git add .
git commit -m “your commit message”
git push
```
## Academic Honesty
Academic dishonesty is against university as well as the system community standards. Academic dishonesty includes, but is not limited to, the following:
Plagiarism: defined as submitting the language, ideas, thoughts or work of another as one's own; or assisting in the act of plagiarism by allowing one's work to be used in this fashion.
Cheating: defined as (1) obtaining or providing unauthorized information during an examination through verbal, visual or unauthorized use of books, notes, text and other materials; (2) obtaining or providing information concerning all or part of an examination prior to that examination; (3) taking an examination for another student, or arranging for another person to take an exam in one's place; (4) altering or changing test answers after submittal for grading, grades after grades have been awarded, or other academic records once these are official.
Cheating, plagiarism or otherwise obtaining grades under false pretenses constitute academic
dishonesty according to the code of this university. Academic dishonesty will not be tolerated and
penalties can include cancelling a student’s enrolment without a grade, giving an F for the course, or for the assignment. For more details, see the University of Nevada, Reno General Catalog.
