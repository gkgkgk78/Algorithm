import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");

        int n, m;
        n = Integer.parseInt(s.nextToken());
        m = Integer.parseInt(s.nextToken());
        int e[] = new int[n];
        s = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < n; i++) {
            e[i] = Integer.parseInt(s.nextToken());
        }
        int a1, a2, a3;
        int data[] = new int[n + 1];
        for (int i = 0; i < m; i++) {
            s = new StringTokenizer(br.readLine(), " ");
            a1 = Integer.parseInt(s.nextToken());
            a2 = Integer.parseInt(s.nextToken());
            a3 = Integer.parseInt(s.nextToken());
            a1 -= 1;
            a2 -= 1;
            data[a1] += a3;
            data[a2 + 1] -= a3;
        }
        for (int i = 1; i < n + 1; i++) {
            data[i] += data[i - 1];
        }
        for (int i = 0; i < n; i++) {
            e[i] += data[i];
            System.out.print(e[i] + " ");
        }


    }
}