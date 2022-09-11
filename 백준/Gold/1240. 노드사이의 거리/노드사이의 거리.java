import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static List<go>[] arr;
	static StringBuffer buffer;
	static class go{
		int x,val;
		
	
		public go(int x, int val) {
		
			this.x = x;
			this.val = val;
		}	
		

	}
	static int n;
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader in= new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer s=new StringTokenizer(in.readLine()," ");
		int m;
		n=Integer.parseInt(s.nextToken());
		m=Integer.parseInt(s.nextToken());
		arr=new ArrayList[n];
		buffer=new StringBuffer();
		for(int i=0;i<n;i++) {
			arr[i]=new ArrayList<>();
			
		}
		for(int i=0;i<n-1;i++) {
			s=new StringTokenizer(in.readLine()," ");
			int a1,a2,a3;
			a1=Integer.parseInt(s.nextToken());
			a2=Integer.parseInt(s.nextToken());
			a3=Integer.parseInt(s.nextToken());
			a1--;
			a2--;
			arr[a1].add(new go(a2,a3));
			arr[a2].add(new go(a1,a3));
		}
		
		for(int i=0;i<m;i++) {
			s=new StringTokenizer(in.readLine()," ");
			int a1,a2,a3;
			
			a1=Integer.parseInt(s.nextToken());
			a2=Integer.parseInt(s.nextToken());
			a1--;
			a2--;
			//System.out.println(a1+" "+a2);
			int z=bfs(a1,a2);
			buffer.append(z+"\n");
		}
			System.out.println(buffer);

	}


	private static int bfs(int a1, int a2) {
		// TODO Auto-generated method stub
		
		int visit[]=new int[n];
		
		Queue<go> q=new LinkedList<>();
		q.add(new go(a1,0));
		while(!q.isEmpty()) {
			go a=q.poll();
			visit[a.x]=1;
			for (go g : arr[a.x]) {
				if(visit[g.x]==0) {
					if(g.x==a2)
					{
						
						return(a.val+g.val);
					}
					q.add(new go(g.x,a.val+g.val));
					visit[g.x]=1;
					
				}
			}
			
			
			
		}
		
		return -1;
		
	}
	

	
}