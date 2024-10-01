//Ankush Joshi 
//12 April, 2023
//Programming Assignment 7 - Arrays and File IO

//Sandwich Orders!

#include <stdio.h>
#define FILE_NAME "subwarray.txt" //defining file names macros
#define RECEIPT "receipt.txt" 

void read(FILE*, char[], char[], char[], int[], int[], int[]); //defining function for read file
void write(FILE*, char[], char[], char[], int[], double, double[], double[], int); //defining function for write file

int main(){
	char temp, chips, drinksize;
	int size, tip, ordersize;
	double price = 0, tax = 0.0827;  
//variable names and types 	
	
	fscanf(fp, " %d %d", &ordersize, &tip); //gets and stores ordersize value as well as tip

	FILE *fp; //file pointer
	fp = fopen (FILE_NAME, "r");
	if (fp == NULL){ //if statement if file is not available
    	printf("Can't open file");
    	return 0;
	}
    
	read(fp, temp, chips, drinksize, size, tip);
	fclose(fp);

	fp = fopen (RECEIPT, "w"); //opens receipt file
	if (fp == NULL){
    	printf("Can't open file");
    	return 0;
	}
    
	write(fp, temp, chips, drinksize, size, tip, price, tax); //calls write function for receipt file
	fclose(fp);
	return 0;
}

void read(FILE* fp, char[] temp, char[] chips, char[] drinksize, int[] size, int[] tip, int[] ordersize){ //sando file function
    
    for(int i = 0; i <= ordersize, i++){ //loops until i exceeds ordersize value 
        fscanf(fp, " %c %d\n%c \n%c", &temp[i], &size[i], &chips[i], &drink[i]);
    }
}
void write(FILE* fp, char temp, char chips, char drinksize, int size, double tip, double price, double tax, int ordersize){ //receipt file function
    
	double tipamount = 0; //sets initial ip amount to 0 
    
	fprintf(fp, "*****Your SANDIWCH Order******\n%d inch", size);

for(i = 0, i<ordersize, i++){ //loops until i exceeds ordersize
	switch(temp[i]){ //switch statements for temperature
    	case 'H':
    	fprintf(fp, " HOT");
        	price += 1.5;    
    	break;
    	case 'C':
    	fprintf(fp, " COLD");
    	break;
	}
	switch(size[i]){ //switch statements for sandwich size and price
    	case 6:
        	price += 6.99;
    	break;
    	case 12:
        	price += 9.99;
    	break;
	}
	fprintf(fp, " sandwich: $%.2lf", price); //prints sandwich price 
 
	switch(chips[i]){ //switch statements for chips
    	case 'Y':
    	fprintf(fp, "\nCHIPS: $1.99");
        	price += 1.99;
    	break;
    	case 'N':
    	break;
	}
    
	double priced = 0; //variable for drink price
	switch(drinksize[i]){ //switch statements for drink choice 
    	case 'S':
    	fprintf(fp, "\nSMALL ");
        	priced = 0.99;
        	price += 0.99;
    	break;
    	case 'M':
    	fprintf(fp, "\nMEDIUM ");
        	priced = 1.99;
        	price += 1.99;
    	break;
    	case 'L':
    	fprintf(fp, "\nLARGE ");
        	priced = 2.99;
        	price += 2.99;
    	break;
	}   
}    
   
    
	fprintf(fp, "drink: $%.2lf \n______________________________\nSUBTOTAL: $%.2lf", priced, price); //prints drink price and total price
    
	tipamount = price*tip/100;
	price = price + price * tax;
	price = price + tipamount;
//calculates total price after tax and tip
    
	fprintf(fp, "\nplus 8.27%c tax and %d%c tip\n==============================\nThe TOTAL is $%.2lf",'%', tip, '%', price); //prints final price as well as tip 
}
	
