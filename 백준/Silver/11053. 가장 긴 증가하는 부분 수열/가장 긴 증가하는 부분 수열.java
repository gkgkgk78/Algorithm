import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(in.readLine());

		int arr[] = new int[n];
		int dis[] = new int[n];
		StringTokenizer s = new StringTokenizer(in.readLine(), " ");

		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(s.nextToken());
		}

		for (int i = 0; i < n; i++) {
			dis[i] = 1;
			for (int j = 0; j < i; j++) {

				if (j != i && arr[j] < arr[i]&&dis[j]>=dis[i]) {
					
					dis[i] = Math.max(dis[i], dis[j])+1;
				}
			}

		}

		int sum = Integer.MIN_VALUE;
		//System.out.println(Arrays.toString(dis));
		for (int i = 0; i < n; i++) {
			sum = Math.max(sum, dis[i]);
		}
		System.out.println(sum);
	}

}