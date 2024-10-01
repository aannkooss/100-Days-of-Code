//Ankush Joshi 
//March 12, 2023 
//Programming Assignment 5 - Complex Number Calculator 

#include <stdio.h>

//Declaring function names
void menuchoice();
void complexnumberinput(double* real, double* imaginary);
void addition(double real1, double imaginary1, double real2, double imaginary2, double* RealOutput, double* ImaginaryOutput);
void subtraction(double real1, double imaginary1, double real2, double imaginary2, double* RealOutput, double* ImaginaryOutput);
void multiplication(double real1, double imaginary1, double real2, double imaginary2, double* RealOutput, double* ImaginaryOutput);

//main function code
int main(){
	//do while loop for user input
	do{
	//declaring variables for main function
	char choice;
	double real1, imaginary1, real2, imaginary2, realanswer, imaginaryanswer;		
		menuchoice();
		scanf(" %c", &choice);	
	
		//switch case to conduct arithmetics based on user input
		switch(choice){
			//switch case for addition
			case 'A':
			case 'a':
				complexnumberinput(&real1, &imaginary1);
				complexnumberinput(&real2, &imaginary2);
				addition(real1, imaginary1, real2, imaginary2, &realanswer, &imaginaryanswer);
				printf("\nComplex SUM: %.2lf + %.2lfi\n", realanswer, imaginaryanswer);
			break;
			
			//switch case for subtraction
			case 'S':
			case 's':
				complexnumberinput(&real1, &imaginary1);
				complexnumberinput(&real2, &imaginary2);
				subtraction(real1, imaginary1, real2, imaginary2, &realanswer, &imaginaryanswer);
				printf("\nComplex DIFFERENCE: %.2lf + %.2lfi\n", realanswer, imaginaryanswer);
			break;
			
			//switch case for multiplication
			case 'M':
			case 'm':
				complexnumberinput(&real1, &imaginary1);
				complexnumberinput(&real2, &imaginary2);
				multiplication(real1, imaginary1, real2, imaginary2, &realanswer, &imaginaryanswer);
				printf("\nComplex PRODUCT: %.2lf + %.2lfi\n", realanswer, imaginaryanswer);
			break;

			//switch case to exit code - if user inputs 'x', it will switch to 'X'
			case 'x':
				choice = 'X';
			case 'X':
				printf("Exiting program now...\n");
			return 0;
			break;
		}
	}while (1 == 1);	

return 0;
}
//menu choice function that gives user choices
void menuchoice(){
	char choice();
	printf("\nCOMPLEX NUMBER CALCULATOR\n");
	printf("(A)dd\n");
	printf("(S)ubtract\n");
	printf("(M)ultiply\n");
	printf("E(X)it\n");
	printf("Please enter the character of your selection: ");
}

//complex number function for real and imaginary number user input
void complexnumberinput(double* real, double* imaginary){
	printf("Enter the real part of your complex number: ");
	scanf(" %lf", real);
	printf("Enter the imaginary part of your complex number: ");
	scanf(" %lf", imaginary);


}
//function for addition
void addition(double real1, double imaginary1, double real2, double imaginary2, double* RealOutput, double* ImaginaryOutput){
	
	*RealOutput = real1 + real2;
	*ImaginaryOutput = imaginary1 + imaginary2;
}

//function for subtraction
void subtraction(double real1, double imaginary1, double real2, double imaginary2, double* RealOutput, double* ImaginaryOutput){
	
	*RealOutput = real1 - real2;
	*ImaginaryOutput = imaginary1 - imaginary2;
}

//function for multiplication
void multiplication(double real1, double imaginary1, double real2, double imaginary2, double* RealOutput, double* ImaginaryOutput){

	*RealOutput = ((real1 * real2) - (imaginary1 * imaginary2));
	*ImaginaryOutput = ((real1 * imaginary2) + (real2 * imaginary1));
}

