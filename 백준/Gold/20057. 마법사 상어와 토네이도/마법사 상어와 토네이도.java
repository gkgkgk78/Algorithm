import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {

	static int movex[][] = { { -1, 1, -2, 2, 0, -1, 1, -1, 1 }, { -1, -1, 0, 0, 2, 0, 0, 1, 1 },
			{ -1, 1, -2, 2, 0, -1, 1, -1, 1 }, { 1, 1, 0, 0, -2, 0, 0, -1, -1 } };// 좌 하 우 상
	static int movey[][] = { { 1, 1, 0, 0, -2, 0, 0, -1, -1 }, { -1, 1, -2, 2, 0, -1, 1, -1, 1 },
			{ -1, -1, 0, 0, 2, 0, 0, 1, 1 }, { -1, 1, -2, 2, 0, -1, 1, -1, 1 } };// 좌 하 우 상
	static int add[] = { 1, 1, 2, 2, 5, 7, 7, 10, 10 };
	static int putx[] = { 0, 1, 0, -1 };
	static int puty[] = { -1, 0, 1, 0 };

	public static void main(String[] args) throws NumberFormatException, IOException {

	

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		// 좌 후 우 상 이 반복이 되며
		// 1 1 2 2 3 3 ...의 순서로 진행이 된다.
		int n = Integer.parseInt(in.readLine());

		int graph[][] = new int[n][n];
		int x, y;

		for (int i = 0; i < n; i++) {
			StringTokenizer a1 = new StringTokenizer(in.readLine());
			for (int j = 0; j < n; j++) {
				graph[i][j] = Integer.parseInt(a1.nextToken());

			}

		}

		x = n / 2;
		y = n / 2;

		int dx[] = { 0, 1, 0, -1 };
		int dy[] = { -1, 0, 1, 0 };
		int now = 1;// 얼마 만큼 더해 줄지
		int check = 0;// 2번 되었을시에는 이제 다시 0으로 해서
		int dir = 0;// 현재 진행 중인 방향
		int count = 0;// 밖으로 나간 모래의 양

		while (true) {

			if (x == 0 && y == 0) {
				// System.out.println(count);
				break;
			} else {

				if (dir == 4)
					dir = 0;
				int zx = x;
				int zy = y;
				for (int i = 0; i < now; i++) {
					zx = dx[dir] + zx;
					zy = dy[dir] + zy;


					// graph[x][y]+=first_size;
					// 이제 이동한 방향에 대해서 진행 하고 남은 양은 더해 줘야함
					int tempx;
					int tempy;

					int now_size = graph[zx][zy];
					int row = 0;
					int left = 0;
					for (int i1 = 0; i1 < 9; i1++) {

						tempx = zx + movex[dir][i1];
						tempy = zy + movey[dir][i1];

						if (0 <= tempx && tempx < n && 0 <= tempy && tempy < n) {
							graph[tempx][tempy] += (int) ((now_size * add[i1]) / 100);

						} else// 격자 밖으로 나간양을 의미한다
						{
							// System.out.println(tempx+" "+tempy);
							count += (int) ((now_size * add[i1]) / 100);

							// row += (int) (now_size * (add[i] * 0.01));
						}
						left += (int) ((now_size * add[i1]) / 100);

					}

					graph[zx][zy] -= left;

					if (graph[zx][zy] > 0) {
						if (0 <= zx + putx[dir] && zx + putx[dir] < n && 0 <= zy + puty[dir] && zy + puty[dir] < n) {
							graph[zx + putx[dir]][zy + puty[dir]] += graph[zx][zy];

						} else// 격자 밖으로 나간양을 의미한다
						{

							count += graph[zx][zy];
							// System.out.println(count+" "+x+" "+y);

						}
					}

					graph[zx][zy] = 0;
					if (zx ==0 && zy==0) {
						System.out.println(count);
						break;
					}
				}
				x=zx;
				y=zy;

				dir++;
				check++;
				if (check == 2) {
					now += 1;
					check = 0;
				}

			}

		}

	}

}