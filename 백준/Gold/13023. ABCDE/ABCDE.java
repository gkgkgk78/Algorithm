import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static int graph[][];

	static int visit[];
	static int n;

	static ArrayList<go> temp;
	public static class go {

		int vertex;
		ArrayList<Integer> hi = new ArrayList<>();

		public go(int vertex, int a) {
			this.vertex = vertex;
			hi.add(a);
		}

		public go(int vertex) {
			this.vertex = vertex;
		}

	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		int m;
		
		StringTokenizer s = new StringTokenizer(in.readLine());
		n = Integer.parseInt(s.nextToken());
		m = Integer.parseInt(s.nextToken());
		// parents = new int[n];
		graph=new int[n][n];
		int a1, a2, a3;
		temp = new ArrayList<>();
		// graph = new int[n][n];
		for (int i = 0; i < n; i++) {
			temp.add(new go(i));

		}

		// System.out.println(Arrays.toString(parents));
		for (int j = 0; j < m; j++) {
			s = new StringTokenizer(in.readLine());
			a1 = Integer.parseInt(s.nextToken());
			a2 = Integer.parseInt(s.nextToken());
			// hll.get(a1).hi.add(a2);
			// union(a1, a2);
			temp.get(a1).hi.add(a2);
			temp.get(a2).hi.add(a1);
			graph[a1][a2]=1;
			graph[a2][a1]=1;
		}

//		ArrayList<Integer> temp = new ArrayList<>();
//		//단일 연결 그리고 최상위 부모
//		for (go as : hll) {
//			if(as.hi.size()==1&&parents[as.vertex]==as.vertex)
//				temp.add(as.vertex);
//		}

		for (int i = 0; i < n; i++) {
			visit = new int[n];
			dfs(i, 0);
		}
		System.out.println(0);

	}

	private static void dfs(int start, int depth) {
		// TODO Auto-generated method stub

		if (depth >= 4) {
			System.out.println(1);
			System.exit(0);
		}

		visit[start] = 1;
		go aa=temp.get(start);
		
		for (int t : aa.hi) {
			if (graph[start][t] == 1 && visit[t] == 0) {
				visit[t] = 1;
				dfs(t, depth + 1);
				visit[t] = 0;
			}
		} 
			
		

	}

}