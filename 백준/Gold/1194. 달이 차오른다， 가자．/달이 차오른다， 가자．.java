import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static char graph[][];
	static int n, m;

	static class go {

		int x, y, key, count;

		public go(int x, int y, int key, int count) {
			this.x = x;
			this.y = y;
			this.key = key;
			this.count = count;
		}

	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer s = new StringTokenizer(in.readLine(), " ");
		n = Integer.parseInt(s.nextToken());
		m = Integer.parseInt(s.nextToken());
		graph = new char[n][m];
		int x = -1, y = -1;
		for (int i = 0; i < n; i++) {
			char[] t = in.readLine().toCharArray();
			for (int j = 0; j < m; j++) {
				graph[i][j] = t[j];
				if (graph[i][j] == '0') {
					x = i;
					y = j;
					graph[i][j] = '.';

				}
			}

		}
		bfs(x, y);
		System.out.println(-1);

	}

	private static void bfs(int x, int y) {
		// TODO Auto-generated method stub

		int visit[][][] = new int[n][m][1 << 6];

		visit[x][y][0] = 1;

		Queue<go> q = new LinkedList<>();
		q.add(new go(x, y, 0, 0));
		int dx[] = { -1, 1, 0, 0 };
		int dy[] = { 0, 0, -1, 1 };
		while (!q.isEmpty()) {
			go a = q.poll();
			
			if (graph[a.x][a.y] == '1') {
				System.out.println(a.count);
				System.exit(0);

			}

			for (int i = 0; i < 4; i++) {
				int zx = dx[i] + a.x;
				int zy = dy[i] + a.y;

				if (0 <= zx && zx < n && 0 <= zy && zy < m&& graph[zx][zy] != '#') {

					if (visit[zx][zy][a.key] == 0 ) {

						if (graph[zx][zy] >= 'a' && graph[zx][zy] <= 'f') {
							int key = a.key;
							key |= (1 << graph[zx][zy] - 'a');
							visit[zx][zy][key] = 1;
							q.add(new go(zx, zy, key, a.count + 1));

						} else if (graph[zx][zy] >= 'A' && graph[zx][zy] <= 'F') {
							int key = a.key;
							key &= (1 << graph[zx][zy] - 'A');
							if (key != 0) {
								visit[zx][zy][a.key] = 1;
								q.add(new go(zx, zy, a.key, a.count + 1));
							}
						} else {
							// 걍 빈칸임
							visit[zx][zy][a.key]=1;
							q.add(new go(zx, zy, a.key, a.count + 1));

						}

					}

				}

			}

		}

	}

}