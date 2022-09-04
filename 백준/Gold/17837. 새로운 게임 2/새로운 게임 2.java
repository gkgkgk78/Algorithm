import java.awt.geom.Area;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	static int graph[][];
	static List<Integer> temp[][];
	static int n;
	static int k;
	static ArrayList<go> hi;

	static class go {
		int x, y;
		int dir;
		int no;
		Stack<go> stack = new Stack<>();

		public go(int x, int y, int dir,int no) {
			this.x = x;
			this.y = y;
			this.dir = dir;
			this.no=no;
		}
	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		// 이동하려는 칸이 흰색인 경우에는 같이 이동을 하도록 하자

		// 이동할시에는 같이 이동을 하고 순서를 바꾸도록 하자

		// 파란색인 경우에는 말의 이동방향을 반대로 하고 한칸이동

		StringTokenizer s = new StringTokenizer(in.readLine(), " ");
		n = Integer.parseInt(s.nextToken());
		k = Integer.parseInt(s.nextToken());
		hi = new ArrayList<>();
		temp = new ArrayList[n][n];
		graph=new int[n][n];
		for (int i = 0; i < n; i++) {
			s = new StringTokenizer(in.readLine(), " ");
			for (int j = 0; j < n; j++) {
				graph[i][j] = Integer.parseInt(s.nextToken());
				temp[i][j]=new ArrayList<>();
			}

		}
		for (int i = 0; i < k; i++) {
			s = new StringTokenizer(in.readLine(), " ");
			int a1, a2, a3;
			a1 = Integer.parseInt(s.nextToken());
			a2 = Integer.parseInt(s.nextToken());
			a3 = Integer.parseInt(s.nextToken());
			hi.add(new go(a1 - 1, a2 - 1, a3 - 1,i));
			temp[a1-1][a2-1].add(i);
		}

		int resu=2;
		for (int i = 1; i <=1000; i++) {
			if(i>=2) {
				resu=7;
				//System.out.println("22");
			}
			int j=game();
			if(i>=2) {
				resu=7;

			}
//			for (int i1 = 0; i1 < n; i1++) {
//				for(int j1=0;j1<n;j1++) {
//					System.out.print((temp[i1][j1])+" ");
//				}
//				System.out.println();
//			}
//			System.out.println();
			if (j==1) {
				System.out.println(i);
				System.exit(0);
			}
			int t=find();
			if (t==1) {
				System.out.println(i);
				System.exit(0);
			}

			
		
		}
		System.out.println(-1);

	}

	private static int find() {
		// TODO Auto-generated method stub
		for (int i = 0; i < k; i++) {
			go u = hi.get(i);
			int ch=temp[u.x][u.y].size();
			
			//System.out.println(u.x+" "+u.y+" "+(temp[u.x][u.y]));
			if(ch>=4)
				return 1;

		}
		return 0;
	}

	private static int game() {
		// TODO Auto-generated method stub
		int dx[] = { 0, 0, -1, 1 };
		int dy[] = { 1, -1, 0, 0 };
		for (int i = 0; i < k; i++) {
			go u = hi.get(i);
			int x = u.x;
			int y = u.y;
			int zx = x + dx[u.dir];
			int zy = y + dy[u.dir];

			if (0 <= zx && zx < n && 0 <= zy && zy < n) {
				if (graph[zx][zy] == 0) {
					move_white(i);
				} else if (graph[zx][zy] == 1) {
					move_red(i);
				} else if (graph[zx][zy] == 2) {
					move_blue(i);
				}

			} else {
				move_blue(i);
			}
//			System.out.println(i);
//			for (int i1 = 0; i1 < n; i1++) {
//				for(int j1=0;j1<n;j1++) {
//					System.out.print((temp[i1][j1])+" ");
//				}
//				System.out.println();
//			}
//			System.out.println();
			for (int i1 = 0; i1 < k; i1++) {
				go u1 = hi.get(i1);
				int ch=temp[u1.x][u1.y].size();
				
				//System.out.println(u.x+" "+u.y+" "+(temp[u.x][u.y]));
				if(ch>=4)
					return 1;

			}
			
		}
		return 0;
	}

	private static void move_white(int i) {
		// TODO Auto-generated method stub
		// 말의위에 다른 말이 있는 경우
		int dx[] = { 0, 0, -1, 1 };
		int dy[] = { 1, -1, 0, 0 };

		go u = hi.get(i);
		int x = u.x;
		int y = u.y;
		int zx = x + dx[u.dir];
		int zy = y + dy[u.dir];

		if (temp[x][y].size() > 0) {
			int check = 0;
			for (int j : temp[x][y]) {
				go h = hi.get(j);
				if (i==h.no)
					check = 1;
				if (check == 1) {		
				h.x = zx;
				h.y = zy;
				temp[zx][zy].add(j);
				}
				
			}
			for (int j = temp[x][y].size() - 1; j >= 0; j--) {
				int a = temp[x][y].get(j);
				go h = hi.get(a);
				if (i==h.no) {
					temp[x][y].remove(j);
					break;
				} else {
					temp[x][y].remove(j);
				}
			}
			// temp[zx][zy]=new ArrayList<>();
		} 
		else
		{
			u.x=zx;
			u.y=zy;
			temp[zx][zy].add(i);
		}

	}

	private static void move_red(int i) {
		// TODO Auto-generated method stub
		int dx[] = { 0, 0, -1, 1 };
		int dy[] = { 1, -1, 0, 0 };

		go u = hi.get(i);
		int x = u.x;
		int y = u.y;
		int zx = x + dx[u.dir];
		int zy = y + dy[u.dir];
		if (temp[x][y].size() > 0) {
			int check = 0;
			for (int j = temp[x][y].size() - 1; j >= 0; j--) {
				int a = temp[x][y].get(j);
				go h = hi.get(a);
				if (i==h.no)
					check = 1;
				
				h.x = zx;
				h.y = zy;
	
				
				temp[zx][zy].add(a);
				if (check == 1) {
					break;
				}
			}
			for (int j = temp[x][y].size() - 1; j >= 0; j--) {
				int a = temp[x][y].get(j);
				go h = hi.get(a);
				if (i==h.no) {
					temp[x][y].remove(j);
					break;
				} else {
					temp[x][y].remove(j);
				}
			}
			// temp[zx][zy]=new ArrayList<>();
		} 
		else
		{
			u.x=zx;
			u.y=zy;
			temp[zx][zy].add(i);
		}

	}

	private static void move_blue(int i) {
		// TODO Auto-generated method stub
		// 파란색인 경우에는 말의 이동방향을 반대로 하고 한칸 이동을 한다
		int dx[] = { 0, 0, -1, 1 };
		int dy[] = { 1, -1, 0, 0 };

		go u = hi.get(i);
		int x = u.x;
		int y = u.y;
		int zx = x + dx[u.dir];
		int zy = y + dy[u.dir];
//		if (0 <= x && x < n && 0 <= y && y < n) {
//			for (int j = temp[x][y].size() - 1; j >= 0; j--) {
//				Integer h = temp[x][y].get(j);
//				go a = hi.get(h);
//				if (i==a.no) {
//					temp[x][y].remove(j);
//					break;
//				}
//			}
//		}
		int di = u.dir;
		//System.out.println();
		//System.out.println(x+" "+y);
		//System.out.println(zx+" "+zy+" "+u.dir);
		if (di == 0) {
			u.dir = 1;
		} else if (di == 1) {
			u.dir = 0;
		} else if (di == 2) {
			u.dir = 3;
		} else if (di == 3) {
			u.dir = 2;
		}
		
		// 이동방향을 반대로 한다/
		zx = x + dx[u.dir];
		zy = y + dy[u.dir];
		//System.out.println(zx+" "+zy+" "+u.dir);
		if (0 <= zx && zx < n && 0 <= zy && zy < n) {
		if (graph[zx][zy] == 2) {
			u.x = x;
			u.y = y;
			//temp[x][y].add(i);
		} else {
			//u.x = zx;
			//u.y = zy;
			//temp[zx][zy].add(i);
			//temp[x][y].add(i);
			if (graph[zx][zy] == 0) {
				move_white(i);
			}
			else if (graph[zx][zy] == 1)
			{
				move_red(i);
			}
		}
		}
		else
		{
			u.x = x;
			u.y = y;
			//temp[x][y].add(i);
		}

	}

}