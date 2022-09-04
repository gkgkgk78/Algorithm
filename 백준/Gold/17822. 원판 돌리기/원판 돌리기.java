import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

	static int n, m, t;
	static int graph[][];
	static int visit[][];
	static int chch = 0;
	static int total = 0;

	static int total_count = 0;
	static int hihi = 0;

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		// System.setIn(new FileInputStream("src/input.txt"));

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer s = new StringTokenizer(in.readLine(), " ");

		n = Integer.parseInt(s.nextToken());
		m = Integer.parseInt(s.nextToken());
		t = Integer.parseInt(s.nextToken());
		graph = new int[n + 1][m + 1];

		// ArrayList<go>hi=new ArrayList<>();
		for (int i = 1; i <= n; i++) {
			s = new StringTokenizer(in.readLine());
			for (int j = 1; j <= m; j++) {
				graph[i][j] = Integer.parseInt(s.nextToken());
				if (graph[i][j] > 0)
					hihi++;
			}
		}

		for (int i1 = 0; i1 < t; i1++) {
			s = new StringTokenizer(in.readLine());
			int x, d, k;
			x = Integer.parseInt(s.nextToken());
			d = Integer.parseInt(s.nextToken());
			k = Integer.parseInt(s.nextToken());

			move(x, d, k);// 이동을 시킴
			visit = new int[n + 1][m + 1];
			chch = 0;

			if (hihi > 0) {
				//System.out.println(x + " " + d + " " + k);
				
				for (int i = 1; i <= n; i++) {// 원판에 적힌 모든 수들에 대해 수가 같은것을 확인해보도록 하자
					for (int j = 1; j <= m; j++) {
						if (visit[i][j] == 0 && graph[i][j] > 0) {
							dfs(i, j, graph[i][j]);
							if (graph[i][j] == 0)
								hihi--;
						}
					}
				}

				// System.out.println();
				total = 0;
				total_count = 0;
				cal();

				if (chch == 0) {

					// System.out.println(total+" "+total_count);
					double za = (double) total;
					double u = za / total_count;
					for (int i = 1; i <= n; i++) {// 원판에 적힌 모든 수들에 대해 수가 같은것을 확인해보도록 하자
						for (int j = 1; j <= m; j++) {
							if (graph[i][j] > 0) {
								if (graph[i][j] < u)
									graph[i][j] += 1;
								else if (graph[i][j] > u)
									graph[i][j] -= 1;
							}
						}
					}

				}
				
//				for (int i = 0; i <= n; i++) {
//					System.out.println(Arrays.toString(graph[i]));
//				}
//				System.out.println();
			}
		}
		//System.out.println(hihi);
		// 원판에 적힌 것들을 확인해 보도록 하자

		total = 0;
		total_count = 0;
		cal();

		System.out.println(total);

	}

	private static void cal() {
		// TODO Auto-generated method stub
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				if (graph[i][j] > 0) {
					total += graph[i][j];
					total_count++;
				}
			}
		}

	}

	private static void dfs(int x, int y, int val) {
		// TODO Auto-generated method stub

		visit[x][y] = 1;
		int ch = 0;
		if (y == 1) {
			// if (y + 1 <= n) {
			if (graph[x][y + 1] == val && visit[x][y + 1] == 0) {
				// visit[x][y + 1] = 1;
				chch = 1;
				//graph[x][y] = 0;
				graph[x][y + 1] = 0;
				hihi--;
				ch = 1;
				dfs(x, y + 1, val);
			}
			// }
			if (graph[x][m] == val && visit[x][m] == 0) {
				// visit[x][y] = 1;
				chch = 1;
				graph[x][m] = 0;
				//graph[x][y] = 0;
				dfs(x, m, val);
				ch = 1;
				hihi--;
			}
		} else if (y == m) {
			// if (y - 1 >= 1) {
			if (graph[x][y - 1] == val && visit[x][y - 1] == 0) {
				// visit[x][y - 1] = 1;
				chch = 1;
				ch = 1;
				hihi--;
				graph[x][y - 1] = 0;
				//graph[x][y] = 0;
				dfs(x, y - 1, val);
			}
			// }
			if (graph[x][1] == val && visit[x][1] == 0) {
				// visit[x][1] = 1;
				chch = 1;
				ch = 1;
				hihi--;
				graph[x][1] = 0;
				//graph[x][y] = 0;
				dfs(x, 1, val);
			}
		} else {
			if (graph[x][y - 1] == val && visit[x][y - 1] == 0) {
				// visit[x][y - 1] = 1;
				chch = 1;
				ch = 1;
				hihi--;
				graph[x][y - 1] = 0;
				//graph[x][y] = 0;
				dfs(x, y - 1, val);
			}
			if (graph[x][y + 1] == val && visit[x][y + 1] == 0) {
				// visit[x][y + 1] = 1;
				chch = 1;
				ch = 1;
				hihi--;
				graph[x][y + 1] = 0;
				//graph[x][y] = 0;
				dfs(x, y + 1, val);
			}

		}

		if (x + 1 <= n) {
			if (graph[x + 1][y] == val && visit[x + 1][y] == 0) {
				// visit[x+1][y] = 1;
				chch = 1;
				ch = 1;
				hihi--;
				graph[x + 1][y] = 0;
				//graph[x][y] = 0;
				dfs(x + 1, y, val);
			}
		}
		if (x -1>=1) {
			if (graph[x - 1][y] == val && visit[x - 1][y] == 0) {
				// visit[x+1][y] = 1;
				chch = 1;
				ch = 1;
				hihi--;
				graph[x - 1][y] = 0;
				//graph[x][y] = 0;
				dfs(x - 1, y, val);
			}
		}

		if (ch == 1)
			graph[x][y] = 0;

	}

	private static void move(int x, int d, int k) {
		// TODO Auto-generated method stub
			int t = x;
			while (true) {
				for (int i = 0; i < k; i++) {
					if (d == 0) {
						rotateclock(t, k);
					} else if (d == 1) {
						rotatecounterclock(t, k);

					}
				}
				t = t + x;
				if (t > n)
					return;
			}
		
	}

	private static void rotatecounterclock(int t, int k) {
		// TODO Auto-generated method stub
		int last = graph[t][1];// 제일 마지막 원소
		for (int i = 1; i <= m - 1; i++) {
			graph[t][i] = graph[t][i + 1];
			// System.out.println(Arrays.toString(graph[t]));
		}
		graph[t][m] = last;
		// System.out.println(Arrays.toString(graph[t]));
		// System.out.println();
	}

	private static void rotateclock(int t, int k) {
		// TODO Auto-generated method stub

		int last = graph[t][m];// 제일 마지막 원소
		for (int i = m; i > 1; i--) {
			graph[t][i] = graph[t][i - 1];
		}
		graph[t][1] = last;
	}

}