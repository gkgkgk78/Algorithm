import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static class go {
		int x, y;

		public go(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}

	}

	static int numbers[];
	static int graph[][];
	static int result = Integer.MIN_VALUE;
	static ArrayList<go> virus;
	static ArrayList<go> blank;
	static int n, m;
	static int ga = 0;
	static int left = 0;

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer s = new StringTokenizer(in.readLine(), " ");
		n = Integer.parseInt(s.nextToken());
		m = Integer.parseInt(s.nextToken());
		graph = new int[n][m];
		numbers=new int[3];
		virus = new ArrayList<>();
		blank = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			s = new StringTokenizer(in.readLine(), " ");
			for (int j = 0; j < m; j++) {
				graph[i][j] = Integer.parseInt(s.nextToken());
				if (graph[i][j] == 2) {
					virus.add(new go(i, j));
				}
				if (graph[i][j] == 0) {
					blank.add(new go(i, j));
					ga++;
				}

			}

		}
		
		comb(0, 3, 0);
		System.out.println(result);

	}

	private static void comb(int start, int end, int cnt) {
		// TODO Auto-generated method stub

		if (cnt == end) {

			game();
			
			return;
		}

		for (int i = start; i < ga; i++) {
			numbers[cnt] = i;
			comb(i + 1, end, cnt + 1);

		}

	}

	private static void game() {
		// TODO Auto-generated method stub

		// 배열 복사
		int graphz[][] = new int[n][m];
		int dx[] = { -1, 0, 1, 0 };
		int dy[] = { 0, 1, 0, -1 };
		int zz = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				graphz[i][j] = graph[i][j];
			}
		}
		int c=0;
		for (int i=0;i<numbers.length;i++) {
			go aa=blank.get(numbers[i]);	
			graphz[aa.x][aa.y]=1;
			//System.out.print(aa.x+" "+aa.y+" ");
			
		}
		//System.out.println();
		

		Queue<go> q = new LinkedList<>();

		for (go g : virus) {
			q.add(new go(g.x, g.y));

		}

		while (!q.isEmpty()) {

			go a = q.poll();
//			if (zz == ga) {
//				return;
//			}

			for (int i = 0; i < 4; i++) {

				int zx = a.x + dx[i];
				int zy = a.y + dy[i];
				if (0 <= zx && zx < n && 0 <= zy && zy < m) {
					if (graphz[zx][zy] == 0) {
						graphz[zx][zy] = 2;
						q.add(new go(zx, zy));
						zz++;
					}

				}
			}

		}
		int u=0;
		//System.out.println(ga-zz);
		int zk=0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if(graphz[i][j]==0)
					zk++;
			}
		}
		//System.out.println(zk);
		result = Math.max(result, zk);
//		if (ga - zz > 0) {
//			if(ga-zz==30)
//				u=ga-zz;
//			result = Math.max(result, ga - zz);
//		}

	}

}