import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int n, k, m;
	static int graph[][];
	static int dir;
	static int nowx, nowy;
	static int q1, q2, q3, q4, q5, q6;
	static int result = 0;

	static class go {
		int x, y;

		public go(int x, int y) {

			this.x = x;
			this.y = y;
		}

	}

	public static void main(String[] args) throws IOException {
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer s = new StringTokenizer(in.readLine());

		n = Integer.parseInt(s.nextToken());
		m = Integer.parseInt(s.nextToken());
		k = Integer.parseInt(s.nextToken());
		q1 = 2;
		q2 = 1;
		q3 = 5;
		q4 = 6;
		q5 = 4;
		q6 = 3;
		graph = new int[n][m];
		dir = 1;

		for (int i = 0; i < n; i++) {
			s = new StringTokenizer(in.readLine());

			for (int j = 0; j < m; j++)
				graph[i][j] = Integer.parseInt(s.nextToken());

		}
//		for (int i = 0; i < n; i++) {
//			System.out.println(Arrays.toString(graph[i]));
//		}
		nowx = 0;
		nowy = 0;

		for (int i = 0; i < k; i++) {
			move();
		}
		System.out.println(result);

	}

	private static void move() {
		// TODO Auto-generated method stub
		int dx[] = { -1, 0, 1, 0 };
		int dy[] = { 0, 1, 0, -1 };

		// 주사위가 위치한 현재 좌표를 의미함

		// 이동하고자 하는 방향으로 이동 가능한지를 파악 하도록 하자.

		int tx = dx[dir] + nowx;
		int ty = dy[dir] + nowy;

		//System.out.println(nowx+" "+nowy+" "+dir);
		// 이동 방향을 벗어나게 된 경우, 방향을 변경해줌
		if (tx < 0 || tx >= n || ty < 0 || ty >=m) {
			int temp = dir;
			for (int i = 0; i < 2; i++) {
				temp += 1;
				if (temp > 3)
					temp = 0;
			}
			dir = temp;
			tx = dx[dir] + nowx;
			ty = dy[dir] + nowy;
		}
		//System.out.println(dir);
		
		
		// 이제 이동하면 됨
		int find = graph[tx][ty];
		// 주사위도 이동을 하여 보자
		move_dx();

		// 점수 획득을 하여 보자
		int get = bfs(tx, ty);
		result += (get * find);
		// 이동 방향을 결정 하자

		if (find < q4) {
			dir += 1;
			if (dir > 3)
				dir = 0;
		} else if (find > q4) {
			dir -= 1;
			if (dir < 0)
				dir = 3;

		}
		// 이동한 방향으로 다시 지정해줌
		nowx = tx;
		nowy = ty;
		//System.out.println(q1+" "+q2+" "+q3+" "+q4+" "+q5+" "+q6);
		//System.out.println(find+" "+q4);
		//System.out.println(tx+" "+ty+" "+dir);
	}

	private static int bfs(int tx, int ty) {
		// TODO Auto-generated method stub
		Queue<go> q = new LinkedList<>();
		int visit[][] = new int[n][m];
		int can = graph[tx][ty];
		int dx[] = { -1, 0, 1, 0 };
		int dy[] = { 0, 1, 0, -1 };
		visit[tx][ty] = 1;
		q.add(new go(tx, ty));
		int count = 1;
		while (!q.isEmpty()) {
			go aa = q.poll();

			for (int i = 0; i < 4; i++) {

				int zx = dx[i] + aa.x;
				int zy = dy[i] + aa.y;
				if (0 <= zx && zx < n && 0 <= zy && zy < m) {
					if (visit[zx][zy] == 0 && graph[zx][zy] == can) {
						q.add(new go(zx, zy));
						visit[zx][zy] = 1;
						count++;
					}
				}

			}
		}

		return count;

	}

	private static void move_dx() {
		// TODO Auto-generated method stub
		int a1, a2, a3, a4, a5, a6;
		a1 = q1;
		a2 = q2;
		a3 = q3;
		a4 = q4;
		a5 = q5;
		a6 = q6;
		if (dir == 0)// 북
		{
			q1 = a2;
			q2 = a3;
			q3 = a4;
			q4 = a1;
			q5 = a5;
			q6 = a6;
		}

		else if (dir == 1)// 동
		{
			q1 = a1;
			q2 = a5;
			q3 = a3;
			q4 = a6;
			q5 = a4;
			q6 = a2;

		} else if (dir == 2)// 남
		{

			q1 = a4;
			q2 = a1;
			q3 = a2;
			q4 = a3;
			q5 = a5;
			q6 = a6;
		}

		else if (dir == 3)// 서
		{

			q1 = a1;
			q2 = a6;
			q3 = a3;
			q4 = a5;
			q5 = a2;
			q6 = a4;
		}

	}

}