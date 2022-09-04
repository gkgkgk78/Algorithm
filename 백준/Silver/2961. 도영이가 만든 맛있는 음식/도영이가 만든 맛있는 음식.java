import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static StringBuffer buffer;
	static int[] check;
	static int[] sin;
	static int[] se;
	static int ans;

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		buffer = new StringBuffer();

		int n = Integer.parseInt(in.readLine());
		sin = new int[n];
		se = new int[n];
		check = new int[n];
		ans = 999999999;
		for (int i = 0; i < n; i++) {
			StringTokenizer s = new StringTokenizer(in.readLine());
			int a1 = Integer.parseInt(s.nextToken());
			int a2 = Integer.parseInt(s.nextToken());
			sin[i] = a1;
			se[i] = a2;
		}

		go(0, 1, 0, n);
		System.out.println(ans);
	}

	private static void go(int start, int ssin, int sese, int n) {

		if (start == n) {
			int sumz = 0;
			for (int i = 0; i < n; i++) {
				sumz += check[i];
			}
			if (sumz == 0)
				return;
			else {
				int last=(ssin-sese);
				if(last<0)
					last=-1*last;
				if(last<ans)
					ans=last;
				return;
			}

		}

		check[start] = 1;
		go(start + 1, ssin * sin[start], sese + se[start], n);
		check[start] = 0;
		go(start + 1, ssin, sese, n);

	}

}