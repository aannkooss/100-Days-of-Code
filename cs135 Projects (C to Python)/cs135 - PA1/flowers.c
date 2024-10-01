//Ankush Joshi 
//February 12, 2023
//Project 1 - Flowers Table 

#include <stdio.h>

int main(){
	
	int quantity1, quantity2, quantity3; //User input for number of flowers
	double price1, price2, price3;       //User input for price of flowers
	char color1, color2, color3;         //User input for color of flowers

	//This section provides a "catalog" of options so the user knows what values to type in and then prompts the
	//user to start filling out their order with the desired otptions
	printf("Welcome to the Flower Shop!\n");
	printf("Here is a list of all the flowers we have in stock! Feel free to take a look and order whenever you're ready\n");
	printf("|**\\OUR FLOWERS/**|\n");
	printf("--Rose: $1.49 | Color: R | IN STOCK--\n");
	printf("--Iris: $1.99 | Color: V | IN STOCK--\n");
	printf("--Lily: $2.50 | Color: O | IN STOCK--\n");

	printf("\nAll set? To order, please enter the color of the flower you would like, the amount, and price per unit for three different flowers below!\n");
	
	//This section begings the user input and tells the user how to type in their order using the price, color and
	//quantity values. It also prompts the user to follow a "formula" and provides directions to typing in their order
	printf("\nLet's start with your first flower:\n");
	printf("(Please write it in the format: Amount Price Color - Please also keep in mind to omit the '$' sign when typgin the price and write the corresponding values for color and price)\n");
	printf("Roses: ");
	scanf("%d %lf %c", &quantity1, &price1, &color1); //Prompts the user to input values using the table + what they want
	printf("Nice! Now do the same for two more flowers: \n");
	printf("Irises: ");
	scanf("%d %lf %c", &quantity2, &price2, &color2); //Prompts the user to input values using the table + what they want
	printf("Lillies: ");
	scanf("%d %lf %c", &quantity3, &price3, &color3); //Prompts the user to input values using the table + what they want

	//This section summarizes the user's order in the previous section and puts it in a "list" format
	printf("\nAwesome! Now let's get your roder sheet made! This part's on us, don't worry!\n");
	printf("\n/**\\FLOWER SHOP ORDER/**\\\n");
	printf("Roses (#flowers price color): %d %.2lf %c \n", quantity1, price1, color1); //Brings information from last section together
	printf("Irises (#flowers price color): %d %.2lf %c \n", quantity2, price2, color2);
	printf("Lillies (#flowers price color): %d %.2lf %c \n", quantity3, price3, color3);

	//Takes all the information provided and organizes everything into a table and calculates total values
	printf("\n     /**\\FLOWER SHOP TOTAL/**\\ \n");
	printf("===========================================\n");
 	printf("| FLOWER | COLOR | QUANTITY | PRICE TOTAL |\n");
	printf("-------------------------------------------\n");
	printf("| ROSE   |   %c  |    %d     |    $%-4.2lf      |\n", color1, quantity1, quantity1*price1); //Grabs values for color and quantity for the respective flower and then calculates total in the last column
	printf("-------------------------------------------\n");
	printf("| IRIS   |   %c  |    %d     |    $%-4.2lf      |\n", color2, quantity2, quantity2*price2);
 	printf("-------------------------------------------\n");
	printf("| LILY   |   %c  |    %d     |    $%-4.2lf      |\n", color3, quantity3, quantity3*price3);
	printf("===========================================\n");
	printf("|TOTAL FOR CUSTOMER'S ORDER |    $%-.2lf  |\n", quantity1*price1+quantity2*price2+quantity3*price3); //Calculates total price of the flowers by adding the multiplicative values of everything
	printf("===========================================\n");

	return 0;
}
