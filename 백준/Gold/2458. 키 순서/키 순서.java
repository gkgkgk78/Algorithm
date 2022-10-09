import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

	static ArrayList<Integer>[] up;
	static ArrayList<Integer>[] down;
	static int n;
	static int result = 0;
	static int visit[];
	static int check;

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer s = new StringTokenizer(in.readLine(), " ");
		n = Integer.parseInt(s.nextToken());
		int m = Integer.parseInt(s.nextToken());
		up = new ArrayList[n + 1];
		down = new ArrayList[n + 1];
		visit = new int[n + 1];
		result = 0;
		for (int j = 0; j <= n; j++) {

			up[j] = new ArrayList<>();
			down[j] = new ArrayList<>();
		}
		for (int j = 0; j < m; j++) {
			int a1, a2;
			s = new StringTokenizer(in.readLine(), " ");
			a1 = Integer.parseInt(s.nextToken());
			a2 = Integer.parseInt(s.nextToken());
			up[a1].add(a2);
			down[a2].add(a1);

		}

		for (int j = 1; j <= n; j++) {
			visit = new int[n + 1];
			check = 1;
			visit[j] = 1;

			dfs(j, 0);
			dfs(j, 1);
			if (check == n)
				result++;

		}

		System.out.println(result);

	}

	private static void dfs(int j, int now) {
		// TODO Auto-generated method stub

		if (now == 0) {
			for (Integer a : down[j]) {
				if (visit[a] == 0) {
					visit[a] = 1;
					check++;
					dfs(a, now);
				}

			}
		}
		if (now == 1) {
			for (Integer a : up[j]) {
				if (visit[a] == 0) {
					visit[a] = 1;
					check++;
					dfs(a, now);
				}

			}
		}
	}

}