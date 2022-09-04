import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static StringBuffer buffer;
	
	public static double com(double a,double b)
	{
		double sum1=1;
		double sum2=1;
		double sum3=1;
		
		
		for(double i=(a);i>0;i--)
		{
			sum1*=i;
		}
				
		for(double i=(b-a);i>0;i--)
		{
			sum2*=i;
		}
				
		for(double i=(b);i>0;i--)
		{
			sum3*=i;
		}
		
		return(sum3/(sum1*sum2));
		
		
	}
	
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		buffer = new StringBuffer();
		int n=Integer.parseInt(in.readLine());
		
		for(int i=0;i<n;i++)
		{
			StringTokenizer aa=new StringTokenizer(in.readLine());
			double x=Double.parseDouble(aa.nextToken());
			double y=Double.parseDouble(aa.nextToken());
			double hi=com(x, y);
			System.out.printf("%.0f",hi);
			System.out.println();
		}
		//System.out.println(buffer);
		
	}

}