import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


public class Main {

	static int n, m;
	static List<node>[] hi;
	static int distance[];
	static int INF = 100000000;

	static class node implements Comparable<node> {
		int no, weight;

		public node(int no, int weight) {
			this.no = no;
			this.weight = weight;
		}

		@Override
		public int compareTo(node o) {
			// TODO Auto-generated method stub
			return Integer.compare(this.weight, o.weight);
		}

	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		n = Integer.parseInt(in.readLine());
		m = Integer.parseInt(in.readLine());
		StringTokenizer s ;
		hi = new ArrayList[n + 1];
		distance=new int[n+1];
		Arrays.fill(distance, INF);
		int a1, a2, a3;

		for (int i = 1; i <= n; i++) {
			hi[i] = new ArrayList<>();
		}
		for (int i = 0; i < m; i++) {
			s = new StringTokenizer(in.readLine(), " ");
			a1 = Integer.parseInt(s.nextToken());
			a2 = Integer.parseInt(s.nextToken());
			a3 = Integer.parseInt(s.nextToken());
			hi[a1].add(new node(a2, a3));

		}
		s = new StringTokenizer(in.readLine(), " ");
		int start = Integer.parseInt(s.nextToken());
		int last = Integer.parseInt(s.nextToken());

		distance[start] = 0;
		dijk(start);
		System.out.println(distance[last]);
	}

	private static void dijk(int start) {
		// TODO Auto-generated method stub
		PriorityQueue<node> q = new PriorityQueue<>();
		boolean visit[] = new boolean[n + 1];
		q.add(new node(start, 0));
		while (!q.isEmpty()) {
			node aa = q.poll();
			int nn = aa.no;
			int ll = aa.weight;
			if (visit[nn] == true)
				continue;
			visit[nn] = true;

			for (node h : hi[nn]) {
				if (distance[h.no] > distance[nn] + h.weight) {
					distance[h.no] = distance[nn] + h.weight;
					q.add(new node(h.no, distance[h.no]));
				}
			}

		}

	}

}