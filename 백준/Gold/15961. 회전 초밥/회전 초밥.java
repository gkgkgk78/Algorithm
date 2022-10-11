import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		HashMap<Integer, Integer> map = new HashMap<>();

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer s = new StringTokenizer(in.readLine(), " ");
		int n, d, k, c;

		n = Integer.parseInt(s.nextToken());
		d = Integer.parseInt(s.nextToken());
		k = Integer.parseInt(s.nextToken());
		c = Integer.parseInt(s.nextToken());

		int arr[] = new int[n];
		for (int i = 0; i < n; i++) {
			int t = Integer.parseInt(in.readLine());
			arr[i] = t;
		}

		int result = Integer.MIN_VALUE;
		int visit[] = new int[30001];
		int count = 0;
		ArrayList<Integer>a1=new ArrayList<>();
		for (int i = 0; i < k; i++) {

			if (visit[arr[i]] == 0) {
				visit[arr[i]] = 1;
				count++;
			} else {
				visit[arr[i]]++;
			}
		}

		if (visit[c] == 0) {
			result = Math.max(count + 1, result);
		} else
			result = Math.max(count, result);
	
		for (int i = 1; i < n; i++) {

			int z=i - k;
			if(visit[arr[i-1]]==1)
				count--;
			visit[arr[i-1]] -= 1;
			int z1=arr[(i+k-1)%n];
			if (visit[z1] == 0) {
				visit[z1] = 1;
				count++;
			} else {
				visit[z1]++;
			}
			if (visit[c] == 0) {
				result = Math.max(count + 1, result);
			} else
				result = Math.max(count, result);
		}
		System.out.println(result);

	}

}