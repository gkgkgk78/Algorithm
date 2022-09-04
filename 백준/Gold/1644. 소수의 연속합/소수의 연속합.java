import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {

		// System.setIn(new FileInputStream("src/input.txt"));

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		int a = Integer.parseInt(in.readLine());
		int total[] = new int[a + 1];
		ArrayList<Integer> now = new ArrayList<>();
		if (a == 2) {
			System.out.println(1);
			System.exit(0);
		} else if (a == 1) {
			System.out.println(0);
			System.exit(0);
		}
		for (int j = 2; j <= a; j++) {
			int k = j;

			while (k <= a) {
				total[k] += 1;
				k = k + j;

			}

		}

		for (int j = 2; j <= a; j++) {
			if (total[j] == 1)
				now.add(j);
		}
		int count = 0;
		int left = 0;
		int right = 0;

		int sum = now.get(0);
		while (true) {
			// System.out.println(left + " " + right + " " + sum + " " + a);
			if (sum <= a) {
				if (sum == a) {
					// System.out.println(left+" "+right);
					count += 1;
				}
				if (right + 1 <= now.size()) {
					// sum -= now.get(right);
					right++;
					sum += now.get(right);
				} else {
					if (left + 1 <= now.size() && left + 1 <= right) {
						sum -= now.get(left);
						left++;

					}

				}
			} else {

				if (left + 1 <= now.size() && left + 1 <= right) {
					sum -= now.get(left);
					left++;

				} else {
					if (right + 1 <= now.size() - 1) {
						right++;
						sum += now.get(right);
					}
				}

			}
			if (left == right) {
				if (sum == a)
					count++;
				if (left == now.size() - 1)
					break;
			}

		}

		System.out.println(count);
	}

}