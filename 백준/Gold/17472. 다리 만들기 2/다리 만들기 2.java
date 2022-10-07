import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int graph[][];
	static int n, m;
	static int parents[];
	static int result = 0;

	static class go {
		int x, y;
		ArrayList<go> next = new ArrayList<>();

		public go(int x, int y) {
			this.x = x;
			this.y = y;
		}

	}

	static class go1 implements Comparable<go1> {
		int len, land1, land2;

		public go1(int len, int land1, int land2) {
			this.len = len;
			this.land1 = land1;
			this.land2 = land2;
		}

		@Override
		public int compareTo(go1 o) {
			// TODO Auto-generated method stub
			return this.len - o.len;
		}

	}

	static List<go> list;
	static List<List<go>> land;

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		list = new ArrayList<>();
		land = new ArrayList<>();
		StringTokenizer s = new StringTokenizer(in.readLine(), " ");
		n = Integer.parseInt(s.nextToken());
		m = Integer.parseInt(s.nextToken());
		visit = new int[n][m];
		graph = new int[n][m];
		for (int i = 0; i < n; i++) {

			s = new StringTokenizer(in.readLine(), " ");
			for (int j = 0; j < m; j++) {
				graph[i][j] = Integer.parseInt(s.nextToken());
				if (graph[i][j] > 0)

				{
					list.add(new go(i, j));
				}

			}

		}

		List<go> l = new ArrayList<>();
		land.add(l);
		int count = 0;// count가 총 섬의 개수를 의미한다.
		int now = 1;
		for (go a : list) {
			if (graph[a.x][a.y] == 1 && visit[a.x][a.y] == 0) {
				check(a.x, a.y, now);

				now++;
				count++;
			}

		}
		
//		for (int i = 0; i < n; i++) {
//			System.out.println(Arrays.toString(graph[i]));
//		}
//		System.out.println();
		
		parents = new int[count + 1];
		makeset(count + 1);
		make();
		//System.out.println(Arrays.toString(parents));
		//System.out.println(result);
		for(int i=1;i<count+1;i++) {

			parents[i]=find(i);
			
		}
		
		int che=find(parents[1]);
		for(int i=2;i<count+1;i++) {
			//System.out.println(find(parents[i]));
			if(find(parents[i])!=che)
			{	System.out.println(-1);
				System.exit(0);
			}
			
		}
		if (result == 0)
			System.out.println(-1);
		else
			System.out.println(result);
	}
	private static int find(int a) {
		if (parents[a] == a)
			return a;
		return parents[a] = find(parents[a]);
	}

	private static int union(int a1, int a2) {

		int z1 = find(a1);
		int z2 = find(a2);
		if (z1 == z2)
			return -1;
		if (a1 < a2)
			parents[z2] = z1;
		else
			parents[z1] = z2;
		return 1;

	}

	private static void makeset(int z) {
		// TODO Auto-generated method stub
		for (int i = 1; i < z; i++) {
			// System.out.println(i);
			parents[i] = i;

		}

	}

	private static void make() {
		// TODO Auto-generated method stub

		// 모든 정점들에 대해서 섬끼리 연결 가능한 모든 엣지를 구해보도록 하자
		// 그렇게 한후에 모든섬을 연결하는 다리 길이의 최솟값을 출력 하도록 해보자

		PriorityQueue<go1> q = new PriorityQueue<>();

		// 우선 가능한 모든 엣지의 셋을 구해 보도록 하자
		for (List<go> is : land) {

			int dx[] = { -1, 0, 1, 0 };// 상우하좌
			int dy[] = { 0, 1, 0, -1 };
			for (go g1 : is) {
				int now = graph[g1.x][g1.y];// 현재 그래프 그룹을 의미함
				// 상우하좌 의 방향에 따라서 끝까지 탐색을 해보도록 하자.

				for (int i = 0; i < 4; i++) {
					int zx = dx[i] + g1.x;
					int zy = dy[i] + g1.y;
					while (zx >= 0 && zx < n && 0 <= zy && zy < m) {
						if (graph[zx][zy] == 0) {
							zx += dx[i];
							zy += dy[i];
						} else {
							if (graph[zx][zy] != now) {
								// 길이, land1,land2
								int zz = Math.abs(g1.x - zx) + Math.abs(g1.y - zy) - 1;
								if (zz >= 2)
									q.add(new go1(zz, now, graph[zx][zy]));
								break;
							} else if (graph[zx][zy] == now) {
								break;
							}
						}

					}

				}

				// 위의 상황은 모든 엣지에서 가능한 엣지들을 모두 탐색을 함

			}

		}
	

		while (!q.isEmpty()) {

			go1 gg = q.poll();
			int z = union(gg.land1, gg.land2);
			
			if (z != -1) {
				//System.out.println(gg.land1+" "+gg.land2+" "+gg.len);
				//System.out.println(Arrays.toString(parents));
				result += gg.len;

			}

		}

	}

	static int visit[][];

	private static void check(int x, int y, int count) {
		// TODO Auto-generated method stub

		// 땅의 모든 좌표를 넣어 줘야 겠다

		Queue<go> q = new LinkedList<>();

		q.add(new go(x, y));
		visit[x][y] = 1;
		int dx[] = { -1, 0, 1, 0 };
		int dy[] = { 0, 1, 0, -1 };
		graph[x][y] = count;
		List<go> l = new ArrayList<>();

		while (!q.isEmpty()) {

			go a = q.poll();
			l.add(a);

			for (int i = 0; i < 4; i++) {
				int zx = dx[i] + a.x;
				int zy = dy[i] + a.y;

				if (0 <= zx && zx < n && 0 <= zy && zy < m) {
					if (visit[zx][zy] == 0 && graph[zx][zy] == 1) {
						visit[zx][zy] = 1;
						graph[zx][zy] = count;
						q.add(new go(zx, zy));
					}

				}

			}

		}
		land.add(l);

	}

}
