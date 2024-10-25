import javax.naming.spi.ObjectFactory;
import java.awt.*;
import java.awt.image.AreaAveragingScaleFilter;
import java.beans.VetoableChangeListener;
import java.io.*;
import java.security.cert.CertificateParsingException;
import java.util.*;
import java.util.List;


public class Main {


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        int n, m;
        n = Integer.parseInt(s.nextToken());
        m = Integer.parseInt(s.nextToken());

        //길이 n짜리 수열이 주어진다
        //수열의 부분합 중에 그 합이 s이상이 되는것 , 가장 짧은 것의 길이를 구하도록 하자
        List<Integer> list = new ArrayList<>();
        Integer[] array = new Integer[n];
        s = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < n; i++) {
            list.add(Integer.parseInt(s.nextToken()));
        }
        array = list.stream().toArray(Integer[]::new);
        Long answer = Long.MAX_VALUE;

        int sum = array[0];
        int left = 0;
        int right = 0;
        if (sum >= m) {
            answer = Math.min(answer, right - left + 1);
        }
        while (right < n) {
            right += 1;
            if (right >= n)
                break;
            sum += array[right];
            if (sum >= m) {
                answer = Math.min(answer, right - left + 1);
                while (left < right) {
                    sum -= array[left];
                    left += 1;
                    if (sum >= m) {
                        answer = Math.min(answer, right - left + 1);
                    } else
                        break;
                }
            }

            if (sum >= m) {
                answer = Math.min(answer, right - left + 1);
            }
        }

        if (answer == Long.MAX_VALUE)
            System.out.println(0);
        else
            System.out.println(answer);

    }


}