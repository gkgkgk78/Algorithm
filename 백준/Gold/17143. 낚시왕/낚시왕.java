import java.awt.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Stack;

public class Main {
	static int r, c, m;
	static int result = 0;

	static class go {

		int x, y, velo, dir, size;

		public go(int x, int y, int velo, int dir, int size) {
			super();
			this.x = x;
			this.y = y;
			this.velo = velo;
			this.dir = dir;
			this.size = size;
		}

		public go(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}

		public go(int x, int y, int velo, int dir) {
			super();
			this.x = x;
			this.y = y;
			this.velo = velo;
			this.dir = dir;
		}

	}

	static ArrayList<go> shark;

	public static void main(String[] args) throws IOException {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer s = new StringTokenizer(in.readLine(), " ");

		r = Integer.parseInt(s.nextToken());
		c = Integer.parseInt(s.nextToken());
		m = Integer.parseInt(s.nextToken());
		shark = new ArrayList<>();
		for (int i = 0; i < m; i++) {

			s = new StringTokenizer(in.readLine(), " ");
			int x, y, vel, dir, size;
			x = Integer.parseInt(s.nextToken());
			x--;
			y = Integer.parseInt(s.nextToken());
			y--;
			vel = Integer.parseInt(s.nextToken());
			dir = Integer.parseInt(s.nextToken());
			size = Integer.parseInt(s.nextToken());
			shark.add(new go(x, y, vel, dir, size));

		}

		game();
		System.out.println(result);

	}

	private static void game() {
		// TODO Auto-generated method stub

		for (int i = 0; i < c; i++) {

			// 낚시왕과 가장 가까운 상어를 한마리 잡음
			// System.out.println(i);
			eat(i);

			// 상어를 이동시킴

			move();
			// System.out.println();
			// 상어가 중복된 곳에 존재를 할시 가장 큰 상어를 제외하고 제거

		}

	}

	private static void move() {
		// TODO Auto-generated method stub

		int graph[][] = new int[r][c];
		int k1 = 0;
		ArrayList<go> temp = new ArrayList<>();
		int dx[] = { 0, -1, 1, 0, 0 };
		int dy[] = { 0, 0, 0, 1, -1 };
		for (go t : shark) {

			// 방향에 따라 움직여야 함

			// d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽
			// System.out.println(t.x + " " + t.y + " " + t.dir);
			if (t.dir == 1) {
				int zx = t.x;
				int zy = t.y;
				int z1 = t.velo;
				

				while (z1 > 0) {

					int tem = dx[t.dir] * z1;

					if (tem + zx < 0) {
						int aa=Math.abs(zx-0);
						z1-=aa;
						zx=0;
						t.dir=2;

					} else if (tem + zx >= r) {
						int aa=Math.abs(r-1-zx);
						z1-=aa;
						zx=r-1;
						t.dir=1;
						
					}
					else
					{
						zx=zx+tem;
						z1=0;
					}


				}
				t.x = zx;
				t.y = zy;

			} else if (t.dir == 2) {
				int zx = t.x;
				int zy = t.y;
				int z1 = t.velo;
				while (z1 > 0) {

					int tem = dx[t.dir] * z1;

					if (tem + zx < 0) {
						int aa=Math.abs(zx-0);
						z1=z1-aa;
						zx=0;
						t.dir=2;

					} else if (tem + zx >= r) {
						int aa=Math.abs(r-1-zx);
						z1=z1-aa;
						zx=r-1;
						t.dir=1;
					}
					else
					{
						zx=zx+tem;
						z1=0;
					}


				}
				t.x = zx;
				t.y = zy;

			} else if (t.dir == 3) {
				// 오른쪽
				int zx = t.x;
				int zy = t.y;
				int z1 = t.velo;
				while (z1 > 0) {

					int tem = dy[t.dir] * z1;

					if (tem + zy < 0) {
						int aa=Math.abs(zy-0);
						z1-=aa;
						zy=0;
						t.dir=3;

					} else if (tem + zy >= c) {
						int aa=Math.abs(c-1-zy);
						z1-=aa;
						zy=c-1;
						t.dir=4;
					}
					else
					{
						zy=zy+tem;
						z1=0;
					}

				}
				t.x = zx;
				t.y = zy;

			} else if (t.dir == 4) {
				// 왼쪽
				int zx = t.x;
				int zy = t.y;
				int z1 = t.velo;

				while (z1 > 0) {

					int tem = dy[t.dir] * z1;

					if (tem + zy < 0) {
						int aa=Math.abs(zy-0);
						z1-=aa;
						zy=0;
						t.dir=3;

					} else if (tem + zy >= c) {
						int aa=Math.abs(c-1-zy);
						z1-=aa;
						zy=c-1;
						t.dir=4;
					}
					else
					{
						zy=zy+tem;
						z1=0;
					}


				}
				
				t.x = zx;
				t.y = zy;

			}
			// System.out.println(t.x+" "+t.y);
			graph[t.x][t.y] += 1;
			if (graph[t.x][t.y] == 2) {
				temp.add(new go(t.x, t.y));
			}

		}
//		for(int i=0;i<r;i++)
//			System.out.println(Arrays.toString(graph[i]));
//		System.out.println();
//		

		for (go g : temp) {
			// System.out.println("아하");
			// 중복된 상어들의 좌표만 존재를 함
			int x1 = g.x;
			int y1 = g.y;
			int size = Integer.MIN_VALUE;
			ArrayList<Integer> op = new ArrayList<>();
			for (int u = 0; u < shark.size(); u++) {
				go g1 = shark.get(u);
				if (g1.x == x1 && g1.y == y1) {
					op.add(u);
					size = Math.max(g1.size, size);
				}
			}

			// 이제 op에 들은거 삭제를 해야함
			for (int u = shark.size() - 1; u >= 0; u--) {
				go g1 = shark.get(u);
				if (g1.x == x1 && g1.y == y1) {
					if (g1.size != size) {
						shark.remove(u);
					}
				}
			}
		}

	}

	private static void eat(int now) {
		// TODO Auto-generated method stub

		int get = -1;
		int index = Integer.MAX_VALUE;
		for (int i = 0; i < c; i++) {

			for (int j = 0; j < shark.size(); j++) {
				go l = shark.get(j);
				if (l.y == now) {
					if (l.x < index) {
						index = l.x;
						get = j;
					}
				}

			}

		}

		if (get != -1) {
			go t = shark.get(get);
			result += t.size;
			// System.out.println(t.size);
			shark.remove(t);
		}

	}

}