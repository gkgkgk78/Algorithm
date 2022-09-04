import java.util.Scanner;

public class Main {
	static StringBuffer buffer;
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();
		buffer = new StringBuffer();
		int arr[] = new int[m + 1];

		for (int i = 2; i <= m; i++) {
			int j = i;
			while (j <= m) {
				arr[j] += 1;
				j = j + i;
			}

		}
		for (int i = n; i <= m; i++) {
			if (arr[i] == 1)
				buffer.append(i+"\n");
		}
		System.out.println(buffer);
	}

}