import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static int graph[][];
	static int col;
	static int c, r;
	static ArrayList<go> hi;
	static int result = 0;
	static int visit[][];

	static class go {
		int x, y;
		int velocity, dir, size;

		public go(int x, int y, int velocity, int dir, int size) {

			this.x = x;
			this.y = y;
			this.velocity = velocity;
			this.dir = dir;
			this.size = size;
		}

		public go(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}

	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int m;
		StringTokenizer s = new StringTokenizer(in.readLine());

		r = Integer.parseInt(s.nextToken());
		c = Integer.parseInt(s.nextToken());
		m = Integer.parseInt(s.nextToken());
		graph = new int[r + 1][c + 1];
		int a1, a2, a3, a4, a5;

		hi = new ArrayList<>();
		col = 0;
		for (int i = 0; i < m; i++) {
			s = new StringTokenizer(in.readLine());
			a1 = Integer.parseInt(s.nextToken());
			a2 = Integer.parseInt(s.nextToken());
			a3 = Integer.parseInt(s.nextToken());
			a4 = Integer.parseInt(s.nextToken());
			a5 = Integer.parseInt(s.nextToken());
			graph[a1][a2] = 1;
			hi.add(new go(a1, a2, a3, a4, a5));
		}
		game();
		System.out.println(result);

	}

	private static void game() {
		// TODO Auto-generated method stub

		while (true) {
			col++;
			if (col == c + 1) {
				return;
			}
//			for (int i = 1; i <= r; i++) {
//				System.out.println(Arrays.toString(graph[i]));
//			}
			//System.out.println();

			int ch = col;
			// 낚시왕이 가장 가까운 상어를 잡음
			for (int i = 1; i <= r; i++) {
				if (graph[i][ch] ==1) {
					graph[i][ch] = 0;
					for (int i1 = hi.size() - 1; i1 >= 0; i1--) {
						go p=hi.get(i1);
						if (p.x == i && p.y == ch) {
							result += p.size;
							hi.remove(i1);
							break;
						}
					}
					break;
				}

			}
			ArrayList<go> temp = new ArrayList<>();
			// 낚시왕이 있는 열에 있는 상에중 가장 가까운 상어를 잡음
			int ct = 0;
			visit=new int[r+1][c+1];
			for (go tt : hi) {
				// 상어들 이동을 하도록 함.
				move(temp, tt.x, tt.y, tt.dir, tt.size, tt.velocity, ct);
				ct++;
			}
//			System.out.println(col);
//			for (go tt : temp) {
//
//				System.out.println(tt.x + " " + tt.y + " " + tt.size);
//
//			}
			for (go tt : temp) {
				int a1 = tt.x;
				int a2 = tt.y;
				int uu = Integer.MIN_VALUE;
				
				for (int i1 = hi.size() - 1; i1 >= 0; i1--) {
					go ye = hi.get(i1);
					if (ye.x == a1 && ye.y == a2) {
						if(ye.size>uu)
							uu=ye.size;
					}
				}
	
				for (int i1 = hi.size() - 1; i1 >= 0; i1--) {
					go ye = hi.get(i1);
					if (ye.x == a1 && ye.y == a2 && ye.size < uu) {
						hi.remove(i1);
					}
				}

				graph[a1][a2] = 1;
			}
//			System.out.println(col);
//			for (go tt : hi) {
//				// 상어들 이동을 하도록 함.
//				System.out.println(tt.x + " " + tt.y + " " + tt.size + " " + tt.dir);
//
//			}
//			System.out.println();

		}
	}

	private static void move(ArrayList<go> temp, int x, int y, int dir, int size, int velocity, int ct) {
		// TODO Auto-generated method stub
		int u = velocity;
		int tx = x;
		int ty = y;
		int dir1 = dir;
		if(visit[x][y]==0)
			graph[x][y] = 0;
		
		while (u > 0) {
			if (dir1 == 1) {
				x -= 1;
				if (x == 0) {
					x += 2;
					dir1 = 2;
				}
			} else if (dir1 == 2) {
				x += 1;
				if (x == r + 1) {
					x -= 2;
					dir1 = 1;
				}
			} else if (dir1 == 3) {
				y += 1;
				if (y == c + 1) {
					y -= 2;
					dir1 = 4;
				}
			} else if (dir1 == 4) {
				y -= 1;
				if (y == 0) {
					y += 2;
					dir1 = 3;
				}
			}
			u--;
		}
		graph[x][y]=1;
		visit[x][y]+=1;
		if (visit[x][y]==2) {
			visit[x][y]+=1;
			temp.add(new go(x, y));
		}
		go e=hi.get(ct);
		e.x = x;
		e.y = y;
		e.dir = dir1;

	}

}