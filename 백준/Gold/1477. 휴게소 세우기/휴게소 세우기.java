import java.io.*;
import java.lang.reflect.AnnotatedArrayType;
import java.util.*;

public class Main {


    public static int find(int[] array, int mid) {
        int count = 0;
        int before = array[0];
        for (int i = 1; i < array.length; i++) {
            count += (array[i] - before-1) / mid;
            before = array[i];
        }
        return count;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        int n, m, l;
        n = Integer.parseInt(s.nextToken());
        m = Integer.parseInt(s.nextToken());
        l = Integer.parseInt(s.nextToken());
        int[] array = new int[n+2];
        s = new StringTokenizer(br.readLine(), " ");
        for (int i = 1; i < n+1; i++) {
            array[i] = Integer.parseInt(s.nextToken());
        }
        array[n+1] = l;
        Arrays.sort(array);
        int left = 0;
        int right = l-1 ;
        while (left + 1 < right) {
            int mid = (left + right) / 2;
            int next = find(array, mid);
            if (next <= m) {
                right = mid;
            } else
                left = mid;
        }
        System.out.println(right);

    }

}