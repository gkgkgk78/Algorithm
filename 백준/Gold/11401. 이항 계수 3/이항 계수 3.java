import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static StringBuffer buffer;
	static long p = 1000000007;

	static long fact[] = new long[4000001];

	static long pow(long a, long b) {

		if (b == 1)
			return a;
		long res = pow(a, b / 2) % p;
		if (b % 2 == 0)
			return res * res % p;
		else
			return (((res * res) % p) * a) % p;

	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		buffer = new StringBuffer();
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		
		int n, r;
		StringTokenizer s = new StringTokenizer(in.readLine(), " ");
		n = Integer.parseInt(s.nextToken());
		r = Integer.parseInt(s.nextToken());
		make(n);
		long nfact = fact[n];
		long nfactr = fact[n - r];
		long rfact = fact[r];

		long mid = (nfactr * rfact) % p;
		long temp = mid;

		mid = pow(mid, p - 2);

		// answer=((nfact%p)/(long)mid%p/(long)mid1%p)%p;
		// answer=(nfact/nfactr/rfact)%p;
		long answer = nfact * mid % p;
		System.out.println(answer);
		

	}

	private static void make(int n) {
		// TODO Auto-generated method stub
		fact[0] = 1;
		for (int i = 1; i <= n; i++) {
			fact[i] = fact[i - 1] * i % p;
		}

	}

}