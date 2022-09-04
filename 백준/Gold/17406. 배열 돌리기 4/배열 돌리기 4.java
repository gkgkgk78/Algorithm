import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static StringBuffer buffer;

	static int n1, m1;
	static int isselected[];
	static int lastt;
	static int opop = 0;
	static int graph1[][];

	public static  void rotate(int nx, int ny, int mx, int my) {
		// nx ny mx my 시작점 끝나는점

		int fx = nx;
		int fy = ny;
		int fin = 0;
		int fin1 = 0;

		int visit[][] = new int[n1][m1];

		int tx = nx;
		int ty = ny;
		int i, j;
		while (fx < mx && fy < my) {
			int tempx = fx;
			int tempy = fy;

			if (visit[tempx][tempy] == 0)// 여기서 이제 회전을 하면서 확인을 해보도록 하자
			{
				int op = 0;

				int temp = 0;
				int first = graph1[tempx][tempy];
				int check = 0;

				/// 우
				for (j = tempy; j <= my - 1; j++) {
					if (visit[tempx][j + 1] == 0) {
						temp = graph1[tempx][j + 1];
						graph1[tempx][j + 1] = first;
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

				// 하
				for (i = tempx; i <= mx - 1; i++) {
					if (visit[i + 1][tempy] == 0) {
						temp = graph1[i + 1][tempy];
						graph1[i + 1][tempy] = first;
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

				// 좌
				for (j = tempy; j - 1 >= ny; j--) {
					if (visit[tempx][j - 1] == 0 && j - 1 >= 0) {
						temp = graph1[tempx][j - 1];
						graph1[tempx][j - 1] = first;
						first = temp;
						visit[tempx][j - 1] = 1;
						check = 1;
					} else
						break;
				}
				if (check == 1)
					op += 1;
				check = 0;

				tempy = j;

				// 상
				for (i = tempx; i - 1 >= nx; i--) {
					if (visit[i - 1][tempy] == 0) {
						temp = graph1[i - 1][tempy];
						graph1[i - 1][tempy] = first;
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

			} else
				break;

			fx += 1;
			fy += 1;

		}
	

	}

	public static void comb(int[] xx, int[] yy, int[] zz, int[] numbers, int r, int k, int start, int[] put,
			int[][] graph) {
		// TODO Auto-generated method stub

		if (k > r) {
			graph1 = new int[n1][m1];
			for (int i1 = 0; i1 < n1; i1++) {
				for (int j1 = 0; j1 < m1; j1++) {
					graph1[i1][j1] = graph[i1][j1];
				}
			}
			// 이제 rotate를 하자
			for (int i = 1; i <= r; i++) {
			
				int ra = xx[put[i]];
				int c = yy[put[i]];
				int sa = zz[put[i]];
				if (i == 2) {
					opop = 2;

				}


				rotate(ra - sa - 1, c - sa - 1, ra + sa - 1, c + sa - 1);
				opop = 0;
				
				
			}
			int sumz = 0;

			for (int i1 = 0; i1 < n1; i1++) {
				for (int j1 = 0; j1 < m1; j1++) {					
					sumz += graph1[i1][j1];
				}
				if(sumz<lastt)
					lastt=sumz;
				sumz=0;
				
			}

			return;
		}
		for (int i = 1; i <= r; i++) {
			if (isselected[i] == 1)
				continue;
			put[k] = numbers[i];
			isselected[i] = 1;
			comb(xx, yy, zz, numbers, r, k + 1, start + 1, put, graph);
			isselected[i] = 0;

		}

	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		lastt = 9999999;
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		buffer = new StringBuffer();
		int n, m, r;
		StringTokenizer s = new StringTokenizer(in.readLine());
		n = Integer.parseInt(s.nextToken());
		m = Integer.parseInt(s.nextToken());
		r = Integer.parseInt(s.nextToken());
		n1 = n;
		m1 = m;
		int[][] graph = new int[n][m];
		for (int i = 0; i < n; i++) {
			s = new StringTokenizer(in.readLine());
			for (int j = 0; j < m; j++) {
				graph[i][j] = Integer.parseInt(s.nextToken());
			}

		}
		int ra, c, sa;
		int xx[] = new int[r + 1];
		int yy[] = new int[r + 1];
		int zz[] = new int[r + 1];
		int numbers[] = new int[r + 1];
		isselected = new int[r + 1];
		int put[] = new int[r + 1];
		for (int i = 0; i < r; i++) {
			s = new StringTokenizer(in.readLine());
			ra = Integer.parseInt(s.nextToken());
			c = Integer.parseInt(s.nextToken());
			sa = Integer.parseInt(s.nextToken());
			xx[i + 1] = ra;
			yy[i + 1] = c;
			zz[i + 1] = sa;
			numbers[i + 1] = i + 1;
			
		}
		comb(xx, yy, zz, numbers, r, 1, 1, put, graph);
		System.out.println(lastt);

	}

}