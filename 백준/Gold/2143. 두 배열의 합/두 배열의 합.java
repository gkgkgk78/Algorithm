import java.io.*;
import java.security.cert.CertificateParsingException;
import java.util.*;


public class Main {

    public static int upper(Integer[] arr, int now) {
        int left = -1;
        int right = arr.length;
        while (left + 1 < right) {
            int mid = (left + right) / 2;
            if (arr[mid] <= now)
                left = mid;
            else
                right = mid;
        }
        return left;
    }

    public static int lower(Integer[] arr, int now) {
        int left = -1;
        int right = arr.length;
        while (left + 1 < right) {
            int mid = (left + right) / 2;
            if (arr[mid] >= now)
                right = mid;
            else
                left = mid;
        }
        return right;
    }


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        int t = Integer.parseInt(s.nextToken());
        s = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(s.nextToken());
        int[] arr1 = new int[n];

        s = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < n; i++) {
            arr1[i] = Integer.parseInt(s.nextToken());
        }
        s = new StringTokenizer(br.readLine(), " ");
        int m = Integer.parseInt(s.nextToken());
        int[] arr2 = new int[m];
        s = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < m; i++) {
            arr2[i] = Integer.parseInt(s.nextToken());
        }

        List<Integer> list1 = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int temp = arr1[i];
            list1.add(temp);
            for (int j = i + 1; j < n; j++) {
                temp += arr1[j];
                list1.add(temp);
            }
        }
        list1.sort((x, y) -> {
            return x - y;
        });
        List<Integer> list2 = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int temp = arr2[i];
            list2.add(temp);
            for (int j = i + 1; j < m; j++) {
                temp += arr2[j];
                list2.add(temp);
            }
        }
        list2.sort((x, y) -> {
            return x - y;
        });

        Integer lArr1[] = new Integer[list1.size()];
        lArr1 = list1.toArray(lArr1);
        Integer lArr2[] = new Integer[list2.size()];
        lArr2 = list2.toArray(lArr2);
        Long answer = 0l;
        for (int i = 0; i < lArr1.length; i++) {
            int now = t - lArr1[i];
            //이제 가능한 범위를 찾도록 하자
            int left = upper(lArr2, now);
            int right = lower(lArr2, now);
            if (0 <= left && left < lArr2.length && 0 <= right && right < lArr2.length)
                answer += (left - right + 1);
        }
        System.out.println(answer);


    }
}