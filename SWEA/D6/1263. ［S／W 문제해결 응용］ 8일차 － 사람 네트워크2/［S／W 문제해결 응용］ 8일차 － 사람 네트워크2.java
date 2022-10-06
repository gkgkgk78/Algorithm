import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static StringBuffer buffer;

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		buffer = new StringBuffer();
		int t = Integer.parseInt(in.readLine());

		for (int i = 1; i <= t; i++) {

			StringTokenizer s = new StringTokenizer(in.readLine(), " ");
			int n = Integer.parseInt(s.nextToken());
			int graph[][] = new int[n][n];

			for (int j = 0; j < n; j++) {
				for (int k = 0; k < n; k++) {

					graph[j][k] = Integer.parseInt(s.nextToken());
					if (j != k && graph[j][k] == 0) {
						graph[j][k] = 99999999;
					}
				}

			}
		
			for (int k = 0; k < n; k++)
				for (int i1 = 0; i1 < n; i1++)
					for (int j = 0; j < n; j++)
						graph[i1][j] = Math.min(graph[i1][j], graph[i1][k] + graph[k][j]);

			int result = Integer.MAX_VALUE;
			for (int k = 0; k < n; k++) {
				int sum=0;
				for (int i1 = 0; i1 < n; i1++) {
					sum+=graph[k][i1];
					
				}
				result=Math.min(result, sum);
			}
			buffer.append("#"+(i)+" "+result+"\n");

		}
		System.out.println(buffer);

	}

}