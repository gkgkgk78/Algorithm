import java.awt.geom.Area;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int graph[][];
	static int m, n;
	static Queue<go> temp;
	static int sum;
	static int visit[][];
	static class go {
		int x, y;
		int z;

		public go(int x, int y, int z) {

			this.x = x;
			this.y = y;
			this.z = z;
		}

	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		// 며칠이 지나면 토마토가 다 익게 되는지 최소 일수를 알고 싶다
		StringTokenizer s = new StringTokenizer(in.readLine());
		m = Integer.parseInt(s.nextToken());
		n = Integer.parseInt(s.nextToken());
		ArrayList<go> hi = new ArrayList<>();
		sum = 0;
		graph=new int[n][m];
		for (int i = 0; i < n; i++) {
			s = new StringTokenizer(in.readLine());
			for (int j = 0; j < m; j++) {
				graph[i][j] = Integer.parseInt(s.nextToken());
				if (graph[i][j] == 1) {					
					hi.add(new go(i, j, 0));
				}
				if(graph[i][j] == 0)
				{
					sum += 1;
				}

			}
		}
		visit = new int[n][m];
		if (sum == 0) {
			System.out.println(0);
			System.exit(0);
		} else {
			temp = new LinkedList<>();
			for (go go : hi) {
				visit[go.x][go.y]=1;
				temp.add(new go(go.x, go.y, go.z));
			}
			bfs();
		}
//		for (int i = 0; i < n; i++) {
//			System.out.println(Arrays.toString(graph[i]));
//		}
		System.out.println(-1);
	}

	private static void bfs() {
		// TODO Auto-generated method stub

		int dx[] = { -1, 0, 1, 0 };
		int dy[] = { 0, 1, 0, -1 };
		while (!temp.isEmpty()) {
			go a = temp.poll();
			
			
			
			int a1 = a.x;
			int a2 = a.y;
			int a3 = a.z;
			//System.out.println(a1+" "+a2);
			
			for (int i = 0; i < 4; i++) {
				int tx = a1 + dx[i];
				int ty = a2 + dy[i];
				if (0 <= tx && tx < n && 0 <= ty && ty < m) {
					if (visit[tx][ty] == 0 && graph[tx][ty] == 0) {
						temp.add(new go(tx, ty, a3 + 1));
						visit[tx][ty] = 1;
						graph[tx][ty]=1;
						sum -= 1;
						if (sum ==0) {
							System.out.println(a3+1);
							System.exit(0);
						}

					}
				}

			}

		}
	}
}