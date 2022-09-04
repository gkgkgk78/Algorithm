import java.awt.BufferCapabilities;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int graph[];

	static List<go>[] hi;
	static int numbers[];
	static int isselected[];
	static int n;
	static int visit[];
	static int result=Integer.MAX_VALUE;
	static class go {

		int no;

		public go(int no) {
			this.no = no;
		}
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub

		// 1.조합으로 1부터 n-1까지의 경우의ㅣ 수를 ㅍ악
		// 2.구한 조합에서 싸이클이 존재하는지 파악

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		n = Integer.parseInt(in.readLine());
		graph = new int[n];
		hi = new ArrayList[n];
		StringTokenizer s = new StringTokenizer(in.readLine(), " ");
		for (int i = 0; i < n; i++) {
			graph[i] = Integer.parseInt(s.nextToken());
			hi[i] = new ArrayList<>();
		}

		for (int i = 0; i < n; i++) {
			s = new StringTokenizer(in.readLine(), " ");
			int t = Integer.parseInt(s.nextToken());
			for (int j = 0; j < t; j++) {
				hi[i].add(new go(Integer.parseInt(s.nextToken())-1));
			}
		}
//		for (List<go> a: hi) {
//			for (go a1 : a) {
//				System.out.print(a1.no+" ");
//			}
//			System.out.println();
//		}
		
		
		for (int i = 1; i < n; i++) {
			numbers = new int[i];
			comb(0, 0, i);
		}
		if(result!=Integer.MAX_VALUE)
		System.out.println(result);
		else
			System.out.println(-1);
	}

	private static void comb(int start, int cnt, int end) {
		// TODO Auto-generated method stub

		if (cnt == end) {

			int left[] = new int[n - cnt];
			int count = 0;
			for (int i = 0; i < n; i++) {
				int check = 0;
				for (int j = 0; j < cnt; j++) {
					if (numbers[j] == i) {
						check = 1;
						break;
					}
				}
				if (check == 0) {
					left[count] = i;
					count++;
				}
			}
			// 이제 나눠진 것들에 대해서 사이클 체크를 하도록 하자
			visit = new int[n];
			int check1=check_cycle(numbers, 0);
			if(check1==-1)
				return;
			
			visit = new int[n];
			int check2=check_cycle(left, 0);
			if(check2==-1)
				return;
			int left_sum=0;
			//System.out.println(Arrays.toString(numbers));
			//System.out.println(Arrays.toString(left));
			for(int i=0;i<cnt;i++) {
				left_sum+=graph[numbers[i]];
			}
			
			int right_sum=0;
			for(int i=0;i<n-cnt;i++) {
				right_sum+=graph[left[i]];
			}			
			result=Math.min(result,Math.abs(left_sum-right_sum));
			return;
		}

		for (int i = start; i < n; i++) {
			numbers[cnt] = i;
			comb(i + 1, cnt + 1, end);

		}

	}

	private static int check_cycle(int[] num, int cnt) {
		// TODO Auto-generated method stub
		
		Queue<Integer>q=new LinkedList<>(); 

		int g=0;
		visit[num[0]]=1;
		q.add(num[0]);
		if(num[0]==1)
		{
			g=78;
		}
		while(!q.isEmpty()) {
			int a1=q.poll();
			visit[a1] = 1;
			//System.out.println(a1);
			// 각 연결된 리스트에서 탐색을 진행 하도록 하자
			for (go a : hi[a1]) {
				int ch = check(num, a.no);
				if (ch == 1 && visit[a.no] == 0) {
					visit[a.no] = 1;
					q.add(a.no);
				}
			}	
		}

		
			// 이때는 모두 방문 했는지 파악 하도록함
			int check=0;
			for(int i=0;i<num.length;i++) {
				if(visit[num[i]]==1)
					check++;
			}
			if(check==num.length)
				return 1;
			return -1;


	}

	private static int check(int[] num, int no) {
		// TODO Auto-generated method stub
		for (int i = 0; i < num.length; i++) {
			if (num[i] == no) {
				return 1;
			}

		}

		return 0;
	}

}