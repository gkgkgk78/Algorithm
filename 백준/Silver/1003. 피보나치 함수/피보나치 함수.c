#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int m[41] = { 1,1 };
int fibo(int N) {
	if (N <= 1) return m[N];
	else {
		if (m[N] > 0) return m[N];
	}
	return m[N] = fibo(N - 1) + fibo(N - 2);
}
int main() {
	int t, n, cont1, cont2;
	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		scanf("%d", &n);
		if (n == 0)
			printf("1 0\n");
		else if (n == 1)
			printf("0 1\n");
		else {
			fibo(n);
			printf("%d %d\n", m[n - 2], m[n - 1]);
		}
	}
	return 0;
}