import java.awt.BufferCapabilities;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int graph[][];
	static shark sha;
	static ArrayList<fish> fis;
	static int n;
	static int result = 0;

	static class shark {
		int x, y, size, count;

		public shark(int x, int y, int size, int count) {

			this.x = x;
			this.y = y;
			this.size = size;
			this.count = count;
		}

	}

	static class fish {
		int x, y, size;
		int time;

		public fish(int x, int y, int time, int size) {

			this.x = x;
			this.y = y;
			this.size = size;
			this.time = time;
		}

		public fish(int x, int y, int size) {

			this.x = x;
			this.y = y;
			this.size = size;
		}
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		n = Integer.parseInt(in.readLine());
		fis = new ArrayList<>();
		graph = new int[n][n];
		for (int i = 0; i < n; i++) {
			StringTokenizer s = new StringTokenizer(in.readLine());
			for (int j = 0; j < n; j++) {
				graph[i][j] = Integer.parseInt(s.nextToken());
				if (graph[i][j] == 9) {

					sha = new shark(i, j, 2, 0);
					graph[i][j] = 0;
				} else if (graph[i][j] >= 1 && graph[i][j] <= 6) {
					fis.add(new fish(i, j, graph[i][j]));
				}
			}

		}

		move();

	}

	private static void move() {
		// TODO Auto-generated method stub

		while (true) {

			// 이동시 크기가 같거나 작은 물고기는 이동하기만 하면되
			// 먹을수 있는것은 나보다 작은 물고기임
			ArrayList<fish> temp = new ArrayList<>();

			int x = -1;
			int y = -1;
			int size = Integer.MAX_VALUE;

			int sh_x = sha.x;
			int sh_y = sha.y;
			int leng=-1;
			// 우선먹을수 있는 물고기들부터 파악을하자
			for (fish f : fis) {
				// int leng=Math.abs(f.x-sh_x)+Math.abs(f.y-sh_y);\
				if (graph[f.x][f.y] < sha.size)
					leng = bfs(f.x, f.y,sha.size);
				else
					leng=-1;
				if (leng > 0) {
					if (leng < size&&leng!=-1) {
						temp = new ArrayList<>();
						x = f.x;
						y = f.y;
						size = leng;
						temp.add(new fish(f.x, f.y, f.size));
					} else if (leng == size) {
						// 가까운 물고기 많다면 우선 가장 위에 있는 물고기
						// 그리고 가장 왼쪽에 있는 물고기를 선택
						if (f.x < x) {
							x = f.x;
							y = f.y;
							temp = new ArrayList<>();
							temp.add(new fish(f.x, f.y, f.size));
						} else if (f.x == x) {
							if (f.y < y) {
								y = f.y;
								temp = new ArrayList<>();
								temp.add(new fish(f.x, f.y, f.size));
							}
						}
					}
				}
			}
			if (temp.size() == 0) {
				System.out.println(result);
				return;
			}
			graph[x][y]=0;
			sha.count++;
			//System.out.println(size);
			result+=size;
			sha.x=x;
			sha.y=y;
			if(sha.count==sha.size)
			{
				sha.size++;
				sha.count=0;
			}

			// 잡은 물고기를 삭제하도록 하자

			for (int i = fis.size() - 1; i >= 0; i--) {
				fish hi = fis.get(i);
				if (hi.x == x && hi.y == y) {
					fis.remove(i);
					break;

				}

			}

//			for (int i = 0; i < n; i++) {
//
//				System.out.println(Arrays.toString(graph[i]));
//
//			}
//			System.out.println();

		}
	}

	private static int bfs(int x, int y, int size) {

		int dx[] = { -1, 0, 1, 0 };
		int dy[] = { 0, 1, 0, -1 };
		Queue<fish> q = new LinkedList<>();

		q.add(new fish(sha.x, sha.y, 0, 0));
		int visit[][] = new int[n][n];
		visit[sha.x][sha.y] = 1;
		int ss = sha.size;
		while (!q.isEmpty()) {
			fish a = q.poll();
			int tx = a.x;
			int ty = a.y;
			int time = a.time;
			for (int i = 0; i < 4; i++) {
				int zx = tx + dx[i];
				int zy = ty + dy[i];
				if (0 <= zx && zx < n && 0 <= zy && zy < n) {
					if (visit[zx][zy] == 0 && graph[zx][zy] <= size) {
						q.add(new fish(zx, zy, time + 1, 0));
						visit[zx][zy] = 1;
						if (zx == x && zy == y) {
							return time + 1;
//							int add = graph[zx][zy];
//							sha.count++;
//							if (sha.size == sha.count) {
//								sha.size++;
//								sha.count = 0;
//							}
//							sha.x=x;
//							sha.y=y;
//							
//							result += (time+1 );
//
//							System.out.println(zx+" "+zy+" "+(time+1)+" "+sha.size+" "+sha.count);
//							graph[zx][zy] = 0;
//							
						}
					}

				}

			}

		}
		return -1;

	}

}