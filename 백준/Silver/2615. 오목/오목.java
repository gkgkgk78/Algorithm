import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.*;

public class Main {

	public static int x;
	public static int y;
	public static int check(int graph[][], int r, int c) {

		// 우선 세로부터 체크를 하자
		int temp = 1;

		int start = graph[r][c];
		for (int i = 1; i <= 5; i++) {
			if (r + i < 19) {
				if (graph[r + i][c] == start) {
					temp += 1;
				} else {
					break;
				}
			} else
				break;
		}
		int tx=r;
		int ty=c;
		x=r;
		y=c;
		for (int i = 1; i <= 5; i++) {
			if (r -i>=0) {
				if (graph[r - i][c] == start) {
					x=r-i;
					temp += 1;
				} else {
					break;
				}
			} else
				break;
		}
		
		if (temp == 5) {
			return 1;
		}

		// 그다음에 가로
		temp = 1;
		x=r;
		y=c;
		for (int i = 1; i <= 5; i++) {
			if (c + i < 19) {
				if (graph[r][c + i] == start) {
					temp += 1;
				} else {
					break;
				}
			} else
				break;
		}
		tx=r;
		ty=c;
		for (int i = 1; i <= 5; i++) {
			if (c - i >=0) {
				if (graph[r][c - i] == start) {
					temp += 1;
					ty=c-i;
				} else {
					break;
				}
			} else
				break;
		}
		
		
		if (temp == 5) {
			return 2;
		}

		// 그다음에 대각선 아래쪽 방향으로 체크
		temp = 1;
		x=r;
		y=c;
		tx = r + 1;
		ty = c + 1;
		for (int i = 1; i <= 5; i++) {
			if (tx < 19 && ty < 19) {
				if (graph[tx][ty] == start) {
					temp += 1;
					tx += 1;
					ty += 1;
				} else {
					break;
				}
			} else
				break;
		}
		tx = r - 1;
		ty = c - 1;
		x=r;
		y=c;
		for (int i = 1; i <= 5; i++) {
			if (tx>=0 && ty-1>=0) {
				if (graph[tx][ty] == start) {
					temp += 1;
					x=tx;
					y=ty;
					tx -= 1;
					ty -= 1;
					
				} else {
					break;
				}
			} else
				break;
		}
		if (temp == 5) {
			return 3;
		}

		int ui=0;
		if(r==5&& c==0)
			ui=7;
		// 그 다음에 대각선 위
		temp = 1;
		tx = r - 1;
		ty = c + 1;
		for (int i = 1; i <= 5; i++) {
			if (tx >=0 && ty < 19) {
				if (graph[tx][ty] == start) {
					temp += 1;
					tx -= 1;
					ty += 1;
				} else {
					break;
				}
			} else
				break;
		}
		tx = r + 1;
		ty = c - 1;
		for (int i = 1; i <= 5; i++) {
			if (tx <19 && ty >=0) {
				if (graph[tx][ty] == start) {
					temp += 1;
					x=tx;
					y=ty;
					tx += 1;
					ty -= 1;
				} else {
					break;
				}
			} else
				break;
		}
		if (temp == 5) {
			return 4;
		}

		return 0;
	}

	public static void main(String[] args) throws FileNotFoundException {
		Scanner sc = new Scanner(System.in);
		// 5개의 알이 일직선 , 직선 대각선 포함을 이루면 이기는 게임이다
		// 흰색과 검정색 바둑알중 어떤 색의 바둑알이 이겼는지 또는 승부가 결정되지 않았는지 를 판단
		// 동시에 이기거나 검은색 또는 흰색이 두군데 이상에서 동시에 이기는 경우는 없음
		// 검은 바둑알은1, 흰 바둑알은 2, 알이 놓이지 않는 자리는 0으로 표시됨
		// 무승부 0, 검은색 승 1, 흰색 승 2
		// 둘째줄 출력에는 이기게 된 바둑알 구함, 세로로 되었을시에는 가장 위쪽의 바둑알 구함
		int graph[][] = new int[19][19];

		for (int i = 0; i < 19; i++) {
			String[] a1 = sc.nextLine().split(" ");
			for (int j = 0; j < 19; j++) {
				graph[i][j] = Integer.parseInt(a1[j]);
			}
		}
		for (int i = 0; i < 19; i++) {
			for (int j = 0; j < 19; j++) {

				if (graph[i][j] != 0) {
					int hi = check(graph, i, j);
					
					if (hi != 0) {
						System.out.println(graph[i][j]);
						if (hi == 1 ||hi==2||hi==3 || hi==4) {
							System.out.println((x+1)+" "+(y+1));
							return ;
							
						} 
						
					}
				}

			}
		}
		System.out.println(0);
		
		
		

	}

}
