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

	static int numbers[];
	static int n, m, h;

	public static class go {
		int x, y;

		public go(int x, int y) {

			this.x = x;
			this.y = y;
		}

	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer s = new StringTokenizer(in.readLine());

		// 세로선, 가로선, 각세로선마다 가로선 놓을수 있는 위치
		n = Integer.parseInt(s.nextToken());
		m = Integer.parseInt(s.nextToken());
		h = Integer.parseInt(s.nextToken());

		graph = new int[h][n];
		// 정답이 3보다 큰값이면 -1을 출력하고 불가능한 경우에는 -1을 추가한다.

		for (int i = 0; i < m; i++) {
			s = new StringTokenizer(in.readLine());
			int a1 = Integer.parseInt(s.nextToken());
			int a2 = Integer.parseInt(s.nextToken());
			graph[a1 - 1][a2 - 1] = 1;// 이렇게 해서 가로선을 놓아둠
		}

		ArrayList<go> hi = new ArrayList<>();
		// 찾을수 있는 모든 시작점을 찾도록 하자
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < n - 1; j++) {
				if (graph[i][j] == 0) {
					// int a1 = j - 2;
					int a2 = j - 1;
					int a3 = j + 1;
					// int a4 = j + 2;
					// if (a1 >= 0) {if (graph[i][a1] == 1)continue;}
					if (a2 >= 0) {
						if (graph[i][a2] == 1)
							continue;
					}
					if (a3 < n) {
						if (graph[i][a3] == 1)
							continue;
					}
					// if (a4 <n) {if (graph[i][a4] == 1)continue;}
					hi.add(new go(i, j));
				}
			}
		}
		int check=0;		
		for (int i = 0; i < n; i++) {
			int ch = dfs(0, i, 0);
			if(ch!=i)
			{
				check=1;
				break;
			}
		}
		if(check==0)
		{
			System.out.println(0);
			return;
		}
		for (int i = 1; i < 4; i++) {
			numbers = new int[i];
			comb(0, 0, i, hi);// cnt start end
		}
		System.out.println(-1);

	}

	private static void comb(int cnt, int start, int end, ArrayList<go> hi) {
		// TODO Auto-generated method stub
		if (cnt == end) {
			//System.out.println(Arrays.toString(numbers));
			for (int i = 0; i < numbers.length; i++) {
				go temp = hi.get(numbers[i]);
				graph[temp.x][temp.y] = 1;
			}

			int count = 0;
			for (int i = 0; i < n; i++) {
				int ch = dfs(0, i, 0);
				if (ch != i) {
					count = 1;
					break;
				}
			}
			for (int i = 0; i < numbers.length; i++) {
				go temp = hi.get(numbers[i]);
				graph[temp.x][temp.y] = 0;
			}
			if (count == 0) {
				System.out.println(end);
				System.exit(0);
			}
			return;
		}
		int k = hi.size();
		for (int i = start; i < k; i++) {
			numbers[cnt] = i;
			comb(cnt + 1, i + 1, end, hi);

		}

	}

	private static int dfs(int k, int i, int down) {

		// TODO Auto-generated method stub
		int x = k;
		int y = i;
//		Queue<go>q=new LinkedList<>();
		int g = 0;
		// visit[x][y] = 1;

		if (down == 1) {
			if (x + 1 >= h)
				return i;
			g = dfs(x + 1, y, 0);
		} else {
			// 오른쪽 탐색

			if (graph[x][y] == 1) {
				g = dfs(x, y + 1, 1);
			}

			// 왼쪽 탐색
			else if (y - 1 >= 0) {
				if (graph[x][y - 1] == 1)
					g = dfs(x, y - 1, 1);
				else {
					if (x + 1 >= h)
						return i;
					g = dfs(x + 1, y, 0);
				}
			}
			// 둘다 아니면 걍 내려감
			else {
				if (x + 1 >= h)
					return i;
				g = dfs(x + 1, y, 0);
			}
		}
		return g;

	}

}