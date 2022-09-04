import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws FileNotFoundException {
		// TODO Auto-generated method stub
		//System.setIn(new FileInputStream("src/input.txt"));
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		
		int sum=0;
		while(n>=0)
		{
			if(n%5==0)
			{
				sum+=(n/5);
				System.out.println(sum);
				System.exit(0);
				
			}
			n-=3;
			sum++;
	
		}
		System.out.println(-1);
		

	}

}