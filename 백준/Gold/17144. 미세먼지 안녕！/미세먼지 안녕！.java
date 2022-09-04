import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {

	static int graph[][];
	static int ux, uy, dx, dy;
	static ArrayList<go> hi;
	static int r, c;

	static class go {
		int x, y, z;

		public go(int x, int y, int z) {
			this.x = x;
			this.y = y;
			this.z = z;
		}
	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		// 미세먼지가 확산이 된후에 공기 청정기가 작동
		

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int t;
		StringTokenizer s = new StringTokenizer(in.readLine(), " ");
		r = Integer.parseInt(s.nextToken());
		c = Integer.parseInt(s.nextToken());
		t = Integer.parseInt(s.nextToken());
		ux = -1;
		uy = -1;
		dx = -1;
		dy = -1;
		
		graph = new int[r][c];
		for (int i = 0; i < r; i++) {
			s = new StringTokenizer(in.readLine(), " ");
			for (int j = 0; j < c; j++) {
				graph[i][j] = Integer.parseInt(s.nextToken());
				if (graph[i][j] == -1) {
					if (ux != -1) {
						dx = i;
						dy = j;

					} else {
						ux = i;
						uy = j;
					}

				} 

			}
		}

		for (int i = 0; i < t; i++) {
			game();

		}
		int sum = 0;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (graph[i][j] > 0)
					sum += graph[i][j];

			}

		}
		System.out.println(sum);

	}

	private static void game() {
		// TODO Auto-generated method stub

		int dx[] = { -1, 0, 1, 0 };
		int dy[] = { 0, 1, 0, -1 };
		// 미세먼지를 확산 하도록 하자

		ArrayList<go> temp = new ArrayList<>();

		for (int i1 = 0; i1 < r; i1++) {
			for (int j = 0; j < c; j++) {
				if (graph[i1][j] > 0) {
					int a1 = i1;
					int a2 = j;
					int minus = graph[a1][a2] / 5;

					for (int i = 0; i < 4; i++) {
						int zx = a1 + dx[i];
						int zy = a2 + dy[i];

						if (0 <= zx && zx < r && 0 <= zy && zy < c) {
							if (graph[zx][zy] != -1) {
								temp.add(new go(zx, zy, minus));
								graph[a1][a2] -= minus;
							}
						}
					}
				}
			}

		}

		for (

		go a : temp) {
			graph[a.x][a.y] += a.z;
		}
		// 미세먼지 확산 끝

		// 공기 청정기 작동 하도록 하자

		move_up();

		move_down();

	}

	private static void move_down() {
		// TODO Auto-generated method stub
		int x = dx;
		int y = dy + 1;

		// 오른쪽 이동을 하자

		int lastright = graph[x][c - 1];// 맨 오른쪽

		for (int i = c - 1; i >= 2; i--) {
			graph[x][i] = graph[x][i - 1];
		}
		graph[dx][dy + 1] = 0;

		// 아래 이동을 하자
		int lastdown = graph[r - 1][c - 1];
		for (int i = r - 1; i >= x + 2; i--) {
			graph[i][c - 1] = graph[i - 1][c - 1];
		}
		graph[x + 1][c - 1] = lastright;

		// 왼쪽이동을함
		int lastleft = graph[r - 1][0];
		for (int i = 0; i <= c - 3; i++) {
			graph[r - 1][i] = graph[r - 1][i + 1];
		}
		graph[r - 1][c - 2] = lastdown;
//		for (int i = 0; i < r; i++) {
//			System.out.println(Arrays.toString(graph[i]));
//			
//		}	
//		
		// 위쪽이동을함
		for (int i = x; i <= r - 3; i++) {
			if (graph[i][0] != -1)
				graph[i][0] = graph[i + 1][0];
		}
		graph[r - 2][0] = lastleft;
	}

	private static void move_up() {
		// TODO Auto-generated method stub

		int x = ux;
		int y = uy + 1;

		int temp = graph[x][y];
		int temp1 = graph[x][y];
		// 오른쪽 이동
		int last = graph[x][c - 1];// 젤 오른쪽 얘를 말함

		for (int i = c - 1; i > uy + 1; i--) {
			graph[x][i] = graph[x][i - 1];
		}
		graph[ux][uy + 1] = 0;
		// 위로 이동
		int lastup = graph[0][c - 1];

		for (int i = 0; i <= x - 2; i++) {

			graph[i][c - 1] = graph[i + 1][c - 1];
		}

		graph[ux - 1][c - 1] = last;

		// 왼쪽 이동
		int lastleft = graph[0][0];
		for (int i = 0; i <= c - 3; i++) {
			graph[0][i] = graph[0][i + 1];
		}
		graph[0][c - 2] = lastup;

		// 아래 이동
		for (int i = x; i >= 2; i--) {

			if (graph[i][0] != -1)
				graph[i][0] = graph[i - 1][0];
		}

		graph[1][0] = lastleft;
//		
//		for (int i = 0; i < r; i++) {
//			System.out.println(Arrays.toString(graph[i]));
//			
//			
	}

}
