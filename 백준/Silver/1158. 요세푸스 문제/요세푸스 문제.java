import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {

		

		// BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();

		int total[] = new int[n];
		int result[] = new int[n];
		int index = 0;
		int start = m;

		for (int i = 0; i < n; i++)

		{
			total[i] = i + 1;
		}
		
		int hk=11;
		while (true) {
			hk=0;
			result[index] = total[start-1];
			start=start-1;
			total[start] = 0;
			index++;
			int count = 0;
			while (true) {

				start++;
				if (start == n)
					start = 0;
				if (total[start] != 0) {

					count++;
				}

				if (count == m) {
					result[index] = total[start];
					total[start]=0;
					count=0;
					index++;
				}

				if (index == n )
				{	System.out.print("<");
					for(int i=0;i<result.length-1;i++)
					{
						
						System.out.print(result[i]+", ");
					}
					System.out.print(result[result.length-1]);
					System.out.println(">");
					System.exit(0);
				}
			}
//			while (true) {
//
//				start++;
//				if (start == n)
//					start = 0;
//				if (total[start] != 0) {
//					result[index] = total[start];
//					index++;
//
//					
//				}
//			
//
//				if (index == n )
//				{	System.out.print("<");
//					for(int i=0;i<result.length-1;i++)
//					{
//						
//						System.out.print(result[i]+", ");
//					}
//					System.out.print(result[result.length-1]);
//					System.out.println(">");
//					System.exit(0);
//				}
//
//			}
			
		}
		
	}

}