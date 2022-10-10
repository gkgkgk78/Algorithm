import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static int graph[][];
	static int sel[];
	static int n;
	static int numbers[];
	static int count=0;
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(in.readLine());

		graph = new int[n][5];

		for (int i = 0; i < n; i++) {
			int a2, a3;
			StringTokenizer s = new StringTokenizer(in.readLine(), " ");
			char a1[] = (s.nextToken().toCharArray());
			a2 = Integer.parseInt(s.nextToken());
			a3 = Integer.parseInt(s.nextToken());
			graph[i][0] = a1[0] - '0';
			graph[i][1] = a1[1] - '0';
			graph[i][2] = a1[2] - '0';
			graph[i][3] = a2;
			graph[i][4] = a3;
		}
		sel = new int[10];
		numbers = new int[3];
		perm(0);
		System.out.println(count);
	}

	private static void perm(int cnt) {
		// TODO Auto-generated method stub
		if (cnt == 3) {
			//if(numbers[0]==3&&numbers[1]==2&&numbers[2]==4)
			game();
			return;
		}
		for (int i = 1; i <= 9; i++) {
			if (sel[i] == 1)
				continue;
			sel[i] = 1;
			numbers[cnt] = i;
			perm(cnt + 1);
			sel[i] = 0;

		}

	}
	
	private static void game() {
		// TODO Auto-generated method stub
		for (int i = 0; i < n; i++) {

			int ch_st = graph[i][3];
			int ch_bl = graph[i][4];

			int st = 0;
			int bl = 0;
			for (int j = 0; j < 3; j++) {
				if (graph[i][j]== numbers[j]) {
					st++;
				} else {
					for (int k = 0; k < 3; k++) {
						if (graph[i][k]== numbers[j]) {
							bl++;
							break;
						}

					}
				}
			}
			if(ch_st!=st||ch_bl!=bl)
				return;
		}
		count++;

	}

}