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
	static int visit[][];
	static int n, m;
	static int sh,wo;
	public static class go {
		int x, y;

		public go(int x, int y) {

			this.x = x;
			this.y = y;
		}

	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub

		

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer s = new StringTokenizer(in.readLine());
		n = Integer.parseInt(s.nextToken());
		m = Integer.parseInt(s.nextToken());

		char[][] graph = new char[n][m];
		visit=new int [n][m];
		sh=0;
		wo=0;
		for (int i = 0; i < n; i++) {

			char[] ss = in.readLine().toCharArray();
			for (int j = 0; j < m; j++) {
				graph[i][j] = ss[j];

			}

		}
	
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (visit[i][j] == 0) {
					bfs(graph, i, j);
				}
			}
		}
		System.out.print(sh+" "+wo);

	}

	private static void bfs(char[][] graph, int x, int y) {

		Queue<go> q = new LinkedList<>();
		ArrayList<go> sheep = new ArrayList<>();
		ArrayList<go> wolf = new ArrayList<>();

		visit[x][y] = 1;
		int dx[] = { -1, 0, 1, 0 };
		int dy[] = { 0, 1, 0, -1 };
		q.add(new go(x, y));

		while (!q.isEmpty()) {
			go now = q.poll();
			int a1, a2;
			a1 = now.x;
			a2 = now.y;
			for (int i = 0; i < 4; i++) {
				int tx = a1 + dx[i];
				int ty = a2 + dy[i];
				if (0 <= tx && tx < n && 0 <= ty && ty < m) {
					if (visit[tx][ty] == 0 && graph[tx][ty] != '#') {
						q.add(new go(tx, ty));
						visit[tx][ty] = 1;
						if (graph[tx][ty] == 'o')
							sheep.add(new go(tx, ty));
						else if (graph[tx][ty] == 'v')
							wolf.add(new go(tx, ty));

					}

				}

			}

		}
		//늑대 숙청
		if(sheep.size()>wolf.size())
		{
			sh+=sheep.size();
			for (go aa: wolf) {
				graph[aa.x][aa.y]='.';
			}
			
			
		}
		else
		{
			wo+=wolf.size();
			for (go aa: sheep) {
				graph[aa.x][aa.y]='.';
			}
			
			
			
		}
		
		

	}

}