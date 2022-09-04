import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

	static int n;

	static int visit[];
	static int graph[][];
	static int sx;
	static int result=Integer.MAX_VALUE;


	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		n = Integer.parseInt(in.readLine());

		graph=new int[n][n];
		for (int i = 0; i <n; i++) {
			StringTokenizer s = new StringTokenizer(in.readLine(), " ");
			for (int j = 0; j <n; j++) {
				int a = Integer.parseInt(s.nextToken());
				if (a != 0) {
				
					graph[i][j]=a;
				}
				
			}
		}

		for (int i = 0; i <n; i++) {
			visit = new int[n ];
			sx=i;
			visit[i]=1;
			dfs(i,0,0);
			visit[i]=0;
		}
		System.out.println(result);
		
		
		
	}
	
	
	
	private static void dfs(int start, int depth,int sum) {	
		// TODO Auto-generated method stub	
		
		
		if(depth==n-1) {				
			int z=sum+graph[start][sx];
			//System.out.println(start+" "+depth+" "+sx+" "+sum);			
			if(graph[start][sx]>0)
				result=Math.min(result,z);
			return;
		}	
		int check=-1;
		int val=Integer.MAX_VALUE;
		for(int i=0;i<n;i++) {
			if(graph[start][i]>0&&visit[i]==0) {
				visit[i]=1;
				dfs(i,depth+1,sum+graph[start][i]);
				visit[i]=0;
			}	
		}
		
		
		
		
		
	}

}