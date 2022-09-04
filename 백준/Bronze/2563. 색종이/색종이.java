import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();

		int graph[][] = new int[100][100];
		int count = 0;
		for (int i = 0; i < n; i++) {
			int a1 = sc.nextInt();
			int a2 = sc.nextInt();

			
			for (int k1 = a1; k1 < a1 + 10; k1++) {
				for (int k2 = a2; k2 < a2 + 10; k2++) {
					if (graph[k1][k2] == 0) {
						graph[k1][k2] = 1;
						count += 1;
					} else
						continue;

				}

			}

		}

		System.out.println(count);

	}

}