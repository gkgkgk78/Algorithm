import java.awt.geom.Area;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static StringBuffer buffer;

	static String first;
	static String second;
	static String third;
	static String forth;
	static String five;
	static int[] hx;
	static int[] hy;
	static int[][] graph;
	static int[][] graph1;
	static int[] numbers;
	static int[] isselected;
	static int n, m;
	static int result;
	public static class go {
		int x;
		int y;
		int z;

		public go(int x, int y, int z) {

			this.x = x;
			this.y = y;
			this.z = z;
		}
	}

	public static int[][] move(int x, int y, char s, int[][] graph) {

		if (s == '상') {

			for (int j = x - 1; j >= 0; j--) {
				if (graph[j][y] == 0 || (graph[j][y] >= 1 && graph[j][y] <= 5)) {
					if (graph[j][y] == 0) {
						graph[j][y] = graph[x][y];
					}

				} else if (graph[j][y] == 6)
					break;

			}

		} else if (s == '우') {
			for (int j = y + 1; j < m; j++) {
				if (graph[x][j] == 0 || (graph[x][j] >= 1 && graph[x][j] <= 5)) {
					if (graph[x][j] == 0) {
						graph[x][j] = graph[x][y];
					}

				} else if (graph[x][j] == 6)
					break;

			}
		}

		else if (s == '하') {
			for (int j = x + 1; j < n; j++) {
				if (graph[j][y] == 0 || (graph[j][y] >= 1 && graph[j][y] <= 5)) {
					if (graph[j][y] == 0) {
						graph[j][y] = graph[x][y];
					}

				} else if (graph[j][y] == 6)
					break;

			}
		} else if (s == '좌') {
			for (int j = y - 1; j >= 0; j--) {
				if (graph[x][j] == 0 || (graph[x][j] >= 1 && graph[x][j] <= 5)) {
					if (graph[x][j] == 0) {
						graph[x][j] = graph[x][y];
					}

				} else if (graph[x][j] == 6)
					break;

			}
		}
		return graph;

	}

	public static void to(int start, int end, ArrayList<go> hi, int[][] graph, int n, int m) {
		String[] first = { "우", "하", "좌", "상" };
		String[] third = { "상우", "우하", "하좌", "좌상" };
		String[] fourth = { "좌상우", "상우하", "우하좌", "하좌상" };
		String[] second = { "좌우", "상하" };
		String[] five = { "상하좌우" };

		int[][] temp = new int[n][m];
		int count=0;

		if (start == end ) {
			
			for (int i = 0; i < n; i++) {
				
				for (int j = 0; j < m; j++) {
					if(graph[i][j]==0)
						count++;
				}
			}
			if(count<result)
				result=count;
			return;
		}
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				temp[i][j] = graph[i][j];
			}

		}
		go hi1 = hi.get(start);
		

		if (hi1.z == 1) {
			for (int i = 0; i < 4; i++) {
				char[] e = first[i].toCharArray();
				for (int l = 0; l < e.length; l++) {
					temp = move(hi1.x, hi1.y, e[l], temp);
					
				}
				to(start + 1, end, hi, temp, n, m);
				for (int i1 = 0; i1 < n; i1++) {
					for (int j1 = 0; j1 < m; j1++) {
						temp[i1][j1] = graph[i1][j1];
					}

				}

			}

		} else if (hi1.z == 2) {
			for (int i = 0; i < second.length; i++) {
				char[] e = second[i].toCharArray();
				for (int l = 0; l < e.length; l++) {
					temp = move(hi1.x, hi1.y, e[l], temp);
					
				}
				to(start + 1, end, hi, temp, n, m);
				for (int i1 = 0; i1 < n; i1++) {
					for (int j1 = 0; j1 < m; j1++) {
						temp[i1][j1] = graph[i1][j1];
					}

				}
			}

		}

		else if (hi1.z == 3) {
			for (int i = 0; i < third.length; i++) {
				char[] e = third[i].toCharArray();
				for (int l = 0; l < e.length; l++) {
					temp = move(hi1.x, hi1.y, e[l], temp);
					
				}
				to(start + 1, end, hi, temp, n, m);
				for (int i1 = 0; i1 < n; i1++) {
					for (int j1 = 0; j1 < m; j1++) {
						temp[i1][j1] = graph[i1][j1];
					}

				}
			}

		} else if (hi1.z == 4) {
			for (int i = 0; i < fourth.length; i++) {
				char[] e = fourth[i].toCharArray();
				for (int l = 0; l < e.length; l++) {
					temp = move(hi1.x, hi1.y, e[l], temp);
					
				}
				to(start + 1, end, hi, temp, n, m);
				

				for (int i1 = 0; i1 < n; i1++) {
					for (int j1 = 0; j1 < m; j1++) {
						temp[i1][j1] = graph[i1][j1];
					}

				}
			}

		} else if (hi1.z == 5) {
			for (int i = 0; i < five.length; i++) {
				char[] e = five[i].toCharArray();
				for (int l = 0; l < e.length; l++) {
					temp = move(hi1.x, hi1.y, e[l], temp);
				}
				to(start + 1, end, hi, temp, n, m);

				for (int i1 = 0; i1 < n; i1++) {
					for (int j1 = 0; j1 < m; j1++) {
						temp[i1][j1] = graph[i1][j1];
					}

				}
			}

		}

	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		buffer = new StringBuffer();
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		// 이렇게 해서 완전탐색을 해보도록 하자

		// char[] nw=second[0].toCharArray();
		ArrayList<go> hi = new ArrayList<>();
		StringTokenizer s = new StringTokenizer(in.readLine());

		n = Integer.parseInt(s.nextToken());
		m = Integer.parseInt(s.nextToken());
		graph = new int[n][m];
		graph1 = new int[n][m];
		for (int i = 0; i < n; i++) {
			s = new StringTokenizer(in.readLine());
			for (int j = 0; j < m; j++) {
				int ee = Integer.parseInt(s.nextToken());
				graph[i][j] = ee;
				graph1[i][j] = ee;
				if (graph[i][j] >= 1 && graph[i][j] <= 5) {
					hi.add(new go(i, j, graph[i][j]));
				}
			}
		}
		// 이렇게 해서 처리를 하였고
		result=Integer.MAX_VALUE;
		hx = new int[hi.size()];
		hy = new int[hi.size()];
		numbers = new int[hi.size()];
		isselected = new int[hi.size()];
		//// 아주 완전 탐색을 해야 겠어
		int count = 0;
		for (go i : hi) {
			hx[count] = i.x;
			hy[count] = i.y;
			count++;
		}
		to(0, hi.size(), hi, graph, n, m);
		System.out.println(result);
	}

}