#define _CRT_SECURE_NO_WARNINGS
#define size1 100002
#define size 1000000009

#include<stdio.h>
#include<stdlib.h>



int dp[size1][4];//데이터 넣어줌

//int arr[size1];


int main() {

	int a,b;
	scanf("%d", &a);
	dp[1][1] = 1;
	dp[1][2] = 0;
	dp[1][3] = 0;

	dp[2][1] = 0;
	dp[2][2] = 1;
	dp[2][3] = 0;

	dp[3][1] = 1;
	dp[3][2] = 1;
	dp[3][3] = 1;

	for (int i = 4; i <= size1-2; i++)
	{
		for (int j = 1; j <= 3; j++)
		{
			if (j == 1)
			{
				dp[i][j] = (dp[i-1][2] + dp[i-1][3])%size;
			}
			else if (j == 2)
			{
				dp[i][j] = (dp[i - 2][1] + dp[i - 2][3])%size;
			}

			else
			{
				dp[i][j] = (dp[i - 3][1] + dp[i - 3][2])%size;

			}
		}

	}

	//int sum = 0;
	int* sum = (int*)malloc(sizeof(int) * a);
	for (int i = 0; i < a; i++)
	{
		//sum = 0;
		int d = 0;
		scanf("%d", &d);
		sum[i] = 0;
		for (int j = 1; j <= 3; j++)
		{
			sum[i] = (sum[i] + dp[d][j])%size;
		
			
		}
		
	}
	for (int i = 0; i < a; i++)
	{
		
	
		printf("%d\n", sum[i]);
	}

}