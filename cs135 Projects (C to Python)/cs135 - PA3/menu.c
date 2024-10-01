//Ankush Joshi 
//February 26, 2023 
//Project 3

//Menu Program 

#include <stdio.h>

int main() 
{
	char choice; //initializing variables 
	int number,count, i, trianglesize, row, space, star;

	do {
	printf("\nMENU\n"); //presenting menu and options to user
	printf("(N)umbers\n");
	printf("(D)raw\n");
	printf("E(X)it\n");
	printf("Please Enter the character of your selection: ");
	scanf(" %c", &choice); //user input for choice

	switch (choice) { //switch statement that determines user's path based on previous input
	case 'N': //case for N or n input from user
	case 'n':
		do{
			printf("Please enter a number (0 to stop): ");
			scanf("%d", &number); //user input for number 
			if(number != 0) {
			    count = 0;
			    for (i = number; i > 0; i /= 10) {
				    count++;
			    }
			    printf("%d has %d digits \n", number, count);
		    }
	    }while (number != 0); //repeats code until user inputs 0
	    break;

	case 'D': //case for D or do input 
	case 'd':
		printf("Please enter a size larger than 2: ");
		scanf("%d", &trianglesize);
		for(row = 1; row <= trianglesize; row++){
			for (space=1; space <= (trianglesize-row); space++)
				printf(" "); //prints spaces to align triangle
		for(star=1; star <= ((2*row)-1); star++){
				printf("*"); //prints asterisks for triangle shape
				}
				printf("\n");	
				}
		break;
	    case 'x':{ //defaults lowercase x to X for exit statement
		choice = 'X';
	    }
	    case 'X':{ //case for X to exit code 
		    printf("Thank you for participating! Exiting Program now\n");
	    }		
	    } 
    }while (choice != 'X'); //loops code until an X or x is inputted

return 0;
}


