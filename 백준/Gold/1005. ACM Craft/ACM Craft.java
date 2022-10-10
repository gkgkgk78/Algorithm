import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int time[];
	static List<List<Integer>> list;
	static int degree[];
	static int n;

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(in.readLine());

		for (int i = 0; i < t; i++) {
			int k;
			StringTokenizer s = new StringTokenizer(in.readLine(), " ");
			n = Integer.parseInt(s.nextToken());
			k = Integer.parseInt(s.nextToken());
			s = new StringTokenizer(in.readLine(), " ");
			time = new int[n];
			list = new ArrayList<>();
			degree = new int[n];
			for (int j = 0; j < n; j++) {
				list.add(new ArrayList<>());
				time[j] = Integer.parseInt(s.nextToken());
			}
			for (int j = 0; j < k; j++) {
				s = new StringTokenizer(in.readLine(), " ");
				int a1 = Integer.parseInt(s.nextToken());
				int a2 = Integer.parseInt(s.nextToken());
				a1--;
				a2--;
				list.get(a1).add(a2);
				degree[a2] += 1;
			}
			int z=Integer.parseInt(in.readLine());
			topo(z);

		}

	}

	private static void topo(int z1) {
		// TODO Auto-generated method stub
		Queue<Integer> q = new LinkedList<>();
		int max[] = new int[n];
		for (int i = 0; i < n; i++) {
			max[i] = time[i];
			if (degree[i] == 0)
				q.add(i);

		}
		while (!q.isEmpty()) {

			int z = q.poll();
			for (Integer i : list.get(z)) {
				degree[i] -= 1;

				max[i] = Math.max(max[i], max[z] + time[i]);

				if (degree[i] == 0) {
					q.add(i);
				}

			}

		}

		System.out.println(max[z1-1]);
		

	}

}