#define _CRT_SECURE_NO_WARNINGS
#define size 32
#define size1 1001
#include<stdio.h>
#include<stdlib.h>



int dp[size1][size1];//데이터 넣어줌

//int arr[size1];

	
int main() {

	int a;
	int i = 0;
	dp[1][1] = 1;
	dp[2][1] = 1;
	dp[2][2] = 1;
	dp[3][1] = 1;
	dp[3][2] = 2;
	dp[3][3] = 1;

	//freopen("input.txt", "rt", stdin);
	
	

	for (int i = 4; i <= 1000; i++)
	{
		for (int j = 1; j <=i ; j++)
		{
			dp[i][j] = ((dp[i - 1][j - 1] + dp[i - 2][j - 1] )% 1000000009 + dp[i - 3][j - 1]) % 1000000009;
			

		}
	}
	scanf("%d", &a);
	int j1, j2;
	for (int i = 0; i < a; i++)
	{
		j1 =0;
		j2 = 0;
		scanf("%d %d", &j1, &j2);
		printf("%d\n", dp[j1][j2]);

	}



	





}