import javax.naming.spi.ObjectFactory;
import java.awt.*;
import java.awt.image.AreaAveragingScaleFilter;
import java.beans.VetoableChangeListener;
import java.io.*;
import java.util.*;
import java.util.List;


public class Main {


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(s.nextToken());
        int array[] = new int[1000002];
        for (int i = 0; i < n; i++) {
            s = new StringTokenizer(br.readLine(), " ");
            int a1, a2;
            a1 = Integer.parseInt(s.nextToken());
            a2 = Integer.parseInt(s.nextToken());
            array[a1] += 1;
            array[a2+1] -= 1;
        }
        for (int i = 1; i < 1000002; i++) {
            array[i] += array[i - 1];
        }
        s = new StringTokenizer(br.readLine(), " ");
        int m = Integer.parseInt(s.nextToken());
        s = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < m; i++) {
            System.out.println(array[Integer.parseInt(s.nextToken())]);
        }


    }


}