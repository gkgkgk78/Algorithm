import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static StringBuffer buffer;
	static int graph[][];

	public static void rotate(int n, int m) {

		int fx = 0;
		int fy = 0;
		int fin = 0;
		int fin1=0;
		int visit[][] = new int[n+1][m+1];
		if (n % 2 == 0)
			fin = n / 2;
		else
			fin = (n / 2) + 1;
		if (m % 2 == 0)
			fin1 = m / 2;
		else
			fin1 = (m / 2) + 1;

		int tx = n;
		int ty = m;
		int i, j;

		while (fx < fin && fy < fin1) {
			int tempx = fx;
			int tempy = fy;

			while (visit[tempx][tempy] == 0)// 여기서 이제 회전을 하면서 확인을 해보도록 하자
			{
				int op = 0;

				int temp = 0;
				int first = graph[tempx][tempy];
				int check = 0;
				// 하
				for (i = tempx; i < tx - 1; i++) {
					if (visit[i + 1][tempy] == 0&&i+1<n) {
						temp = graph[i + 1][tempy];
						graph[i + 1][tempy] = first;
						first = temp;
						visit[i + 1][tempy] = 1;
						check = 1;
					} else
						break;
				}
				
				if (check == 1)
					op += 1;
				check = 0;
				tempx = i;

				/// 우
				for (j = tempy; j < ty - 1; j++) {
					if (visit[tempx][j + 1] == 0&&j+1<m) {
						temp = graph[tempx][j + 1];
						graph[tempx][j + 1] = first;
						first = temp;
						visit[tempx][j + 1] = 1;
						check = 1;
					} else
						break;
				}
				if (check == 1)
					op += 1;
				check = 0;
				tempy = j;


				// 상
				for (i = tempx; i > 0; i--) {
					if (visit[i - 1][tempy] == 0&&i-1>=0) {
						temp = graph[i - 1][tempy];
						graph[i - 1][tempy] = first;
						first = temp;
						visit[i - 1][tempy] = 1;
						check = 1;
					} else
						break;
				}

				tempx = i;
				if (check == 1)
					op += 1;
				check = 0;

				// 좌
				for (j = tempy; j > 0; j--) {
					if (visit[tempx][j - 1] == 0&&j-1>=0) {
						temp = graph[tempx][j - 1];
						graph[tempx][j - 1] = first;
						first = temp;
						visit[tempx][j - 1] = 1;
						check = 1;
					} else
						break;
				}
				if (check == 1)
					op += 1;
				check = 0;

				if (op == 1) {

					graph[fx][fy] = temp;
					visit[fx][fy] = 1;
					break;

				}
				
				tempy = j;
				

			}
			
			fx += 1;
			fy += 1;

		}

	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		buffer = new StringBuffer();
		int n, m, r;
		StringTokenizer s = new StringTokenizer(in.readLine());
		n = Integer.parseInt(s.nextToken());
		m = Integer.parseInt(s.nextToken());
		r = Integer.parseInt(s.nextToken());
		graph = new int[n][m];
		for (int i = 0; i < n; i++) {
			s = new StringTokenizer(in.readLine());
			for (int j = 0; j < m; j++) {
				graph[i][j] = Integer.parseInt(s.nextToken());
			}

		}

		for (int k = 0; k < r; k++) {
			rotate(n, m);

		}
		for (int k = 0; k < n; k++) {
			for (int j = 0; j < m; j++) {
				buffer.append(graph[k][j] + " ");
			}
			buffer.append("\n");
		}
		System.out.println(buffer);
	}

}