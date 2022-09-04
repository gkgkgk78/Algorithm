import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static StringBuffer buffer;
	static int[] check;
	static int[] sin;
	static int[] se;
	static int ans;

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		buffer = new StringBuffer();

		
		sin = new int[9];
		se = new int[9];
		check = new int[9];

		for (int i = 0; i < 9; i++) {
			StringTokenizer s = new StringTokenizer(in.readLine());
			int a1 = Integer.parseInt(s.nextToken());	
			sin[i] = a1;
		}

		go(0, 0, 9,0);
	
	}

	private static void go(int start, int ssin, int n,int count) {

		if (count==7) {
			
			if(ssin==100)
			{
				for(int i=0;i<9;i++)
				{
					if(check[i]==1)
					{
						System.out.println(sin[i]);
					}
				}
				System.exit(0);
			}
			else
				return;
		}
		if(start==9)
			return;
		check[start]=1;
		go(start + 1, ssin + sin[start],  n,count+1);
		check[start]=0;
		go(start + 1, ssin,n,count);

	}

}