import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int degree[];
	static int time[],n;
	static List<List<Integer>> list;

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(in.readLine());
		degree = new int[n];
		time = new int[n];
		list = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			list.add(new ArrayList<>());
		}

		for (int i = 0; i < n; i++) {
			StringTokenizer s = new StringTokenizer(in.readLine(), " ");
			time[i] = Integer.parseInt(s.nextToken());
			int z=Integer.parseInt(s.nextToken())-1;
			if(z==-1)
				continue;
			while (s.hasMoreTokens()) {
				z=Integer.parseInt(s.nextToken())-1;
				
			
				degree[z]+=1;
				list.get(i).add(z);
			}
		}
		
		topo();
		

	}

	private static void topo() {
		// TODO Auto-generated method stub
		Queue<Integer>q=new LinkedList<Integer>();
		int []max=new int[n];
		for (int i = 0; i < n; i++) {
			max[i]=time[i];
			if(degree[i]==0)
			{
				q.add(i);
			}
		}
		int timez=0;
		while(!q.isEmpty()) {
			
			int t=q.poll();
			timez+=time[t];
			for (Integer i : list.get(t)) {
				degree[i]-=1;
				max[i]=Math.max(max[i],time[i]+max[t]);
				if(degree[i]==0)
					q.add(i);
			}
			
			
		}
		int m=0;
		for (int i = 0; i < n; i++) {
			m=Math.max(max[i], m);
		}
		System.out.println(m);
		
		
		
	}

}