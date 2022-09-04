import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static int[] parents;
	static int v, e;

	static void make() {

		for (int i = 0; i < v; i++) {
			parents[i] = i;
		}

	}

	static int find(int a) {
		if (parents[a] == a)
			return a;
		return parents[a] = find(parents[a]);

	}

	static boolean union(int a, int b) {
		int u1=find(a);
		int u2=find(b);
		if (u1==u2)
			return false;
		
		if(u1<u2)
			parents[u2] = u1;
		else
			parents[u1] = u2;
		return true;

	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer s = new StringTokenizer(in.readLine());
		int n = Integer.parseInt(s.nextToken());
		int m = Integer.parseInt(s.nextToken());
		parents = new int[n + 1];
		v=n;
		make();
		for (int i = 0; i < m; i++) {
			s = new StringTokenizer(in.readLine());
			int a1=Integer.parseInt(s.nextToken());
			int a2=Integer.parseInt(s.nextToken());
			if(!union(a1,a2))
			{
				System.out.println(i+1); 
				System.exit(0);
			}
			
		}

		System.out.println(0);
	}

}