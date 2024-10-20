import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.security.cert.CertificateParsingException;
import java.util.*;


public class Main {

    public static int go(Integer[] array, int mid, int c) {

        int before = array[0];
        int count = 1;
        for (int i = 1; i < array.length; i++) {
            int temp = array[i] - before;
            if (temp >= mid) {
                before = array[i];
                count += 1;
            }
        }

        return count;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        BufferedReader br = new BufferedReader(new FileReader("src/input.txt"));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        int n, c;
        n = Integer.parseInt(s.nextToken());
        c = Integer.parseInt(s.nextToken());
        Integer[] array = new Integer[n];
        for (int i = 0; i < n; i++) {
            s = new StringTokenizer(br.readLine(), " ");
            array[i] = Integer.parseInt(s.nextToken());
        }
        Arrays.sort(array, (x, y) -> {
            return x - y;
        });
        int left = 1;
        int right = array[n - 1]-array[0] + 1;
        while (left + 1 < right) {
            int mid = (left + right) / 2;
            int now = go(array, mid, c);
            if (now >= c)
                left = mid;
            else
                right = mid;
        }
        System.out.println(left);


    }
}