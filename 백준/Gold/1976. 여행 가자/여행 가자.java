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

		int n = Integer.parseInt(in.readLine());
		int m = Integer.parseInt(in.readLine());
		parents = new int[n + 1];
		v=n;
		make();
		for (int i = 0; i < n; i++) {
			StringTokenizer s = new StringTokenizer(in.readLine());

			for (int j = 0; j < n; j++) {
				int temp = Integer.parseInt(s.nextToken());
				if (temp == 1) {
					union(i, j);

				}

			}

		}
		//System.out.println(Arrays.toString(parents));
		
		StringTokenizer s = new StringTokenizer(in.readLine());
		int start=Integer.parseInt(s.nextToken());
		start--;
		for(int i=1;i<m;i++ ) {
			int t=Integer.parseInt(s.nextToken());
			t-=1;
			int uu=find(t);
			//System.out.println(find(start)+" "+find(t));
			if(find(start)!=find(t))
			{
				System.out.println("NO");
				System.exit(0);
			}
			
		}
		System.out.println("YES");
	}

}