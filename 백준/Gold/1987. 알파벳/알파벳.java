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

	public static class go {
		int x;
		int y;

		public go(int x, int y) {

			this.x = x;
			this.y = y;
		}

		public go() {

		}

	}

	static StringBuffer buffer;
	static int count;
	static int visit[];

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		
		buffer = new StringBuffer();
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer s = new StringTokenizer(in.readLine());
		int r, c;
		r = Integer.parseInt(s.nextToken());
		c = Integer.parseInt(s.nextToken());
		count = 0;
		char graph[][] = new char[r][c];
		visit = new int[26];
		for (int i = 0; i < r; i++) {
			char[] is = in.readLine().toCharArray();
			for (int j = 0; j < c; j++) {
				graph[i][j] = is[j];
			}

		}
		dfs(graph, 0, 0, 0, r, c);
		System.out.println(count);

	}

	private static void dfs(char[][] graph, int x, int y, int cou, int r, int c) {
		// TODO Auto-generated method stub

		if (visit[graph[x][y] - 'A'] == 1) {
			if (cou > count)
				count = cou;
			return;
		}
		int dx[] = { -1, 0, 1, 0 };
		int dy[] = { 0, 1, 0, -1 };
		visit[graph[x][y] - 'A'] = 1;
		cou++;

		for (int i = 0; i < 4; i++) {
			int tx = x + dx[i];
			int ty = y + dy[i];
			if (0 <= tx && tx < r && 0 <= ty && ty < c) {
				dfs(graph, tx, ty, cou, r, c);
			}
		}
		visit[graph[x][y] - 'A'] = 0;
	}

}