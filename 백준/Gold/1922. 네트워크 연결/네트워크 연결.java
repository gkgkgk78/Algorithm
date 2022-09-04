import java.awt.BufferCapabilities;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

	static int parents[];
	static int n;

	static void make() {
		for (int i = 1; i <= n; i++) {
			parents[i] = i;

		}

	}

	static int find(int a) {
		if (parents[a] == a)
			return a;
		return parents[a] = find(parents[a]);

	}

	static int union(int a, int b) {

		int a1 = find(a);
		int a2 = find(b);

		if (a1 == a2)
			return 0;

		if (a1 < a2)
			parents[a2] = a1;
		else
			parents[a1] = a2;
		return 1;

	}

	static class go implements Comparable<go> {
		int x, y, z;

		public go(int x, int y, int z) {
			this.x = x;
			this.y = y;
			this.z = z;
		}

		@Override
		public int compareTo(go o) {
			// TODO Auto-generated method stub
			return Integer.compare(this.z, o.z);
		}

	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(in.readLine());
		parents=new int[n+1];
		make();
		int e = Integer.parseInt(in.readLine());
		int a1, a2, a3;
		StringTokenizer s;
		
		ArrayList<go> hi = new ArrayList<>();
		int count = 0;
		for (int i = 0; i < e; i++) {
			s = new StringTokenizer(in.readLine());
			a1 = Integer.parseInt(s.nextToken());
			a2 = Integer.parseInt(s.nextToken());
			a3 = Integer.parseInt(s.nextToken());
			hi.add(new go(a1, a2, a3));
		}

		Collections.sort(hi);
		int result = 0;
		for (go go : hi) {
			a1 = go.x;
			a2 = go.y;
			a3 = go.z;
			if (a1 != a2) {
				int check = union(a1, a2);
				if (check == 1) {
					count++;
					result += a3;
				}
				if (check == n)
					break;
			}
		}
		System.out.println(result);

	}

}
