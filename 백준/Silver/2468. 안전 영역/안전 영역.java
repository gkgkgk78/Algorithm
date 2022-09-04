import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;
import java.util.concurrent.LinkedBlockingDeque;

public class Main {

	static int graph[][];
	static int result;
	static int fifi;
	static int visit[][];
	static int n;

	static class go {
		int x, y;

		public go(int x, int y) {
			this.x = x;
			this.y = y;
		}

	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		result = Integer.MIN_VALUE;
		fifi = 1;
		n = Integer.parseInt(in.readLine());
		graph=new int[n][n];
		for (int i = 0; i < n; i++) {
			StringTokenizer s = new StringTokenizer(in.readLine(), " ");
			for (int j = 0; j < n; j++) {
				graph[i][j] = Integer.parseInt(s.nextToken());
				result = Math.max(result, graph[i][j]);
			}
		}

		for (int i = 1; i < result; i++) {
			visit = new int[n][n];
			int cnt = 0;
			for (int j = 0; j < n; j++) {
				for (int k = 0; k < n; k++) {
					if (graph[j][k] > i && visit[j][k] == 0) {
						bfs(j, k, i);
						cnt++;
					}

				}
			}
			fifi = Math.max(fifi, cnt);
		}
		System.out.println(fifi);
	}

	private static void bfs(int j, int k, int height) {
		// TODO Auto-generated method stub
		Queue<go> q = new LinkedList<>();

		int dx[] = { -1, 0, 1, 0 };
		int dy[] = { 0, 1, 0, -1 };
		visit[j][k]=1;
		q.add(new go(j,k));
		while (!q.isEmpty()) {
			go a = q.poll();
			for (int i = 0; i < 4; i++) {
				int zx = dx[i] + a.x;
				int zy = dy[i] + a.y;

				if (0 <= zx && zx < n && 0 <= zy && zy < n) {
					if (graph[zx][zy] > height && visit[zx][zy] == 0) {
						{
							q.add(new go(zx, zy));
							visit[zx][zy]=1;

						}
					}
				}

			}

		}

	}

}