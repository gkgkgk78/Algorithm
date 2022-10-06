import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(in.readLine());
		StringTokenizer s = new StringTokenizer(in.readLine(), " ");
		int arr[] = new int[n];
		int dp[] = new int[n];
		for (int i = 0; i < n; i++) {

			arr[i] = Integer.parseInt(s.nextToken());

		}
		int size = 1;
		dp[0]=arr[0];

		for (int i = 1; i < n; i++) {
			int now = arr[i];
			if (now > dp[size-1]) {
		
				dp[size] = now;
				size++;
				
			} else if (now <= dp[size-1]) {
				int u = bi(now, 0, size-1, dp);
				dp[u]=now;

			}

		}
		//System.out.println(Arrays.toString(dp));
		System.out.println(size);

	}

	private static int bi(int now, int left, int right, int dp[]) {
		// TODO Auto-generated method stub

		int l = left;
		int r = right;

		while (l <= r) {

			int mid = (l + r) / 2;
			int tt = dp[mid];

			if (tt < now) {
				l = mid + 1;
			} else

			{
				r = mid - 1;
			}

		}
		return l;

	
	}

}