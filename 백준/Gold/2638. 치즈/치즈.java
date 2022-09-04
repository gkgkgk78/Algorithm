import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int visit[][];
	static int n, m;
	static int sh, wo;
	static int graph[][];
	static int chee;

	public static class go {
		int x, y;

		public go(int x, int y) {

			this.x = x;
			this.y = y;
		}

	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub

		

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer s = new StringTokenizer(in.readLine());
		n = Integer.parseInt(s.nextToken());
		m = Integer.parseInt(s.nextToken());
		graph = new int[n][m];
		chee = 0;
		for (int i = 0; i < n; i++) {
			s = new StringTokenizer(in.readLine());
			for (int j = 0; j < m; j++) {
				graph[i][j] = Integer.parseInt(s.nextToken());
				if (graph[i][j] == 1)
					chee += 1;

			}

		}
		int time = 0;

		while (true)

		{

			if (chee == 0) {
				System.out.println(time);
				break;
			} else
				bfs(0, 0);

			time++;

		}

	}

	private static void bfs(int i, int j) {
		Queue<go> q = new LinkedList<>();
		int visit[][] = new int[n][m];

		q.add(new go(i, j));
		visit[i][j] = 1;
		ArrayList<go> death = new ArrayList<>();
		int dx[] = { -1, 0, 1, 0 };
		int dy[] = { 0, 1, 0, -1 };
		while (!q.isEmpty()) {
			go now = q.poll();
			int a1, a2;
			a1 = now.x;
			a2 = now.y;

			for (int i1 = 0; i1 < 4; i1++) {
				int tx = dx[i1] + a1;
				int ty = dy[i1] + a2;

				if (0 <= tx && tx < n && 0 <= ty && ty < m)

				{
					if (visit[tx][ty] == 0) {
						if (graph[tx][ty] == 0) {
							visit[tx][ty] = 1;
							q.add(new go(tx, ty));
						}
					}
					if (graph[tx][ty] == 1)
						visit[tx][ty] += 1;
					if (visit[tx][ty] >= 2)
						death.add(new go(tx, ty));
				}

			}

		}
		int cou = 0;
		for (go k : death) {
			if (graph[k.x][k.y] == 1) {
				graph[k.x][k.y] = 0;
				cou++;
			}
		}
		chee -= cou;
//		for (int ti = 0; ti < n; ti++) {
//
//			System.out.println(Arrays.toString(graph[ti]));
//		}
//		System.out.println();
	}

}