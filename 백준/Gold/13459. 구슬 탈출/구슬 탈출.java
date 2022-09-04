import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

class Ball {
	int x;
	int y;
	int count;

	public Ball(int x, int y, int count) {
		this.x = x;
		this.y = y;
		this.count = count;
	}

}

public class Main {

	static int rx;
	static int ry;
	static int bx;
	static int by;
	static int n;
	static int m;
	static int visit[][][][];

	static char graph[][];
	static Ball r_b, b_b;

	public static void bfs(Ball r, Ball b) {
		int dx[] = { -1, 0, 1, 0 };
		int dy[] = { 0, 1, 0, -1 };
		Deque<Ball> qr = new ArrayDeque<>();
		Deque<Ball> qb = new ArrayDeque<>();

		qr.add(r);
		qb.add(b);
		visit[r.x][r.y][b.x][b.y] = 1;
		int ooo;
		while (!qr.isEmpty() && !qb.isEmpty()) {
			Ball tr = qr.pollFirst();
			Ball tb = qb.pollFirst();

			if (tr.count >= 10) {
				System.out.println(0);
				System.exit(0);
			}

			if (tr.x == 1 && tr.y == 1) {
				ooo = 25;
			}
			// 사방 방향으로 각자 기울이면서 최종 위치를 파악하도록 하자
			// 방문하지 않았다면 갈수 있겠지
			// 방문을 하였다면 그 방향은 선택을 할수가 없어.
			// 가다가 벽에 부딪혔다면 멈추면 되고

			// 동시에 움직인 공에서 최종 위치가 같다면 더 멀리 움직인얘가
			// 최종 위치고 다른공은 그전위치로 하자

			// 빨간 공이 구멍에 빠지면 성공
			// but 파란 공도 구멍에 빠지면 안됨(동시)

			// 우선 빨간 공부터 움직이자

			for (int i = 0; i < 4; i++) {
				int r_go = 0;
				int bb = 0;
				int tx = dx[i] + tr.x;
				int ty = dy[i] + tr.y;
				int check_goal_r = 0;
				int check_goal_b = 0;

				while ((graph[tx][ty] == '.' || graph[tx][ty] == 'O')) {

					if (graph[tx][ty] == 'O') {
						tx += dx[i];
						ty += dy[i];
						r_go += 1;
						check_goal_r = 1;
						break;
					}

					tx += dx[i];
					ty += dy[i];
					r_go += 1;

				}
				r_go -= 1;
				tx -= dx[i];
				ty -= dy[i];

				int b_go = 0;

				int zx = dx[i] + tb.x;
				int zy = dy[i] + tb.y;
				while ((graph[zx][zy] == '.' || graph[zx][zy] == 'O')) {

					if (graph[zx][zy] == 'O') {
						zx += dx[i];
						zy += dy[i];
						b_go += 1;
						check_goal_b = 1;
						break;
					}
					zx += dx[i];
					zy += dy[i];
					b_go += 1;

				}
				b_go -= 1;
				zx -= dx[i];
				zy -= dy[i];

				// 여기까지는 해당 방향이 아니고 최종 적으로 이동을 한상태임
				if (check_goal_r == 1 && check_goal_b == 1) {
					if (r_go == b_go) {
						System.out.println(0);
						System.exit(0);
					}
					else
						continue;
				} else if (check_goal_r == 1 && check_goal_b == 0) {
					System.out.println(1);
					System.exit(0);
				}

				else if (check_goal_b == 1) {
					continue;
				}
				if (tx == zx && ty == zy)// 최종 이동 경로가 같을시
				{
					if (r_go < b_go) {
						zx -= dx[i];
						zy -= dy[i];
					} else if (r_go > b_go) {
						tx -= dx[i];
						ty -= dy[i];
					}
				}
				// 이제 이동한방향까지 모두 visit 처리를 해준다

				if (visit[tx][ty][zx][zy] == 0) {
					visit[tx][ty][zx][zy] = 1;
					qr.add(new Ball(tx, ty, tr.count + 1));
					qb.add(new Ball(zx, zy, tb.count + 1));
				}

			}

			// 선택한 방향에 대한 최종 위치 파악

		}
		System.out.println(0);

	}

	public static void main(String[] args) throws NumberFormatException, IOException {

		

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer a1 = new StringTokenizer(in.readLine());
		n = Integer.parseInt(a1.nextToken());
		m = Integer.parseInt(a1.nextToken());
		graph = new char[n][m];
		visit = new int[n][m][n][m];

		for (int i = 0; i < n; i++) {

			char[] temp = in.readLine().toCharArray();

			for (int j = 0; j < m; j++) {
				graph[i][j] = temp[j];

				if (graph[i][j] == 'R') {

					r_b = new Ball(i, j, 0);
					graph[i][j] = '.';

				} else if (graph[i][j] == 'B') {
					b_b = new Ball(i, j, 0);
					graph[i][j] = '.';
				}

			}
		}
		bfs(r_b, b_b);

	}

}