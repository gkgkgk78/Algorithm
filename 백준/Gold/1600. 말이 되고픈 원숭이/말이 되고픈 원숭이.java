import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int tx[] = { -2, -2, -1, -1, 1, 1, 2, 2 };
	static int ty[] = { -1, 1, -2, 2, -2, 2, -1, 1 };
	static int k;
	static int n, m;
	static int visit[][][];// 좌표 2개+걸어서 , 말타고온 횟수
	static int graph[][];
	static int result = Integer.MAX_VALUE;

	static class go {

		int x, y, run, horse, flag;// 총 걸은 횟수, 말타고온 횟수

		public go(int x, int y, int run, int horse, int flag) {
			this.x = x;
			this.y = y;
			this.run = run;
			this.horse = horse;
			this.flag = flag;
		}

	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		// 방문처리를 걸어서 온것과 말타고 온것을 구분하여 작성을 해보자
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		k = Integer.parseInt(in.readLine());
		StringTokenizer s = new StringTokenizer(in.readLine(), " ");

		m = Integer.parseInt(s.nextToken());
		n = Integer.parseInt(s.nextToken());

		graph = new int[n][m];
		visit = new int[n][m][k + 1];
		for (int i = 0; i < n; i++) {
			s = new StringTokenizer(in.readLine(), " ");
			for (int j = 0; j < m; j++) {
				graph[i][j] = Integer.parseInt(s.nextToken());
				for (int l = 1; l <= k; l++) {
					visit[i][j][l] = 0;

				}
			}
		}
		visit[0][0][0]=1;
		bfs(0, 0);
		
		if (result != Integer.MAX_VALUE) {
			
				System.out.println(result);
		}
		else
			if(n==1&&m==1)
				System.out.println(0);
			else	
			System.out.println(-1);
	}

	private static void bfs(int i1, int j1) {
		// TODO Auto-generated method stub

		Queue<go> q = new LinkedList<>();

		q.add(new go(0, 0, 0, 0, 0));

		int dx[] = { -1, 0, 1, 0 };
		int dy[] = { 0, 1, 0, -1 };
		/*
		 * this.x = x; this.y = y; this.run = run; this.horse = horse; this.flag = flag;
		 * 
		 */

		while (!q.isEmpty()) {

			// 처음에 뚜벅이 였다면
			go temp = q.poll();
			int x, y, run, horse, flag;
			x = temp.x;
			y = temp.y;
			run = temp.run;
			horse = temp.horse;
			flag = temp.flag;
			int jo = 0;
			// 뚜벅이로 이동을 함
			
			
			for (int i = 0; i < 4; i++) {
				int zx = x + dx[i];
				int zy = y + dy[i];

				if (0 <= zx && zx < n && 0 <= zy && zy < m && graph[zx][zy] == 0 && visit[zx][zy][horse] == 0) {

					visit[zx][zy][horse] =1;
					q.add(new go(zx, zy, run + 1, horse, 0));

					if (zx == n - 1 && zy == m - 1) {
						jo =run+horse+1;
						if (jo < result)
							result = jo;
						return;
					}

				}

			}

			/// 걸어서 이동을 함
			if (horse < k) {
				for (int i = 0; i < 8; i++) {
					int zx = x + tx[i];
					int zy = y + ty[i];

					if (0 <= zx && zx < n && 0 <= zy && zy < m && graph[zx][zy] == 0 && visit[zx][zy][horse+1] == 0) {

						visit[zx][zy][horse+1] =1;
						q.add(new go(zx, zy, run, horse + 1, 0));

						if (zx == n - 1 && zy == m - 1) {
							jo =run+horse+1;
							if (jo < result)
								result = jo;
							return;
						}

					}

				}

			}

		}

	}

}