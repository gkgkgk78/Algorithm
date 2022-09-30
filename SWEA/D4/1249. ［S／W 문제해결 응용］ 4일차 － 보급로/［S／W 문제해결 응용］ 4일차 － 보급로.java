import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {

	static StringBuffer buffer;
	static int visit[][];
	static int distance[][];
	static int graph[][];
	static int z;

	static class go {
		int x, y;

		public go(int x, int y) {
			this.x = x;
			this.y = y;
		}

	}

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		buffer = new StringBuffer();

		int n = Integer.parseInt(in.readLine());

		for (int i = 1; i <= n; i++) {

			z = Integer.parseInt(in.readLine());
			visit = new int[z][z];
			distance = new int[z][z];
			graph = new int[z][z];
			
			for (int k = 0; k < z; k++) {
				char ss[] = in.readLine().toCharArray();
				for (int j = 0; j < z; j++) {
					graph[k][j] = (ss[j]) - '0';
				}
			}
			int z1 = bfs();
			buffer.append("#"+(i)+" " + z1 + "\n");
		}
		System.out.println(buffer);

	}

	private static int bfs() {
		// TODO Auto-generated method stub

		Queue<go> q = new LinkedList<>();
		q.add(new go(0, 0));
		visit[0][0] = 1;
		int dx[] = { -1, 0, 1, 0 };
		int dy[] = { 0, 1, 0, -1 };

		while (!q.isEmpty()) {
			go qq = q.poll();
			int x = qq.x;
			int y = qq.y;
			for (int i = 0; i < 4; i++) {
				int zx = x + dx[i];
				int zy = y + dy[i];
				if (0 <= zx && zx < z && 0 <= zy && zy < z) {

					if (visit[zx][zy] == 0) {
						distance[zx][zy] = distance[x][y] + graph[zx][zy];
						visit[zx][zy] = 1;
						q.add(new go(zx, zy));

					} else {
						if (distance[zx][zy] > distance[x][y] + graph[zx][zy]) {
							distance[zx][zy] = distance[x][y] + graph[zx][zy];
							q.add(new go(zx, zy));
						}
					}

				}
			}

		}

		return distance[z - 1][z - 1];
	}

}