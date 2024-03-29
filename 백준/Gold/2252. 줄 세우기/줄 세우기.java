import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int n, m;
	static int degree[];
	static List<List<Integer>> hi;
	static StringBuffer buffer;
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		buffer=new StringBuffer();
		StringTokenizer s = new StringTokenizer(in.readLine(), " ");
		n = Integer.parseInt(s.nextToken());
		m = Integer.parseInt(s.nextToken());
		hi = new ArrayList<>();
		for (int i = 0; i <= n; i++) {
			hi.add(new ArrayList<>());
		}
		degree = new int[n + 1];
		for (int i = 0; i < m; i++) {
			s = new StringTokenizer(in.readLine(), " ");
			int a1, a2;
			a1 = Integer.parseInt(s.nextToken());
			a2 = Integer.parseInt(s.nextToken());
			hi.get(a1).add(a2);
			degree[a2] += 1;
		}
		topology();

	}

	private static void topology() {
		// TODO Auto-generated method stub
		Queue<Integer> q = new LinkedList<>();
		Queue<Integer> result = new LinkedList<>();
		for (int i = 1; i <= n; i++) {
			if (degree[i] == 0) {
				q.add(i);
			}
		}
		while (!q.isEmpty()) {
			int temp = q.poll();
			result.add(temp);
			for (Integer integer : hi.get(temp)) {
				degree[integer]--;
				if (degree[integer] == 0)
					{
						q.add(integer);
						
					}
			}	
		}
		//System.out.println(Arrays.toString(degree));
		while(!result.isEmpty()) {
			buffer.append(result.poll()+" ");
		}
		System.out.println(buffer);

	}

}