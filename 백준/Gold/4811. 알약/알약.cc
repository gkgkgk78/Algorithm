#define _CRT_SECURE_NO_WARNINGS
#define size 32
#define size1 1001
#include<stdio.h>
#include<stdlib.h>



long long dp[size][size];//데이터 넣어줌

int arr[size1];

	
int main() {

	int a;
	int i = 0;

	//freopen("input.txt", "rt", stdin);

	scanf("%d", &a);
	arr[i] = a;
	i++;
	while (a !=0)
	{	
		scanf("%d", &a);
		if (a != 0) {
			arr[i] = a;
			i++;
		}

	}
	for (int h2 = 0; h2 <= 30; h2++)
	{
		for (int h1 = 0; h1 <= 30; h1++)
		{

			if (h1 >=h2) {				
				if (h2 == 0)
					dp[h1][h2] = 1;

				else
				{
					dp[h1][h2] = dp[h1][h2 - 1] + dp[h1 - 1][h2];


				}


			}



		}

	}

	for (int k = 0; k < i; k++)
	{

		int h = arr[k];
		
		printf("%lld\n",dp[h][h]);


	}








}