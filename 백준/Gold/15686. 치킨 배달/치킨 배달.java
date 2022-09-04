import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static int numbers[];
	static int input[];
	static int visited[];
	static int min;
	static int graph[][];

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		int n, m;
		StringTokenizer s = new StringTokenizer(in.readLine());
		n = Integer.parseInt(s.nextToken());
		m = Integer.parseInt(s.nextToken());

		graph = new int[n][n];
		ArrayList<Integer> chicken_x = new ArrayList<>();
		ArrayList<Integer> chicken_y = new ArrayList<>();

		ArrayList<Integer> home_x = new ArrayList<>();
		ArrayList<Integer> home_y = new ArrayList<>();
		min = Integer.MAX_VALUE;
		for (int i = 0; i < n; i++) {
			s = new StringTokenizer(in.readLine());
			for (int j = 0; j < n; j++) {
				graph[i][j] = Integer.parseInt(s.nextToken());
				if (graph[i][j] == 1)// 음 집
				{
					home_x.add(i);
					home_y.add(j);

				} else if (graph[i][j] == 2)// 치킨집
				{
					chicken_x.add(i);
					chicken_y.add(j);
				}

			}

		}
		// 이제 조합을 통하여서 순서를 고르도록 하자,
		numbers = new int[m];// 여기에 조합의 순서를 저장하도록 하자
		input = new int[chicken_x.size()];
		visited = new int[chicken_x.size()];
		for (int i = 0; i < chicken_x.size(); i++) {
			input[i] = i;
		}
		comb(n, m, 0, 0, chicken_x, chicken_y, home_x, home_y);// 전체 횟수임,채워진 개수를 의미함

		System.out.println(min);
	}

	private static void comb(int n, int m, int cnt, int start, ArrayList<Integer> chicken_x,
			ArrayList<Integer> chicken_y, ArrayList<Integer> home_x, ArrayList<Integer> home_y) {
		if (cnt == m) {
			// 이제 횟수를 파악해서 답 도출 하면됨

			//System.out.println(Arrays.toString(numbers));
			calculate(chicken_x, chicken_y, home_x, home_y);
			return;
		}


		for (int i = start; i < chicken_x.size() ; i++) {
			if (visited[i] == 1)
				continue;
			visited[i] = 1;
			numbers[cnt] = input[i];
			comb(n, m, cnt + 1, i+1, chicken_x, chicken_y, home_x, home_y);
			visited[i] = 0;
		}

	}

	private static void calculate(ArrayList<Integer> chicken_x, ArrayList<Integer> chicken_y, ArrayList<Integer> home_x,
			ArrayList<Integer> home_y) {
		// TODO Auto-generated method stub
		// 각자의 집에서 모든 치킨집에 해당 되는 것을 찾아서 계산을 하도록 하자

		int sum = 0;
		for (int i = 0; i < home_x.size(); i++) {
			int hx = home_x.get(i);
			int hy = home_y.get(i);
			int temp = Integer.MAX_VALUE;
			for (int j = 0; j < numbers.length; j++) {
				// System.out.println(Arrays.toString(numbers));
				int cx = chicken_x.get(numbers[j]);
				int cy = chicken_y.get(numbers[j]);
				int midx = hx - cx;
				int midy = hy - cy;
				midx = Math.abs(midx);
				midy = Math.abs(midy);

				if (midx + midy < temp)
					temp = midx + midy;
			}
			sum += temp;

		}
		if (sum < min) {
			min = sum;
		}

	}

}