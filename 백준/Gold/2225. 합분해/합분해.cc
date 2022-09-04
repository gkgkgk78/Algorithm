#define _CRT_SECURE_NO_WARNINGS
#define size 1000000000
#define size1 202
#include<stdio.h>
#include<stdlib.h>



int dp[size1][size1];//데이터 넣어줌

//int arr[size1];


int main() {

	int a,b;
	scanf("%d %d", &a,&b);

	dp[0][0] = 0;
	for (int i = 1; i <= b; i++) {
		dp[0][i] = 1;
	}

	for (int i = 1; i <= a; i++)
	{
		for (int j = 0; j <= b; j++)
		{
			
			if (j == 0)
				dp[i][j] = 0;
			else if (j == 1)
				dp[i][j] = 1;
			else
			{
				for (int c = 0; c <= i; c++)
				{
					dp[i][j] = (dp[i][j]+dp[c][j-1])%size;
				}
			}

		}

	}
	printf("%d", dp[a][b]);



}