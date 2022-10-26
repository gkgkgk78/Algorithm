import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int r, c;
	static char[][] graph;
	static int sx, sy, fx, fy;
	static int gp[][][];
	static int visit[][];
	static char ss;

	// 0북 1동 2남 3서
	static int gx = -1, gy = -1, gdir = -1;

	public static void main(String[] args) throws IOException {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer s = new StringTokenizer(in.readLine(), " ");
		r = Integer.parseInt(s.nextToken());
		c = Integer.parseInt(s.nextToken());
		graph = new char[r][c];
		gp = new int[r][c][4];
		for (int i = 0; i < r; i++) {
			char temp[] = in.readLine().toCharArray();
			for (int j = 0; j < c; j++) {
				graph[i][j] = temp[j];
				if (temp[j] == 'M') {
					sx = i;
					sy = j;
				} else if (temp[j] == 'Z') {
					fx = i;
					fy = j;
				}
			}
		}

		// m에서 진행을 하고 //z에서 진행을 해보도록 하자
		game();

	}

	private static void game() {
		// TODO Auto-generated method stub

		int dx[] = { -1, 0, 1, 0 };
		int dy[] = { 0, 1, 0, -1 };
		int mx = -1;
		int my = -1;

		int dir = -1;
		
		// 파악한 방향이 내가 가고자 하는 방향과 같아야지
		// 즉 시작 점에서는 시작 할수 있는 방향을 찾지 못한 경우를 의미함,이때는 끝나는 지점을 해서 한번더 확인을 해봐야지

		
		visit=new int[r][c];
		for (int i = 0; i < 4; i++) {
			int zx,zy;
			zx=sx+dx[i];
			zy=sy+dy[i];
			if (0 <= zx && zx < r && 0 <= zy & zy < c) {
				if(graph[zx][zy]!='.'&&graph[zx][zy]!='Z')
				{
					mx=zx;
					my=zy;
					dir=i;
					break;
				}
			}
		}
		dfs(sx,sy,dir,0);
		char [] tt= {'|','-','+','1','2','3','4'};
		for (int i = 0; i < 7; i++) {
			visit=new int[r][c];
	
			graph[gx][gy]=tt[i];
			dfs(sx,sy,dir,1);
		}
		
		
		
		

	}

	private static int[] check(char d) {
		// 들어오고자 하는 좌표가 가진 방향으로 들어 올수 있는좌표들을 리턴해줌

		if (d == '|') {// 남 북 방향으로 진행 했을시에만 진입이 가능함
			int re[] = { 0, 2 };
			return re;

		} else if (d == '-') {
			int re[] = { 1, 3 };
			return re;

		} else if (d == '+') {
			int re[] = { 0, 1, 2, 3 };
			return re;

		} else if (d == '1') {
			int re[] = { 0, 3 };
			return re;
		}

		else if (d == '2') {
			int re[] = { 2, 3 };
			return re;

		} else if (d == '3') {
			int re[] = { 1, 2 };
			return re;

		} else if (d == '4') {
			int re[] = { 0, 1 };
			return re;
		}

		return null;
	}

	private static int dfs(int x, int y, int dir,int chch) {// 마지막은 0:m 1:전체 길 탐색 을 위한 것을 의미
		// TODO Auto-generated method stub

		int dx[] = { -1, 0, 1, 0 };
		int dy[] = { 0, 1, 0, -1 };

		int count = 0;
		visit[x][y]=1;
		int zx = dx[dir] + x;
		int zy = dy[dir] + y;
		
		if (0 <= zx && zx < r && 0 <= zy & zy < c) {
			if (graph[zx][zy] != 'M' && graph[zx][zy] != 'Z' && graph[zx][zy] != '.') {
				int[] temp = check(graph[zx][zy]);// 해당 하는 좌표에서 지금 내가 가진 방향으로 갈수 있는 좌표를 탐색
				if (temp != null) {
					// 내가 가진 방향에 맞는 것을 파악한다면 시작 할수 있는 좌표 임을 의미함
					for (int k = 0; k < temp.length; k++) {
						if (temp[k] == dir) {
							if (temp.length == 4) {
								if (visit[zx][zy] < 2) {
									visit[zx][zy]++;
									int u = find(zx, zy, dir);
									int z = dfs(zx, zy, u,chch);
									if (z == 1)
										return 1;

								}
							}
							if (visit[zx][zy] == 0) {
								visit[zx][zy]++;
								int u = find(zx, zy, dir);
								int z = dfs(zx, zy, u,chch);
								if (z == 1)
									return 1;
							}
							break;
						}
					}
				}
			}
			if (chch==1&&graph[zx][zy] == 'Z')// 탈출 조건을 의미함
			{
				System.out.println((gx+1)+" "+(gy+1)+" "+graph[gx][gy]);
				System.exit(0);
			}
			if (chch==0&&graph[zx][zy] == '.')// 탈출 조건을 의미함
			{
				gx=zx;
				gy=zy;
				gdir=dir;
				return 1;
			}
			
		}

		return 0;

	}

	private static int find(int zx, int zy, int dir) {
		// TODO Auto-generated method stub
		char d = graph[zx][zy];
		if (d == '|') {// 남 북 방향으로 진행 했을시에만 진입이 가능함

			return dir;

		} else if (d == '-') {
			return dir;

		} else if (d == '+') {
			return dir;

		} else if (d == '1') {
			if (dir == 0)
				return 1;
			else if (dir == 3)
				return 2;
		} else if (d == '2') {
			if (dir == 2)
				return 1;
			else if (dir == 3)
				return 0;
		} else if (d == '3') {
			if (dir == 2)
				return 3;
			else if (dir == 1)
				return 0;
		} else if (d == '4') {
			if (dir == 1)
				return 2;
			else if (dir == 0)
				return 3;
		}
		return 0;
	}

}