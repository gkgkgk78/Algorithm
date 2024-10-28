import java.io.*;
import java.util.*;

//https://www.acmicpc.net/problem/1749
public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        int n, m;
        n = Integer.parseInt(s.nextToken());
        m = Integer.parseInt(s.nextToken());
        long array[][] = new long[n + 1][m + 1];
        long sumz[][] = new long[n + 1][m + 1];
        for (int i = 1; i <= n; i++) {
            s = new StringTokenizer(br.readLine(), " ");
            for (int j = 1; j <= m; j++) {
                array[i][j] = Integer.parseInt(s.nextToken());
            }
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                array[i][j] += array[i][j - 1];
            }
        }
        for (int j = 1; j <= m; j++) {
            for (int i = 1; i <= n; i++) {
                array[i][j] += array[i - 1][j];
            }
        }
        long answer = -Long.MIN_VALUE;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                for (int k = i; k <= n; k++) {
                    for (int l = j; l <= m; l++) {
                        long sum = array[k][l] - array[i - 1][l] - array[k][j - 1] + array[i - 1][j - 1];
                        answer = Math.max(answer, sum);
                    }
                }
            }
        }
        System.out.println(answer);

    }


}