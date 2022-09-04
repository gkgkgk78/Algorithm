#define _CRT_SECURE_NO_WARNINGS
#define size 101
#include<stdio.h>
#include<stdlib.h>


int h1;
int h2;
int arr[size][size];//데이터 넣어줌
long long cal[size][size];//정보 저장
int h3;
int h4;



int max = 0;
long long det(int a, int b)
{

	int k1 = arr[a][b];
	int j1[2] = { a,a+k1  };
	int j2[2] = { b+k1,b  };

	if (a==h1-1&&b==h1-1)
		return 1;
	if (cal[a][b] != -1)
		return cal[a][b];

	

		cal[a][b] = 0;
		for (int i = 0; i < 2; i++)
		{

			int new_r = j1[i];
			int new_c = j2[i];
			//printf("실행%d %d\n", new_r, new_c);
			if (new_r < h1 && new_r >= 0 && new_c < h1 && new_c >= 0)
			{

				//printf("오잉\n", new_r, new_c);

				cal[a][b] = cal[a][b] + det(new_r, new_c);



			}
		}
	
	return cal[a][b];





}




int main() {

	int a, b;
	//freopen("input.txt", "rt", stdin);
	scanf("%d", &a);
	
	
	h1 = a;
	for (int i = 0; i < a; i++)
	{
		for (int j = 0; j < a; j++)
		{

			scanf("%d", &arr[i][j]);
			cal[i][j] = -1;
		}
	}



	det(0, 0);
	
	/*
	for (int i = 0; i < a; i++)
	{
		for (int j = 0; j < a; j++)
		{

			printf("%d ", cal[i][j]);
		}
		printf("\n");
	}
	*/
	printf("%lld", cal[0][0]);




}