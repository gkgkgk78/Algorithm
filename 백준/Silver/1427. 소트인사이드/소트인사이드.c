#pragma warning(disable:4996)

#include<stdio.h>
#include<stdlib.h>


int main()
{
    int input;
    scanf("%d", &input);
    int ary[10]={ 0, };
    while (input > 0) {
        ary[input % 10]++;
        input /= 10;
    }
    for (int i = 9; i >= 0; i--)
    {
        if (ary[i] != 0)
        {
            while (ary[i] > 0)
            {
                printf("%d",i);
                ary[i]--;


            }


        }



    }
    printf("\n");
	


}