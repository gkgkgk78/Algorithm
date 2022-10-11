import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static StringBuffer buffer;
	static int n, x;
	static int graph[][];
	static int result;

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub

		// 활주로를 건설 하고자 한다ㅏ.
		// 각 셀의 숫자는 지형의 높이를 의미한다.
		buffer = new StringBuffer();
		// 높이가 다를 시 무조건 활주로를 건설해야 함
		// 그것이 되지 않으면 답의 경우의 수에 포함이 되지 않음
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		int t = Integer.parseInt(in.readLine());
		for (int i = 1; i <= t; i++) {

			StringTokenizer s = new StringTokenizer(in.readLine(), " ");

			n = Integer.parseInt(s.nextToken());
			x = Integer.parseInt(s.nextToken());
			graph = new int[n][n];
			result = 0;
			for (int j = 0; j < n; j++) {
				s = new StringTokenizer(in.readLine(), " ");
				for (int k = 0; k < n; k++) {
					graph[j][k] = Integer.parseInt(s.nextToken());

				}

			}

			// 가로로 해보고
			game_row();

			// 세로로 해보자
			game_col();
			buffer.append("#"+(i)+" "+result+"\n");
		}
		System.out.println(buffer);
	}

	private static void game_row() {
		// TODO Auto-generated method stub
		int check = 0;
		int count = 0;
		int same = 0;
		
		int visit[][]=new int[n][n];
		for (int i = 0; i < n; i++) {
			
			// 오른쪽으로 진행을 하며 높이가 다르면 그전 까지 탐색을 해서 파악을 해보자
			check = 0;
			count = 0;
			same = 0;
			int first = graph[i][0];
			if (i == 3)
				check = 0;
			int j = 0;
			while (j < n) {
				// System.out.println(j);
				// 내가 왼쪽 오른쪽 거중에서 다른거 파악을 하고 놓도록 하자
				if (first == graph[i][j])
					same++;
				// 오른쪽
				if (j != n - 1 && graph[i][j + 1] != graph[i][j]) {
					// 놓을수 있는지 판단을 하자.
					if (graph[i][j + 1] == graph[i][j] + 1) {// 오른쪽이 한칸 큼

						int temp = (j + 1) - x;

						if (temp < 0) {
							check = 1;
							break;
						}
						int val = graph[i][j];
						for (int k = temp; k < j + 1; k++) {

							if (val != graph[i][k]||visit[i][k]!=0) {
								check = 1;
								break;
							}

						}
						if (check == 1)
							break;
						count++;
						for (int k = temp; k < j + 1; k++) {
							visit[i][k]=1;
							

						}
						

					} else if (graph[i][j + 1] == graph[i][j] - 1) {

						int temp = j + x;

						if (temp >= n) {
							check = 1;
							break;
						}
						int val = graph[i][j] - 1;
						for (int k = temp; k >= j + 1; k--) {

							if (val != graph[i][k]||visit[i][k]!=0) {
								check = 1;
								break;
							}

						}
						if (check == 1)
							break;
						count++;
						for (int k = temp; k >= j + 1; k--) {

							visit[i][k]=1;

						}
						j = temp-1;
						

					} else {
						check = 1;
						break;
					}

				}
				j++;

			}
			if (check == 0) {
				if (count > 0) {
					result++;
					//System.out.println(i + " " + result);
				} else if (same == n) {

					result++;
					//System.out.println(i + " " + result);

				}
			}

		}

	}

	private static void game_col() {
		// TODO Auto-generated method stub
		int check = 0;
		int count = 0;
		int same = 0;
		int visit[][]=new int[n][n];
		for (int i = 0; i < n; i++) {
			// System.out.println(i);
			// 오른쪽으로 진행을 하며 높이가 다르면 그전 까지 탐색을 해서 파악을 해보자
			check = 0;
			count = 0;
			same = 0;
			int first = graph[0][i];
			if (i == 6)
				check = 0;
			int j = 0;
			while (j < n) {
				// System.out.println(j);
				// 내가 왼쪽 오른쪽 거중에서 다른거 파악을 하고 놓도록 하자
				if (first == graph[j][i])
					same++;
				// 아래가 큼
				if (j != n - 1 && graph[j+1][i] != graph[j][i]) {
					// 놓을수 있는지 판단을 하자.
					//아래가 큼
					if (graph[j+1][i] == graph[j][i]+1) {// 오른쪽이 한칸 큼

						int temp = (j + 1) - x;

						if (temp < 0) {
							check = 1;
							break;
						}
						int val = graph[j][i];
						for (int k = temp; k < j+1; k++) {

							if (val != graph[k][i]||visit[k][i]!=0) {
								check = 1;
								break;
							}

						}
						if (check == 1)
							break;
						for (int k = temp; k < j+1; k++) {
							visit[k][i]=1;

						}
						count++;
						

					} 
					//아래가 작음
					else if (graph[j+1][i] == graph[j][i]-1) {

						int temp = j + x;

						if (temp >= n) {
							check = 1;
							break;
						}
						int val = graph[j][i] - 1;
						for (int k = temp; k >= j + 1; k--) {

							if (val != graph[k][i]||visit[k][i]!=0) {
								check = 1;
								break;
							}

						}
						if (check == 1)
							break;
						for (int k = temp; k >= j + 1; k--) {

							visit[k][i]=1;
							
						}
						count++;
						j = temp-1;

					} else {
						check = 1;
						break;
					}

				}
				j++;

			}
			if (check == 0) {
				if (count > 0) {
					result++;
					 //System.out.println(i + " " + result);
				} else if (same == n) {

					result++;
					 //System.out.println(i + " " + result);

				}
			}

		}

	}

}