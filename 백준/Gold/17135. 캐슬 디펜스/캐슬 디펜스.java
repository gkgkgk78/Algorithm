import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	static int graph[][];
	static int numbers[];
	static int input[];
	static int n, m, d;
	static int result;
	public static class go {
		int x, y;

		public go(int x, int y) {

			this.x = x;
			this.y = y;
		}

	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer s = new StringTokenizer(in.readLine());
		ArrayList<go> hi = new ArrayList<>();
		n = Integer.parseInt(s.nextToken());
		m = Integer.parseInt(s.nextToken());
		d = Integer.parseInt(s.nextToken());
		numbers = new int[3];
		result=Integer.MIN_VALUE;
		input = new int[m];
		graph = new int[n + 1][m];
		for (int i = 0; i < n; i++) {
			s = new StringTokenizer(in.readLine());
			for (int j = 0; j < m; j++) {
				graph[i][j] = Integer.parseInt(s.nextToken());
				if (graph[i][j] == 1) {
					hi.add(new go(i, j));
				}
			}
		}
		for (int j = 0; j < m; j++) {
			input[j] = j;
		}

		comb(0, 0, m, hi);// cnt start end
		System.out.println(result);
	}

	private static void comb(int cnt, int start, int k, ArrayList<go> hi) {
		// TODO Auto-generated method stub
		if (cnt == 3) {
			//System.out.println(Arrays.toString(numbers));

			for (int j = 0; j < 3; j++) {
				graph[n][numbers[j]] = 1;
			}

			attack(hi);
			for (int j = 0; j < 3; j++) {
				graph[n][numbers[j]] = 0;
			}
			// 이제 공격을 시작하도록 하자
			return;
		}

		for (int i = start; i < k; i++) {
			numbers[cnt] = input[i];
			comb(cnt + 1, i + 1, k, hi);
		}
		
	}

	private static void attack(ArrayList<go> hi) {
		// TODO Auto-generated method stub
		int ct=0;
		ArrayList<go> hi1 = new ArrayList<>();
		for (go g : hi) {
			hi1.add(new go(g.x, g.y));

		}
		int graph1[][]=new int[n+1][m];
		for (int i = 0; i < n+1; i++) {
			for (int j = 0; j < m; j++) {
				graph1[i][j]=graph[i][j];
			}
		}
		while (true) {
			// 궁수 공격

			ArrayList<go> death = new ArrayList<>();
			for (int i = 0; i < m; i++) {
				if (graph1[n][i] == 1) {
					int lo = Integer.MAX_VALUE;
					ArrayList<go> temp = new ArrayList<>();// 각 궁수마다 제거할 얘 선택할 것들
					// 모든 궁수의 위치를 파악하여서 가까운 위치에 있다면
					for (go g : hi1) {//여기는 적들
						int tx = Math.abs(g.x - (n ));
						int ty = Math.abs(g.y - (i));

						if (tx + ty <= d) {
							if (tx + ty < lo) {// 최저 거리가 변경이 되어야 하는 상황임
								if (lo != Integer.MAX_VALUE)// 지금 가장 처음이 아니고 ㄷ작은 얘가 나옴
								{
									temp = new ArrayList<>();
									temp.add(new go(g.x, g.y));
									lo = tx + ty;
								} else// 처음 삽입시
								{
									temp.add(new go(g.x, g.y));
									lo = tx + ty;
								}

							} else if (tx + ty == lo)// 거리가 같은게 있다면 우선 넣고 보자
							{
								temp.add(new go(g.x, g.y));
							}

						}

					}
					//이제 각 포문을 돌면서 가장 왼쪽에 있는 적을 추가 y값이 가장 작은얘
					int y=Integer.MAX_VALUE;
					int x=0;
					//System.out.println("hi");
					for (go g1 : temp) {
						//System.out.println(g1.x+" "+g1.y);
						if (g1.y<y)
						{
							x=g1.x;
							y=g1.y;
						}
					}
					if(y!=Integer.MAX_VALUE)
						death.add(new go(x,y));

				}

			}
			
			
			
			// 공격받은 적 체크한후 제거
			for (go g1 : death) {
				//System.out.println(g1.x+" "+g1.y);
				if(graph1[g1.x][g1.y]==1)
					
				{	graph1[g1.x][g1.y]=0;
					ct++;
				}
			}


			// 공격끝난후 적 한칸아래씩 이동
			for(int i=hi1.size()-1;i>=0;i--)
			{
				go aa=hi1.get(i);
				if(graph1[aa.x][aa.y]==0)
					hi1.remove(i);
				else
				{
					if (aa.x+1!=n)
						graph1[aa.x+1][aa.y]=1;
					graph1[aa.x][aa.y]=0;
					aa.x=aa.x+1;
				}
			}

			// 만약 성이있는 칸으로 이동시 제거
			for(int i=hi1.size()-1;i>=0;i--)
			{
				go aa=hi1.get(i);
				if(aa.x==n)
					hi1.remove(i);
				
			}
			
			if(hi1.size()==0)
			{
				
				result=Integer.max(ct, result);
				break;
			}
			
		}

	}

}