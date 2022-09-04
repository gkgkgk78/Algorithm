import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static StringBuffer buffer;
	static int graph[][];

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		buffer = new StringBuffer();

		graph = new int[101][101];
		int result = 0;
		StringTokenizer s = new StringTokenizer(in.readLine());
		int n = Integer.parseInt(s.nextToken());
		int a1, a2, a3, a4;
		for (int i = 0; i < n; i++) {
			s = new StringTokenizer(in.readLine());
			a1 = Integer.parseInt(s.nextToken());
			a2 = Integer.parseInt(s.nextToken());
			a3 = Integer.parseInt(s.nextToken());
			a4 = Integer.parseInt(s.nextToken());

			game(a1, a2, a3, a4);
//			for (int i1 = 0; i1 < 8; i1++) {
//				System.out.println(Arrays.toString(graph[i1]));
//			}
//			System.out.println();

		}
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				if (graph[i][j] == 1) {
					if (graph[i][j + 1] == 1 && graph[i + 1][j] == 1 && graph[i + 1][j + 1] == 1)
						result++;
				}

			}

		}

		System.out.println(result);

	}

	private static void game(int x, int y, int dir, int gen) {
		// TODO Auto-generated method stub

		int s = 1;
		ArrayList<Integer> q = new ArrayList<>();
		q.add(dir);
		int tx = x;
		int ty = y;
		graph[x][y] = 1;
		if (dir == 0) {
			tx += 1;
			graph[tx][ty] = 1;

		} else if (dir == 1) {

			ty -= 1;
			graph[tx][ty] = 1;

		} else if (dir == 2) {

			tx -= 1;
			graph[tx][ty] = 1;

		} else if (dir == 3) {

			ty += 1;
			graph[tx][ty] = 1;

		}
		while (s <= gen) {
			ArrayList<Integer> temp = new ArrayList<>();
			for (int i = q.size() - 1; i >= 0; i--) {
				int a1 = q.get(i);
				if (a1 == 0) {
					int dd = 1;
					ty -= 1;
					graph[tx][ty] = 1;
					temp.add(dd);

				} else if (a1 == 1) {
					int dd = 2;
					tx -= 1;
					graph[tx][ty] = 1;
					temp.add(dd);

				} else if (a1 == 2) {
					int dd = 3;
					ty += 1;
					graph[tx][ty] = 1;
					temp.add(dd);
				} else if (a1 == 3) {
					int dd = 0;
					tx += 1;
					graph[tx][ty] = 1;
					temp.add(dd);
				}
			}

			for (int i = 0; i < temp.size(); i++) {
				q.add(temp.get(i));
			}

			s++;

		}

	}

}