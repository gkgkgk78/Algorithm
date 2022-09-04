#define _CRT_SECURE_NO_WARNINGS
#define size1 100001
#define size 1000000009

#include<stdio.h>
#include<stdlib.h>



int dp[size1][2];//데이터 넣어줌

//int arr[size1];


int main() {

	int a,b;
	scanf("%d", &a);
	dp[1][0] = 1;
	dp[1][1] = 0;
	dp[2][0] = 1;
	dp[2][1] = 1;
	dp[3][0] = 2;
	dp[3][1] = 2;
	
	


	for (int i = 4; i <= size1-1; i++)
	{
		dp[i][0] = ( (dp[i - 1][1] + dp[i - 2][1])%size + dp[i - 3][1])%size;
		dp[i][1] = ((dp[i - 1][0] + dp[i - 2][0]) % size + dp[i - 3][0]) % size;

	}

	//int sum = 0;
	int* sum = (int*)malloc(sizeof(int) * a);
	for (int i = 0; i < a; i++)
	{
		//sum = 0;
		int d = 0;
		scanf("%d", &d);
		
		sum[i] = d;
		
		
		
	}
	for (int i = 0; i < a; i++)
	{
		int h = sum[i];
	
		printf("%d %d\n", dp[h][0],dp[h][1]);
	}
	
}