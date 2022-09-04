import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static int v,e;
	static StringBuffer buffer;
	static List<node> [] list; 
	static int distance[];
	static int INF=100000000;
	static class node implements Comparable<node> {
		int  no, weight;

		public node(int no, int weight) {
			this.no = no;
			this.weight = weight;
		}

		@Override
		public int compareTo(node o) {
			// TODO Auto-generated method stub
			return this.weight-o.weight;
		}

	}

	public static void main(String[] args) throws IOException {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer s = new StringTokenizer(in.readLine());
		
		v = Integer.parseInt(s.nextToken());
		e = Integer.parseInt(s.nextToken());
		
		list=new ArrayList[v+1];
		distance=new int[v+1];
		buffer=new StringBuffer();
		int start=Integer.parseInt(in.readLine());
		Arrays.fill(distance, INF);
		distance[start]=0;
		for(int i=1;i<=v;i++)
		{
			list[i]=new ArrayList<>();
		}
		
		int a1,a2,a3;
		for(int i=0;i<e;i++)
		{
			s = new StringTokenizer(in.readLine());
			a1=Integer.parseInt(s.nextToken());
			a2=Integer.parseInt(s.nextToken());
			a3=Integer.parseInt(s.nextToken());
			
			list[a1].add(new node(a2,a3));
		}
		
		dik(start);
		for(int i=1;i<=v;i++) {
			if(distance[i]!=INF)
			{
				buffer.append(distance[i]+"\n");
			}
			else
			{
				buffer.append("INF\n");
			}
			
		}
		System.out.println(buffer);

	}

	private static void dik(int start) {
		// TODO Auto-generated method stub
		PriorityQueue<node> q=new PriorityQueue<>();
		int visit[]=new int[v+1];
		
		q.add(new node(start,0));

		while(!q.isEmpty()) {
			node a=q.poll();
			
			if(visit[a.no]==1)
				continue;
			visit[a.no]=1;
			
			for (node aa : list[a.no]) {
				
				if(distance[aa.no]>aa.weight+distance[a.no]) {
					distance[aa.no]=aa.weight+distance[a.no];
					q.add(new node(aa.no,distance[aa.no]));
					
				}
			}
			
			
			
			
			
		}
		
		
		
		
		
	}


}