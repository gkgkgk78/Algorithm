import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static StringBuffer buffer;

	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		buffer = new StringBuffer();
		StringTokenizer s = new StringTokenizer(in.readLine());
		int t = Integer.parseInt(s.nextToken());

		for (int i = 0; i < t; i++) {
			int n = Integer.parseInt(in.readLine());
			int arr[] = new int[n];
			int lis[]=new int[n];
			s = new StringTokenizer(in.readLine(), " ");
			for (int j = 0; j < n; j++) {
				arr[j] = Integer.parseInt(s.nextToken());

			}
			int max=0;
			for(int j=0;j<n;j++) {
				
				lis[j]=1;
				for(int k=0;k<=j-1;k++) {
					
					if(arr[k]<arr[j]&&lis[j]<lis[k]+1)
						lis[j]=lis[k]+1;
					
				}
				max=Math.max(max, lis[j]);
				
			}
			buffer.append("#"+(i+1)+" "+max+"\n");
			

		}
		System.out.println(buffer);

	}

}