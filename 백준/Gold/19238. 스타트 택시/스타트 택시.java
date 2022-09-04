import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

import javax.management.Query;

public class Main {

	static int n, m, k;
	static int graph[][];
	static ArrayList<go> cus;
	static go taxi;
	static int val,tx,ty;
	static class go {
		int x, y;
		int tox, toy;
		int depth;

		public go(int x, int y) {
			this.x = x;
			this.y = y;
		}

		public go(int x, int y, int depth) {
			this.x = x;
			this.y = y;
			this.depth = depth;
		}

		public go(int x, int y, int tox, int toy) {
			this.x = x;
			this.y = y;
			this.tox = tox;
			this.toy = toy;
		}

	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer s = new StringTokenizer(in.readLine(), " ");
		n = Integer.parseInt(s.nextToken());
		m = Integer.parseInt(s.nextToken());
		k = Integer.parseInt(s.nextToken());

		graph = new int[n][n];
		cus = new ArrayList<>();

		for (int i = 0; i < n; i++) {
			s = new StringTokenizer(in.readLine(), " ");
			for (int j = 0; j < n; j++) {
				graph[i][j] = Integer.parseInt(s.nextToken());
			}
		}
		s = new StringTokenizer(in.readLine(), " ");
		taxi = new go(Integer.parseInt(s.nextToken())-1, Integer.parseInt(s.nextToken())-1 );
		for (int i = 0; i < m; i++) {
			s = new StringTokenizer(in.readLine(), " ");
			int a1=Integer.parseInt(s.nextToken())-1;
			int a2=Integer.parseInt(s.nextToken())-1;
			graph[a1][a2]=3;
			cus.add(new go(a1,a2,Integer.parseInt(s.nextToken())-1, Integer.parseInt(s.nextToken())-1 ) );
		}
		game();
		System.out.println(-1);

	}

	private static void game() {
		// TODO Auto-generated method stub

		while (true) {
			val = Integer.MAX_VALUE;
			tx = -1;
			ty = -1;
			int e=bfs1();
			
//			for (go g : cus) {
//				bfs1();
//				int h = bfs(g.x, g.y);// 각 고객당 최단 거리를 구하고자 함
//				if (h >= 0) {
//					if (h < val) {
//						val = h;
//						tx = g.x;
//						ty = g.y;
//					} else if (h == val) {
//						// 행번호가 가장 작은 승객
//						if (g.x < tx) {
//							tx = g.x;
//							ty = g.y;
//						} else if (g.x == tx) {
//							if (g.y < ty) {
//								tx = g.x;
//								ty = g.y;
//							}
//						}
//
//					}
//
//				}
//			}
			if(e==0)
				return;
			if(val==Integer.MAX_VALUE)
				return;
			for(int i=cus.size()-1;i>=0;i--)
			{
				go g=cus.get(i);
				if(g.x==tx&&g.y==ty) {
					taxi.x=tx;
					taxi.y=ty;
					graph[g.x][g.y]=0;
					k-=val;//우선 승객 태운 만큼 기름을 뺌
					//bfs로 목적지까지의 최단 경로를 찾음
					
					int h = bfs(g.tox, g.toy);
					if (h==-1)
						return;
					if(k-h<0)
						return ;
					else
						k=k-h;
					k=k+(h*2);
					
					taxi.x=g.tox;
					taxi.y=g.toy;
					cus.remove(i);
					break;
				}
	
			}
			if(cus.size()==0)
			{
				System.out.println(k);
				System.exit(0);
			}
		}
	}

	private static int  bfs1() {
		// TODO Auto-generated method stub
		Queue<go> q = new LinkedList<>();
		boolean visit[][] = new boolean[n][n];
		q.add(new go(taxi.x, taxi.y, 0));
		int dx[] = { -1, 0, 1, 0 };
		int dy[] = { 0, 1, 0, -1 };
		visit[taxi.x][taxi.y]=true;
		int count=cus.size();
		while (!q.isEmpty()) {
			go a = q.poll();
			int a1 = a.x;
			int a2 = a.y;
			
			if (graph[a1][a2]==3) {
				update(a,a.depth);
				count--;
			}
			if(count==0)
				return 1;
			for (int i = 0; i < 4; i++) {
				int zx = a1 + dx[i];
				int zy = a2 + dy[i];
				if (0 <= zx && zx < n && 0 <= zy && zy < n) {
					if (visit[zx][zy] == false&&(graph[zx][zy]==0||graph[zx][zy]==3)) {

						q.add(new go(zx, zy, a.depth + 1));
						visit[zx][zy] = true;
					}
				}
			}

			
		}

		if(count==0)
			return 1;
		return 0;

	}
		
		
		
		
	private static void update(go a, int len) {
		// TODO Auto-generated method stub
	
		go g=a;
		int h=len;
		
		if (h >= 0) {
			if (h < val) {
				val = h;
				tx = g.x;
				ty = g.y;
			} else if (h == val) {
				// 행번호가 가장 작은 승객
				if (g.x < tx) {
					tx = g.x;
					ty = g.y;
				} else if (g.x == tx) {
					if (g.y < ty) {
						tx = g.x;
						ty = g.y;
					}
				}

			}

		}
	



	}

	private static int bfs(int x, int y) {
		// TODO Auto-generated method stub

		Queue<go> q = new LinkedList<>();
		boolean visit[][] = new boolean[n][n];
		q.add(new go(taxi.x, taxi.y, 0));

		int dx[] = { -1, 0, 1, 0 };
		int dy[] = { 0, 1, 0, -1 };
		visit[taxi.x][taxi.y]=true;
		while (!q.isEmpty()) {
			go a = q.poll();
			int a1 = a.x;
			int a2 = a.y;
			if (a1 == x && a2 == y) {
				return a.depth;
			}
			for (int i = 0; i < 4; i++) {
				int zx = a1 + dx[i];
				int zy = a2 + dy[i];
				if (0 <= zx && zx < n && 0 <= zy && zy < n) {
					if (visit[zx][zy] == false&&(graph[zx][zy]==0||graph[zx][zy]==3)) {
						if (zx == x && zy == y)
							return a.depth + 1;
						q.add(new go(zx, zy, a.depth + 1));
						visit[zx][zy] = true;
					}
				}
			}

		}

		return -1;
	}

}