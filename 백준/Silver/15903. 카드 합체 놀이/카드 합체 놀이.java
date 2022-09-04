import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		//점수를 가장 작게 만드는 것이 놀이의 목표이다.
		
		
		BufferedReader in= new BufferedReader(new InputStreamReader(System.in));
		int n,m;
		
		StringTokenizer s=new StringTokenizer(in.readLine());
		n=Integer.parseInt(s.nextToken());
		m=Integer.parseInt(s.nextToken());
		Queue<Long>sa=new PriorityQueue<Long>();
		s=new StringTokenizer(in.readLine());
		for(int l=0;l<n;l++)
		{
			sa.add(Long.parseLong(s.nextToken()));
		}
		for(int l=0;l<m;l++)
		{
			long a1=sa.poll();
			
			long a2=sa.poll();
			sa.add(a1+a2);
			sa.add(a1+a2);
		}
		long sum=0;
		while(!sa.isEmpty())
		{
			sum+=sa.poll();
		}
		System.out.println(sum);

	}

}