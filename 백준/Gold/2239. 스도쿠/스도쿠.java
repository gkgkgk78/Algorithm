import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

	static int graph[][];

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		graph = new int[9][9];

		for (int i = 0; i < 9; i++) {
			char temp[] = in.readLine().toCharArray();
			for (int j = 0; j < 9; j++) {
				graph[i][j] = temp[j] - '0';

			}

		}

		int tt = 0;
//		game(0);
		game(0);
		for (int i = 0; i < 9; i++) {
			for(int j=0;j<9;j++)
				System.out.print(graph[i][j]+"");
			System.out.println();
		}

	}

	private static int game(int i1) {
		// TODO Auto-generated method stub

		// 해당되는 3*3 구역 내에서 남은 개수를 확인을 함

		int x = i1 / 9;
		int y = i1 % 9;

		if (i1 == 81)
			return 1;

		if (graph[x][y] != 0) {
			int z = game(i1 + 1);
			if (z == 1)
				return 1;
		} else {

			// 좌우로 판단을

			for (int i = 1; i < 10; i++) {

				int zz = check(x, y, i);
				if (zz == 1) {
					graph[x][y] = i;
					int z = game(i1 + 1);
					if (z == 1)
						return 1;
					else {
						graph[x][y] = 0;
					}
				}

			}

		}
		return 0;
	}

	private static int check(int x, int y, int e) {
		// TODO Auto-generated method stub

		for (int i = 0; i < 9; i++) {
			if (graph[x][i] == e || graph[i][y] == e)
				return 0;
		}

		int row = (x / 3) * 3;
		int col = (y / 3) * 3;

		for (int i = row; i < row + 3; i++) {
			for (int j = col; j < col + 3; j++) {
				if (graph[i][j] == e)
					return 0;

			}

		}

		return 1;
	}

}