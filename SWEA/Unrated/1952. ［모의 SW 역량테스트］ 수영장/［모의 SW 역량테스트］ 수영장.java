import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

	static int month[];
	static int plan[];
	static StringBuffer buffer;
	static int result = 0;
	static int dp[];

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		buffer = new StringBuffer();
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(in.readLine());
		for (int i = 1; i <= t; i++) {
			StringTokenizer s = new StringTokenizer(in.readLine(), " ");
			month = new int[13];
			plan = new int[4];
			dp = new int[13];
			result = Integer.MAX_VALUE;
			for (int j = 0; j < 4; j++) {
				plan[j] = Integer.parseInt(s.nextToken());

			}
			s = new StringTokenizer(in.readLine(), " ");
			for (int j = 1; j < 13; j++) {

				month[j] = Integer.parseInt(s.nextToken());

			}
			// System.out.println(Arrays.toString(month));
			// System.out.println(Arrays.toString(plan));
			
			dp(0);
			result = Math.min(dp[12], plan[3]);
			buffer.append("#" + i + " " + result + "\n");

		}
		System.out.println(buffer);

	}

	private static void dp(int start) {
		// TODO Auto-generated method stub

		for (int i = 1; i <= 12; i++) {

			dp[i] = Math.min(dp[i - 1] + month[i] * plan[0], dp[i - 1] + plan[1]);
			if(i>=3) 
				dp[i] = Math.min(dp[i], dp[i - 3] + plan[2]);
		}

	}

}