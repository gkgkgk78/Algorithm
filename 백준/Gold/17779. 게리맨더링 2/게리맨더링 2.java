import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

	static int graph[][];
	static int n;
	static int result;
	static int tot=0;
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(in.readLine());

		graph = new int[n + 1][n + 1];

		for (int i =0 ; i <n; i++) {
			StringTokenizer s = new StringTokenizer(in.readLine());
			for (int j = 0; j < n; j++) {
				graph[i][j] = Integer.parseInt(s.nextToken());
				tot+=graph[i][j];
			}
		}
		result = Integer.MAX_VALUE;
		for (int i = 0; i < n; i++) {

			for (int j = 0; j < n; j++) {
				game(i, j);
			}
		}
		System.out.println(result);

	}

	private static void game(int x, int y) {
		// TODO Auto-generated method stub
		int d1 = 1;
		int d2 = 1;
		for (d1 = 1; d1 < n; d1++) {
			for (d2 = 1; d2 < n; d2++) {
				if (x + d1 + d2 >=n)
					continue;
				if (y - d1 < 0 || y + d2 >=n)
					continue;
				caculate(x, y, d1, d2);
			}
		}

	}

	private static void caculate(int x, int y, int d1, int d2) {
		// TODO Auto-generated method stub
		
		int visit[][] = new int[n][n];

		for (int i = 0; i <= d1; i++) {
			visit[x + i][y - i] = 1;
			visit[x + d2 + i][y + d2 - i] = 1;
		}
		for (int i = 0; i <= d2; i++) {
			visit[x + i][y + i] = 1;
			visit[x + d1 + i][y - d1 + i] = 1;
		}
		int s1 = 0;
		int s2 = 0;
		int s3 = 0;
		int s4 = 0;
		int s5 = 0;
		int susu[]=new int[5];

		// 1번 지역구 탐색
		for (int i = 0; i < x + d1; i++) {
			for (int j = 0; j <= y; j++) {
				if (visit[i][j]==0) {
					s1 += graph[i][j];
				} else
					break;
			}

		}
		// s2
		for (int i = 0; i <=x + d2; i++) {
			for (int j = n-1; j >y; j--) {
				if (visit[i][j]==0) {
					s2 += graph[i][j];
				} else
					break;
			}

		}
		// s3
		for (int i = x + d1; i < n; i++) {
			for (int j = 0; j < y - d1 + d2; j++) {
				if (visit[i][j]==0) {
					s3 += graph[i][j];
				} else
					break;
			}

		}
		// s4
		for (int i = x+d2+1; i <n; i++) {
			for (int j =n-1; j >=y-d1+d2; j--) {
				if (visit[i][j]==0) {
					s4 += graph[i][j];
				} else
					break;
			}

		}
		s5=tot-(s1+s2+s3+s4);
		susu[0]=s1;
		susu[1]=s2;
		susu[2]=s3;
		susu[3]=s4;
		susu[4]=s5;
		Arrays.sort(susu);
		result=Math.min(result,susu[4]-susu[0]);

	}

}