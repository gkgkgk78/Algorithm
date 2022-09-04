import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static char graph[][];
	static int result = 0;
	static int fx, fy;
	static int visit[][];
	static int r, c;

	static class go {
		int x, y;
		int z;

		public go(int x, int y) {

			this.x = x;
			this.y = y;
		}

		public go(int x, int y, int z) {

			this.x = x;
			this.y = y;
			this.z = z;
		}

	}

	public static void main(String[] args) throws IOException {

		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer s = new StringTokenizer(in.readLine());

		r = Integer.parseInt(s.nextToken());
		c = Integer.parseInt(s.nextToken());
		graph = new char[r][c];
		Queue<go> water = new LinkedList<>();
		Queue<go> gsm = new LinkedList<>();
		visit = new int[r][c];
		for (int i = 0; i < r; i++) {
			char temp[] = in.readLine().toCharArray();
			for (int j = 0; j < c; j++) {
				graph[i][j] = temp[j];
				if (graph[i][j] == 'D') {
					fx = i;
					fy = j;
				} else if (graph[i][j] == '*')

				{
					water.add(new go(i, j));
				} else if (graph[i][j] == 'S')

				{
					gsm.add(new go(i, j));
				}
			}

		}

		// 우선 물부터 차오르고

		// 그다음에 고슴도치 이동을 함
		
		while (true) {
			result+=1;
			bfs(water, 0);
			bfs(gsm, 1);
			
//			for (int i = 0; i < r; i++) {
//				System.out.println(Arrays.toString(graph[i]));
//			}
//			System.out.println();
			if(gsm.size()==0)
				break;
			
			
		}
		System.out.println("KAKTUS");


	}

	private static void bfs(Queue<go> q, int t) {
		// TODO Auto-generated method stub

		Queue<go> temp = new LinkedList<>();
		int dx[] = { -1, 0, 1, 0 };
		int dy[] = { 0, 1, 0, -1 };
		
		while (!q.isEmpty()) {
			go a = q.poll();
			int a1 = a.x;
			int a2 = a.y;
			
			for (int i = 0; i < 4; i++) {
				int tx = a1 + dx[i];
				int ty = a2 + dy[i];

				if (0 <= tx && tx < r && 0 <= ty && ty < c) {
					if (visit[tx][ty] == 0) {
						if(t==1)
						{
							if(graph[tx][ty]=='D')
							{
								System.out.println(result);
								System.exit(0);
							}
						}
						if(graph[tx][ty]=='.')
						{
							
							visit[tx][ty]=1;
							if(t==0)
								graph[tx][ty]='*';
							else if(t==1)
								graph[tx][ty]='S';
							temp.add(new go(tx,ty));
						}
					}

				}
			}

		}
		
		
		for (go a : temp) {
			q.add(new go(a.x,a.y));
		}
		
		
		

	}

}