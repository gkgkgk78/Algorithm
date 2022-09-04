#define _CRT_SECURE_NO_WARNINGS
#define size1 100001
#define size 1000000009

#include<stdio.h>
#include<stdlib.h>



int dp[size1];//데이터 넣어줌

//int arr[size1];


int main() {

	int a,b;
	scanf("%d", &a);
	dp[1] = 1;
	dp[2] = 2;
	dp[3] = 2;
	dp[4] = 3;
	dp[5] = 3;
	dp[6] = 6;


	for (int i = 7; i <= size1-1; i++)
	{
		dp[i] = ( (dp[i - 2] + dp[i - 4])%size + dp[i - 6])%size;

	}

	//int sum = 0;
	int* sum = (int*)malloc(sizeof(int) * a);
	for (int i = 0; i < a; i++)
	{
		//sum = 0;
		int d = 0;
		scanf("%d", &d);
		
		sum[i] = dp[d];
		
		
		
	}
	for (int i = 0; i < a; i++)
	{
		
	
		printf("%d\n", sum[i]);
	}
	
}