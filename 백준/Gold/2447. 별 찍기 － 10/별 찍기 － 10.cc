#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>



void rec(int i,int j, int a)
{
	
	if ((i / a) % 3 == 1 && (j / a) % 3 == 1) {
		printf( " ");
	}
	else
	{
		if (a / 3 == 0)
			printf("*");
		else
			rec(i, j, a / 3);
	}


}



int main()
{

	int a;
	scanf("%d",&a);

	for (int i = 0; i < a; i++)
	{
		for (int j = 0; j < a; j++)
			rec(i,j,a);
		printf("\n");


	}


	







}
