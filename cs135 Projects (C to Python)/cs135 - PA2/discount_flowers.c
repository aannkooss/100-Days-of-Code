//Ankush Joshi
//18 February, 2023 
//Project 2 - Flower Discount

#include <stdio.h>

int main ()
{
//declaring variables for # of flowers, color, price, and discount
	int numflowers1, numflowers2; 
	char color1, color2;
	double flowerprice1, flowerprice2, saleprice1, saleprice2, discountprice1, discountprice2, total1, total2, bestdeal;
	float discount = 0.03;

//Greeting the user and showing "menu" to base responses off of
	printf("Welcome back to the Flower Shop!\n");
	printf ("Today's your special day! We are having a special deal where every flower you buy over 6 flowers, earns you a 3 percent Discount!\n");
	printf ("Here is a list of all the flowers we have in stock! Feel free to take a look and order whenever you're ready!\n");
	printf ("|**\\OUR FLOWERS/**|\n");
	printf ("--Rose: $4.99 | Color: R | IN STOCK--\n");
	printf ("--Iris: $2.99 | Color: V | IN STOCK--\n");
	printf ("--Lily: $1.75 | Color: O | IN STOCK--\n");

//Prompts user to fill out their order using the information above
	printf ("\nAll set? To order, please enter the amount and color of the flower you would with a space in between below!\n");
	printf ("Example: If you want 3 red flowers, you would enter - 3 R\n");
	scanf ("%d %c", &numflowers1, &color1); //prompts user to provide # and color of flowers
	printf ("Good Selection! Now for the next order: \n");
	scanf ("%d %c", &numflowers2, &color2);

//Creates order sheet with the information from above =
	printf ("\nAwesome! Now Let's get your order sheet made!\n");
	printf ("\n/**\\FLOWER SHOP ORDER/**\\\n");
	printf ("Flower Order 1 (#flowers type): %d %c \n", numflowers1, color1); //tells user short summary of their order using variables they provided
	printf ("Flower Order 2 (#flowers type): %d %c \n", numflowers2, color2);

//switch statement for connecting prices with user input of flower type for first flower
	switch (color1)
    	{
		case 'R': //if User inputs 'R' when prompted, it would grab the R flowerprice for calculation at the end
			flowerprice1 = 4.99;
			break;
		case 'V': 
			flowerprice1 = 2.99;
			break;
		case 'O':
			flowerprice1 = 1.75;
	}
//switch statement for connecting prices with user input of flower type for second flower
	switch (color2)
	{
		case 'R': 
			flowerprice2 = 4.99;
			break;
		case 'V':
			flowerprice2 = 2.99;
			break;
		case 'O':
			flowerprice2 = 1.75;
	}
 
//conditional statements for calculating final price and discount price (if applicable) 
	if (numflowers1 <= 6) //calculates price if user input flowers less than or equal to 6
    	{
        	saleprice1 = numflowers1 * flowerprice1;
        	total1 = saleprice1;
    	}
	else if (numflowers1 > 6) //calculates price with discount if user input flowers more than 6
   	{
        	saleprice1 = (flowerprice1 * numflowers1);
       		discountprice1 = ((numflowers1 - 6) * discount);
       		if (discountprice1 >= 0.5){ //sets 0.5 limiter on the discount and determines which case to use
       		    discountprice1 = 0.5;
       		}
       		else if (discountprice1 < 0.5){
       		    discountprice1 = (numflowers1 - 6) * discount;
       		}
        	
        	total1 = saleprice1 - (saleprice1 * discountprice1);
   	}

//conditional statements for calculating final price and discount price (if applicable) 
	if (numflowers2 <= 6) //calculates price if user input flowers less than or equal to 6
    	{
        	saleprice2 = numflowers2 * flowerprice2;
        	total2 = saleprice2;
    	}
	else if (numflowers2 > 6) 
   	{
        	saleprice2 = (flowerprice2 * numflowers2);
       		discountprice2 = ((numflowers2 - 6) * discount);
       		if (discountprice2 >= 0.5){ 
       		    discountprice2 = 0.5;
       		}
       		else if (discountprice2 < 0.5){
       		    discountprice2 = (numflowers2 - 6) * discount;
       		}
        	
        	total2 = saleprice2 - (saleprice2 * discountprice2);
   	}

//creates order sheet table using the calculations above and user input from section before
  printf ("\n   /**\\ FLOWER SHOP ORDERS /**\\ \n");
  printf ("==================================== \n");
  printf ("| FLOWERS | QUANTITY | PRICE TOTAL |\n");
  printf ("------------------------------------\n");
  printf ("|   %-c     |   %-d     |    $%-3.2lf   |\n", color1, numflowers1,
	  total1);
  printf ("------------------------------------\n");
  printf ("|   %-c     |   %-d     |    $%-3.2lf   |\n", color2, numflowers2,
	  total2);
  printf ("==================================== \n");

//conditional statements for determining which flower gives the better deal
  if (total1 < total2)//conditional statement telling the user the first deal is better
    {
      printf ("The %c flower order for %d is the better deal: $%.2lf", color1,
	      numflowers1, total1);
    }
  else if (total1 > total2)//conditional statement telling the user the second deal is better
    {
      printf ("The %c flower order for %d is the better deal: $%.2lf \n",
	      color2, numflowers2, total2);
    }else if(total1 == total2)//conditional statement telling the user both deals are the same
    {
        printf("These flowers are equivalent, you choose!");
    }
  return 0;
}
