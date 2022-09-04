import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		sc.nextLine();
		int la[] = new int[n];
		String[] z1 = sc.nextLine().split(" ");
		int i = 0;
		for (i = 0; i < n; i++) {
			la[i] = Integer.parseInt(z1[i]);
		}
		int n1 = sc.nextInt();
		sc.nextLine();

		for (i = 0; i < n1; i++) {
			int a1 = sc.nextInt();
			int a2 = sc.nextInt();
			a2--;
			//sc.nextLine();

			if (a1 == 1) {
				int a3 = a2;
				while (a3 < n) {
					if (la[a3] == 1)
						la[a3] = 0;
					else
						la[a3] = 1;
					a3 += (a2 + 1);
				}

			} else {
				if (la[a2] == 1)
					la[a2] = 0;
				else
					la[a2] = 1;
				int l1 = a2 - 1;
				int l2 = a2 + 1;
				while (l1 >= 0 && l2 < n) {

					if (la[l1] == la[l2]) {
						if (la[l1] == 0) {
							la[l1] = 1;
							la[l2] = 1;
						} else {
							la[l1] = 0;
							la[l2] = 0;

						}

					} else
						break;

					l1 -= 1;
					l2 += 1;

				}

			}

		}
		
		for (i = 0; i < n; i++) {
			if (i > 0&&i % 20 == 0)
				System.out.println();
			System.out.print(la[i] + " ");

		}
		System.out.println();

	}

}