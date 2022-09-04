import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	static StringBuffer buffer;

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		buffer = new StringBuffer();

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(in.readLine());
		StringTokenizer s = new StringTokenizer(in.readLine());
	
		
		int count = 1;
		Stack<int[]> stack = new Stack<>();
		// push pop peek
		for (int i = 0; i < n; i++) {
			int h = Integer.parseInt(s.nextToken());
			//System.out.println(h);

			while (!stack.isEmpty()) {
				if (stack.peek()[0] < h)
					stack.pop();
				else {
					//System.out.println("hi"+stack.peek()[1]+" ");
					buffer.append(stack.peek()[1] + " ");
					break;
				}
			}
			if (stack.empty()) {
				//System.out.println("hi1"+"0 ");
				//System.out.println();
				buffer.append("0 ");
			}
			stack.push(new int[] { h, i + 1 });

		}

		System.out.println(buffer);

	}

}