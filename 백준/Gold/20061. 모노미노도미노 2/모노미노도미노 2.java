import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static int red[][];
	static int blue[][];
	static int green[][];
	static int score = 0;

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		red = new int[4][4];
		green = new int[6][4];
		blue = new int[4][6];
		int n = Integer.parseInt(in.readLine());
		for (int i = 0; i < n; i++) {
			StringTokenizer s = new StringTokenizer(in.readLine(), " ");
			int t, x, y;
			t = Integer.parseInt(s.nextToken());
			x = Integer.parseInt(s.nextToken());
			y = Integer.parseInt(s.nextToken());
			game(t, x, y);

		}
		int su = 0;
		for (int j = 0; j < 6; j++) {
			//System.out.println(Arrays.toString(green[j]));
			for (int k = 0; k < 4; k++)
			{
				if (green[j][k] == 1)
					su++;
			}
		}
		//System.out.println();
		for (int j = 0; j < 4; j++) {
			//System.out.println(Arrays.toString(blue[j]));
			for (int k = 0; k < 6; k++)

			{
				if (blue[j][k] == 1)
					su++;
			}
		}

		//System.out.println();
		System.out.println(score);
		System.out.println(su);
	}

	private static void game(int t, int x, int y) {

		if (t == 1)// 1*1
		{
			move_green(x, y, 1);
			move_blue(x, y, 1);

		} else if (t == 2)// 1*2
		{
			move_green(x, y, 2);
			move_blue(x, y + 1, 2);

		} else if (t == 3) {// 2*1

			move_green(x + 1, y, 3);
			move_blue(x, y, 3);
		}
		// 행이나 열이 타일로 가득찬 경우가 없을때까지 점수 획득 하도록 하자

		// 초록색 체크 진행
		for (int i = 5; i >= 0; i--) {
			int ta = 0;
			for (int j = 0; j < 4; j++) {
				if (green[i][j] == 0) {
					ta = 1;
					break;
				}
			}
			if (ta == 0) {
				while (true) {
					for (int j = 0; j < 4; j++) {
						green[i][j] = 0;

					}
					score++;

					move_green_1(i);

					ta = 0;
					for (int j = 0; j < 4; j++) {
						if (green[i][j] == 0) {
							ta = 1;
							break;
						}
					}
					if (ta == 1)
						break;
				}
			}
		}
		// 파란색 처리
		for (int i = 5; i >= 0; i--)// 열
		{
			int ta = 0;
			for (int j = 0; j < 4; j++) {// 행
				if (blue[j][i] == 0) {
					ta = 1;
					break;
				}
			}
			if (ta == 0) {
				while (true) {
					for (int j = 0; j < 4; j++) {
						blue[j][i] = 0;

					}
					score++;
					move_blue_1(i);
					ta = 0;
					for (int j = 0; j < 4; j++) {
						if (blue[j][i] == 0) {
							ta = 1;
							break;
						}
					}
					if (ta == 1)
						break;
				}
			}
		}

		// 연한칸에 블록이 있는 경우를 처리 하도록 하자
		// 초록 연한칸 처리
		int chch = 0;
		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < 4; j++) {
				if (green[i][j] == 1) {
					chch++;
					break;
				}
			}
		}
		if (chch == 2) {
			for (int j = 0; j < 4; j++) {
				green[5][j] = 0;
			}
			for (int j = 0; j < 4; j++) {
				green[4][j] = 0;
			}
			for (int j = 0; j < 4; j++) {
				for (int k = 3; k >= 0; k--) {
					green[k + 2][j] = green[k][j];
					green[k][j] = 0;
				}
			}

		}

		else if (chch == 1) {
			for (int j = 0; j < 4; j++) {
				green[5][j] = 0;
			}
			for (int j = 0; j < 4; j++) {
				for (int k = 4; k >= 0; k--) {
					green[k + 1][j] = green[k][j];
					green[k][j] = 0;
				}
			}

		}
		chch = 0;
		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < 4; j++) {
				if (blue[j][i] == 1) {
					chch++;
					break;
				}
			}
		}
		if (chch == 2) {
			for (int j = 0; j < 4; j++) {
				blue[j][5] = 0;
			}
			for (int j = 0; j < 4; j++) {
				blue[j][4] = 0;
			}
			for (int j = 0; j < 4; j++) {
				for (int k = 3; k >= 0; k--) {
					blue[j][k + 2] = blue[j][k];
					blue[j][k] = 0;
				}
			}

		}

		else if (chch == 1) {
			for (int j = 0; j < 4; j++) {
				blue[j][5] = 0;
			}

			for (int j = 0; j < 4; j++) {
				for (int k = 4; k >= 0; k--) {
					blue[j][k + 1] = blue[j][k];
					blue[j][k] = 0;
				}
			}

		}

	}

	private static void move_blue_1(int k) {
		// TODO Auto-generated method stub
		for (int i = k - 1; i >= 0; i--) {
			for (int j = 0; j < 4; j++) {
				if (blue[j][i] == 1) {
					blue[j][i + 1] = blue[j][i];
					blue[j][i] = 0;
				}

			}

		}
	}

	private static void move_green_1(int k) {
		// TODO Auto-generated method stub
		for (int i = 0; i < 4; i++) {
			for (int j = k - 1; j >= 0; j--) {
				if (green[j][i] == 1) {
					green[j + 1][i] = green[j][i];
					green[j][i] = 0;
				}

			}

		}
	}

	private static void move_blue(int x, int y, int z) {
		// TODO Auto-generated method stub
		if (z == 3) {
			int ty = 0;
			while (ty <= 4) {
				if (blue[x][ty + 1] == 0 && blue[x + 1][ty + 1] == 0) {
					ty++;
					if (ty == 5) {
						blue[x][ty] = 1;
						blue[x + 1][ty] = 1;
						return;
					}

				} else {
					blue[x][ty] = 1;
					blue[x + 1][ty] = 1;
					return;
				}

			}
		} else {
			int ty = 0;
			while (ty <= 4) {
				if (blue[x][ty + 1] == 0) {
					ty++;

					if (ty == 5) {
						blue[x][ty] = 1;
						if (z == 2) {
							blue[x][ty - 1] = 1;
						}
						return;
					}

				} else {
					blue[x][ty] = 1;
					if (z == 2) {
						blue[x][ty - 1] = 1;
					}
					return;
				}

			}

		}

	}

	private static void move_green(int x, int y, int z) {
		// 단순히 보드의 경계나 다른 블록을 만나기 전까지 계속해서 이동을 함

		if (z == 2) {
			int tx = 0;
			while (tx <= 4) {
				if (green[tx + 1][y] == 0 && green[tx + 1][y + 1] == 0) {
					tx += 1;
					if (tx == 5) {
						green[tx][y] = 1;
						green[tx][y + 1] = 1;
						return;
					}
				} else {
					green[tx][y] = 1;
					green[tx][y + 1] = 1;
					return;
				}
			}

		} else {
			int tx = 0;
			while (tx <= 4) {

				if (green[tx + 1][y] == 0) {
					tx += 1;
					if (tx == 5) {
						green[tx][y] = 1;
						if (z == 3) {
							green[tx - 1][y] = 1;
						}
						return;
					}
				} else {
					green[tx][y] = 1;
					if (z == 3) {

						green[tx - 1][y] = 1;
					}
					return;
				}
			}

		}

	}

}