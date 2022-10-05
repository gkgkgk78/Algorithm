import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.LineNumberInputStream;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static class go {
		int x, y;

		public go(int x, int y) {
			this.x = x;
			this.y = y;
		}

	}
	static int total=0;
	static int graph[][];
	static int visit[][];

	static int n, m;

	public static void main(String[] args) throws IOException {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer s = new StringTokenizer(in.readLine(), " ");

		n = Integer.parseInt(s.nextToken());
		m = Integer.parseInt(s.nextToken());
		graph=new int[n][m];
		for (int i = 0; i < n; i++) {
			s = new StringTokenizer(in.readLine(), " ");

			for (int j = 0; j < m; j++) {
				graph[i][j] = Integer.parseInt(s.nextToken());
				if(graph[i][j]==1)
				{
					total++;
				}
			}

		}

		// 모두 녹아서 없어지는 데 걸리는 시간
		int z=total;
		int time = 0;
		while (true) {
			bfs();
			time++;
			if (total == 0)

			{
				System.out.println(time);
				System.out.println(z);
				break;
			}
			else
				
			{
				z=total;
			}
		}

		// 모두 녹기 한시간 전에 남아있는 치즈 조각이 놓여있는 칸

	}

	private static void bfs() {
		// TODO Auto-generated method stub

		int dx[] = { -1, 0, 1, 0 };
		int dy[] = { 0, 1, 0, -1 };

		visit = new int[n][m];
		Queue<go> q = new LinkedList<>();
		q.add(new go(0, 0));
		visit[0][0] = 1;
		ArrayList<go> last = new ArrayList<>();
		while (!q.isEmpty()) {

			go a = q.poll();
			for (int i = 0; i < 4; i++) {
				int zx = dx[i] + a.x;
				int zy = dy[i] + a.y;

				if (0 <= zx && zx < n && 0 <= zy && zy < m) {

					if (visit[zx][zy] == 0 && graph[zx][zy] == 1) {
						visit[zx][zy] = 1;
						
					} else if (visit[zx][zy] <2 && graph[zx][zy] == 1) {
						
						visit[zx][zy] +=1;

					}
					else if (visit[zx][zy] == 0 && graph[zx][zy] == 0) {
						q.add(new go(zx, zy));
						visit[zx][zy] =1;

					}

				}

			}
		}
		int u=0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if(graph[i][j]==1&&visit[i][j]>0)
				{
					total--;
					graph[i][j]=0;
				}
			}

		}

	}

}