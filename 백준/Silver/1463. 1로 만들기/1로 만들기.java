import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(in.readLine());

		int d[] = new int[n + 1];
		for (int i = 1; i <= n; i++) {
			d[i] = Integer.MAX_VALUE;
		}
		d[n] = 0;
		if (n == 1) {
			System.out.println(0);
			System.exit(0);
		}
		Queue<Integer> q = new LinkedList<Integer>();
		q.add(n);
		while (!q.isEmpty()) {
			n = q.poll();
			if (n % 3 == 0) {
				int z = n / 3;
				d[z] = Math.min(d[n] + 1, d[z]);
				q.add(z);
				if (z == 1) {
					System.out.println(d[1]);
					System.exit(0);
				}

			}
			if (n % 2 == 0) {
				int z = n / 2;
				d[z] = Math.min(d[n] + 1, d[z]);
				q.add(z);
				if (z == 1) {
					System.out.println(d[1]);
					System.exit(0);
				}

			}

			d[n - 1] = Math.min(d[n] + 1, d[n - 1]);
			q.add(n - 1);
			if (n - 1 == 1) {
				System.out.println(d[1]);
				System.exit(0);
			}

		}

	}

}