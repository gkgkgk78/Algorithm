import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader in=new BufferedReader(new InputStreamReader(System.in));
		
		int a=Integer.parseInt(in.readLine());
		
		PriorityQueue<Integer>hu=new PriorityQueue<>(Collections.reverseOrder());
		
		
		for(int i=0;i<a;i++)
		{
			StringTokenizer jo=new StringTokenizer(in.readLine());
			int a1[]=new int[a];
			for(int j=0;j<a;j++)
			{
				hu.add(Integer.parseInt(jo.nextToken()));
			}
			
			
		}
		for(int i=0;i<a-1;i++)
		{
		hu.poll();
		}
		System.out.println(hu.poll());
		
		
		
		
		
		
		

	}

}