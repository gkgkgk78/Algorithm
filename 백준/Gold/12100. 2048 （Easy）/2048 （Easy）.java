import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static StringBuffer buffer;

	static int[] target = new int[] { 0, 1, 2, 3 };
	static int[] result = new int[5];
	static int[][] visit;
	static int n;
	static int[][] graph;// 원본
	static int[][] graph1;// 복사본
	static int res;

	private static void permutation(int cnt) {
		if (cnt == 5) {
			graph1 = new int[n][n];
			// System.out.println(Arrays.toString(result));
			int fi = Integer.MIN_VALUE;
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++)
					graph1[i][j] = graph[i][j];

			}

			// 이때 시작을 해보도록 하지
			for (int i = 0; i < 5; i++) {
				game(result[i]);

			}
			// 그러고 나서 최대의 결과를 확인해 보도록 하자
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if (graph1[i][j] > fi)
						fi = graph1[i][j];
				}
			}
			if (fi > res)
				res = fi;
//			System.out.println(Arrays.toString(result));
//			for (int i = 0; i < n; i++) {
//				System.out.println(Arrays.toString(graph1[i]));
//			}
//			System.out.println();

			return;
		}

		for (int i = 0; i < 4; i++) {
			result[cnt] = target[i];
			permutation(cnt + 1);

		}

	}

	private static void game(int i) {
		// TODO Auto-generated method stub
		//
		visit = new int[n][n];
		if (i == 0)// 상 , 위에서 부터 내려오면서 찾아서 존재하면 위로 올림
		{

			int u = n - 1;

			for (int p = 0; p < n; p++) {// 열
				for (int k = 0; k < n; k++) {// 행

					if (graph1[k][p] > 0 && k > 0) {
						int k1 = k - 1;
						int chch = 0;
						while (k1 >= 0) {
							if (graph1[k1][p] > 0) {
								// 더하는 조건
								if (visit[k][p] == 0 && visit[k1][p] == 0) {
									if (graph1[k1][p] == graph1[k][p]) // 이때 더하는 거임
									{
										graph1[k1][p] += graph1[k][p];
										visit[k1][p] = 1;
										if (k != k1) {
											graph1[k][p] = 0;
											visit[k][p] = 0;
										}
										break;
									} else {// 아니면 그전에 놓아둠
										graph1[k1 + 1][p] = graph1[k][p];
										visit[k1 + 1][p] = visit[k][p];
										if (k != k1 + 1) {
											visit[k][p] = 0;
											graph1[k][p] = 0;
										}
										break;
									}

								} else {// 아니면 그전에 놓아둠
									graph1[k1 + 1][p] = graph1[k][p];
									visit[k1 + 1][p] = visit[k][p];
									if (k != k1 + 1) {
										visit[k][p] = 0;
										graph1[k][p] = 0;
									}
									break;
								}

							}
							k1--;

						}
						if (k1 == -1) {
							graph1[0][p] = graph1[k][p];
							visit[0][p] = visit[k][p];
							visit[k][p] = 0;
							graph1[k][p] = 0;

						}
					}

				}

			}

		} else if (i == 1)// 하,아래쪽부터 탐색, 밑으로 내리고자 할거임, 행이 움직여야함
		{
			for (int p = 0; p < n; p++) {// 열
				for (int k = n - 2; k >= 0; k--) {// 행
					if (graph1[k][p] > 0) {
						int k1 = k + 1;
						int chch = 0;
						while (k1 < n) {
							if (graph1[k1][p] > 0) {
								// 더하는 조건
								if (visit[k][p] == 0 && visit[k1][p] == 0) {
									if (graph1[k1][p] == graph1[k][p]) // 이때 더하는 거임
									{
										graph1[k1][p] += graph1[k][p];
										visit[k1][p] = 1;
										if (k != k1) {
											graph1[k][p] = 0;
											visit[k][p] = 0;
										}
										break;
									} else {// 아니면 그전에 놓아둠
										graph1[k1 - 1][p] = graph1[k][p];
										visit[k1 - 1][p] = visit[k][p];
										if (k != k1 - 1) {
											visit[k][p] = 0;
											graph1[k][p] = 0;
										}
										break;
									}
								} else {// 아니면 그전에 놓아둠
									graph1[k1 - 1][p] = graph1[k][p];
									visit[k1 - 1][p] = visit[k][p];
									if (k != k1 - 1) {
										visit[k][p] = 0;
										graph1[k][p] = 0;
									}
									break;
								}

							}
							k1++;

						}
						if (k1 == n) {
							graph1[n - 1][p] = graph1[k][p];
							visit[n - 1][p] = visit[k][p];
							visit[k][p] = 0;
							graph1[k][p] = 0;

						}
					}
				}
			}
		}

		else if (i == 2)// 좌,왼부터 탐색, 오른쪽으로 움직이고자 할거임, 열이 움직여야함
		{
			for (int p = 0; p < n; p++) {// 행
				for (int k = 1; k < n; k++)// 열
				// 열이 움직이는 거로 탐색을 해야함
				{
//					for (int i1 = 0; i1 < n; i1++) {
//						System.out.println(Arrays.toString(graph1[i1]));
//						if (k == 1)
//							i1 = i1;
//					}
//					System.out.println();
					if (graph1[p][k] > 0) {
						int k1 = k - 1;
						int chch = 0;
						while (k1 >= 0) {
							if (graph1[p][k1] > 0) {
								// 더하는 조건
								if (visit[p][k1] == 0 && visit[p][k] == 0) {
									if (graph1[p][k1] == graph1[p][k]) // 이때 더하는 거임
									{
										graph1[p][k1] += graph1[p][k];
										visit[p][k1] = 1;
										if (k != k1) {
											graph1[p][k] = 0;
											visit[p][k] = 0;
										}
										break;
									} else {// 아니면 그전에 놓아둠
										graph1[p][k1 + 1] = graph1[p][k];
										visit[p][k1 + 1] = visit[p][k];
										if (k != k1 + 1) {
											visit[p][k] = 0;
											graph1[p][k] = 0;
										}
										break;
									}
								} else {// 아니면 그전에 놓아둠
									graph1[p][k1 + 1] = graph1[p][k];
									visit[p][k1 + 1] = visit[p][k];
									if (k != k1 + 1) {
										visit[p][k] = 0;
										graph1[p][k] = 0;
									}
									break;
								}

							}
							k1--;

						}
						if (k1 == -1) {
							graph1[p][0] = graph1[p][k];
							visit[p][0] = visit[p][k];
							visit[p][k] = 0;
							graph1[p][k] = 0;

						}
					}
				}
			}
		}

		else if (i == 3)// 우,오른쪽 부터 탐색을 해야함, 열이 탐색을 해야함
		{
			for (int p = 0; p < n; p++) {// 행
				for (int k = n - 2; k >= 0; k--)// 열
				// 열이 움직이는 거로 탐색을 해야함
				{
					if (graph1[p][k] > 0) {
						int k1 = k + 1;
						int chch = 0;
						while (k1 < n) {
							if (graph1[p][k1] > 0) {
								// 더하는 조건
								if (visit[p][k1] == 0 && visit[p][k] == 0) {
									if (graph1[p][k1] == graph1[p][k]) // 이때 더하는 거임
									{
										graph1[p][k1] += graph1[p][k];
										visit[p][k1] = 1;
										if (k != k1) {
											graph1[p][k] = 0;
											visit[p][k] = 0;
										}
										break;
									} else {// 아니면 그전에 놓아둠
										graph1[p][k1 - 1] = graph1[p][k];
										visit[p][k1 - 1] = visit[p][k];
										if (k != k1 - 1) {
											visit[p][k] = 0;
											graph1[p][k] = 0;
										}
										break;
									}
								} else {// 아니면 그전에 놓아둠
									graph1[p][k1 - 1] = graph1[p][k];
									visit[p][k1 - 1] = visit[p][k];
									if (k != k1 - 1) {
										visit[p][k] = 0;
										graph1[p][k] = 0;
									}
									break;
								}

							}
							k1++;

						}
						if (k1 == n) {
							graph1[p][n - 1] = graph1[p][k];
							visit[p][n - 1] = visit[p][k];
							visit[p][k] = 0;
							graph1[p][k] = 0;

						}
					}
				}
			}

		}

	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		buffer = new StringBuffer();

		n = Integer.parseInt(in.readLine());

		graph = new int[n][n];
		res = Integer.MIN_VALUE;
		for (int i = 0; i < n; i++) {
			StringTokenizer s = new StringTokenizer(in.readLine());
			for (int j = 0; j < n; j++)
				graph[i][j] = Integer.parseInt(s.nextToken());

		}
		// 벽을 만나면 거기에 멈추고
		// 움직이고자 하는 방향에 존재시 합침
		permutation(0);

		// 테스트코드 시작
//		graph1 = new int[n][n];
//		for (int i = 0; i < n; i++) {
//			for (int j = 0; j < n; j++)
//				graph1[i][j] = graph[i][j];
//
//		}
//
//		game(2);
//
//		for (int i = 0; i < n; i++) {
//			System.out.println(Arrays.toString(graph1[i]));
//		}
		// 테스트 코드 끝

		System.out.println(res);
	}

}