//Ankush Joshi 
//March 3, 2023 
//Project 3 - Menu Functions 

//Menu Function Program 

#include <stdio.h>
//declaring varables
void menuchoice();
int numbercount(); 
int triangleinput();

//function for menu choice and prompt for user input
void menuchoice(){
	char choice; //declaring variable for menu function
   	printf("\nMENU\n");
   	printf("(N)umbers\n");
   	printf("(D)raw\n");
   	printf("E(X)it\n");
   	printf("Please Enter the character of your selection: ");
	}

//function for number count 
int numbercount(){
	
	int number, i, size, row, column, space;//declaring variables for number function
	do{
        int count = 0;
        printf("Please enter a number (0 to stop): ");
        scanf(" %d", &number); //user input for numbers
        
	if(number != 0){
            for(i = number; i > 0; i /= 10){
                count++;
            }
            printf("%d has %d digits \n", number, count);
        }
        else{
            return 0;
            
        }
    }while(number != 0); //repeats code until user inputs 0
    
}   
    
//function for creating a triangle    
int triangleinput(){
    int trianglesize, row, space, star; //declaring variables for triangle function
    
	printf("Please enter a size larger than 2: ");
	scanf("%d", &trianglesize);
	for(row = 1; row <= trianglesize; row++){
		for (space=1; space <= (trianglesize-row); space++)
			printf(" "); 
		for(star=1; star <= ((2*row)-1); star++){
			printf("*"); 
		}
			printf("\n");	
	}
    }

//main function
int main()
{
    char choice;
    int number, i, size, row; //declaring variables for main function
    
    do{
        menuchoice();
        scanf(" %c", &choice); //user input for choice
        
        switch(choice){ //switch case for user input
            case 'N':
            case 'n':
                numbercount();
                break;
            case 'D':
            case 'd':
                triangleinput();
                break;
            case 'x':
                choice = 'X';
            case 'X':
                printf("Thanks for participating! Exiting Program now... \n");
        }
    } while (choice != 'X'); //repeats code until user inputs x or X
    return 0;
}



