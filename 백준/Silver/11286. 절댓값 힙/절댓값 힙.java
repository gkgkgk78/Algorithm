import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(in.readLine());

		PriorityQueue<Integer> q = new PriorityQueue<>(new Comparator<Integer>() {

			@Override
			public int compare(Integer o1, Integer o2) {
				// TODO Auto-generated method stub
				if (Math.abs(o1) > Math.abs(o2))
					return 1;
				else if (Math.abs(o1)== Math.abs(o2))
					return o1 - o2;
				else
					return -1;
			}
			
		});

		for (int i = 0; i < n; i++) {
			int a = Integer.parseInt(in.readLine());
			if (a == 0) {
				if (q.size() == 0)
					System.out.println(0);
				else
					System.out.println(q.poll());

			} else
				q.add(a);

		}

	}

}