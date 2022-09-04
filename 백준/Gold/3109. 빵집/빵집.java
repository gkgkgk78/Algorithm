import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static StringBuffer buffer;
	static char graph[][];
	static int count = 0;
	static int visit[][];

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub

		buffer = new StringBuffer();
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		int r, c;
		StringTokenizer s = new StringTokenizer(in.readLine());
		r = Integer.parseInt(s.nextToken());
		c = Integer.parseInt(s.nextToken());

		graph = new char[r][c];
		visit = new int[r][c];

		for (int i = 0; i < r; i++) {
			char temp[] = in.readLine().toCharArray();
			for (int j = 0; j < c; j++) {
				graph[i][j] = temp[j];
			}
		}
		for (int i = 0; i < r; i++) {
			dfs(i, 0, r, c);
		}
		System.out.println(count);
	}

	private static int dfs(int i, int j, int r, int c) {
		// TODO Auto-generated method stub
		int dx[] = { -1, 0, 1 };
		int dy[] = { 1, 1, 1 };
		if (j == c - 1) {
			count++;
			return 1;
		}
		

		for (int i1 = 0; i1 < 3; i1++) {
			int tx = dx[i1] + i;
			int ty = dy[i1] + j;
			int z = 0;
			if (0 <= tx && tx < r && 0 <= ty && ty < c)// 갈수있다면 탐색을 해보도록 하자
			{
				if (graph[tx][ty] != 'x') {
					if (visit[tx][ty] == 0) {
						visit[tx][ty] = 1;
						z = dfs(tx, ty, r, c);
						if (z == 1) {
							return 1;
						} 
					}
				}

			}

		}

		return 0;
	}

}