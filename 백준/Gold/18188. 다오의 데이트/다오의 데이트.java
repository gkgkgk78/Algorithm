import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

	static char graph[][];
	static int visit[][];
	static int nh;

	static class go {
		int x, y;
		ArrayList<String> next = new ArrayList<>();

		public go(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}
	}
	static class mak {
		char a1, a2;
		public mak(char a1, char a2) {
			this.a1 = a1;
			this.a2 = a2;
		}
	}

	static go dao;
	static List<mak> to;
	static List<String> answer;
	static int n, m;

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer s = new StringTokenizer(in.readLine(), " ");
		n = Integer.parseInt(s.nextToken());
		m = Integer.parseInt(s.nextToken());
		graph = new char[n][m];
		visit = new int[n][m];
		for (int i = 0; i < n; i++) {
			// s = new StringTokenizer(in.readLine());
			String s1 = in.readLine();
			for (int j = 0; j < m; j++) {
				graph[i][j] = s1.charAt(j);
				if (graph[i][j] == 'D') {
					dao = new go(i, j);
					graph[i][j] = '.';
				}
			}
		}
		to = new ArrayList<>();
		int h = Integer.parseInt(in.readLine());
		nh = h;
		for (int i = 0; i < h; i++) {
			char a1, a2;
			String s1 = in.readLine();
			a1 = s1.charAt(0);
			a2 = s1.charAt(2);
			to.add(new mak(a1, a2));

		}
		answer = new ArrayList<>();

		// visit[dao.x][dao.y] = 1;
		dfs(dao.x, dao.y, 0, "");

		if (answer.size() > 0) {
			System.out.println("YES");
			List<String> answea = answer;
			System.out.println(answer.get(0));
		} else
			System.out.println("NO");
	}

	private static void dfs(int x, int y, int count, String next) {
		// TODO Auto-generated method stub

		if (count < nh) {
			mak z = to.get(count);
			char z1 = ' ';
			for (int i = 0; i < 2; i++) {
				if (i == 0)
					z1 = z.a1;
				else
					z1 = z.a2;
				if (z1 == 'W') {
					if (x - 1 >= 0) {
						if (graph[x - 1][y] == 'Z') {
							answer.add(next.concat(Character.toString(z1)));
							dfs(x - 1, y, count + 1, next.concat(Character.toString(z1)));
						} else if (graph[x - 1][y] == '.') {
							dfs(x - 1, y, count + 1, next.concat(Character.toString(z1)));
						}
					}
				} else if (z1 == 'A') {
					if (y - 1 >= 0) {
						if (graph[x][y - 1] == 'Z') {
							answer.add(next.concat(Character.toString(z1)));
							dfs(x, y - 1, count + 1, next.concat(Character.toString(z1)));
						} else if (graph[x][y - 1] == '.') {
							dfs(x, y - 1, count + 1, next.concat(Character.toString(z1)));
						}
					}

				} else if (z1 == 'S') {
					if (x + 1 < n) {
						if (graph[x + 1][y] == 'Z') {
							answer.add(next.concat(Character.toString(z1)));
							dfs(x + 1, y, count + 1, next.concat(Character.toString(z1)));
						} else if (graph[x + 1][y] == '.') {
							dfs(x + 1, y, count + 1, next.concat(Character.toString(z1)));
						}
					}

				} else if (z1 == 'D') {
					if (y + 1 < m) {
						if (graph[x][y + 1] == 'Z') {
							answer.add(next.concat(Character.toString(z1)));
							dfs(x, y + 1, count + 1, next.concat(Character.toString(z1)));
						} else if (graph[x][y + 1] == '.') {
							dfs(x, y + 1, count + 1, next.concat(Character.toString(z1)));
						}
					}
				}
			}
		} else {
			return;
		}

	}

}