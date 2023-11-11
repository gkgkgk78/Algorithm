import java.util.*;
import java.io.*;


public class Main {


    public static class go {
        String name;
        int x1, x2, x3;

        public go(String name, int x1, int x2, int x3) {
            this.name = name;
            this.x1 = x1;
            this.x2 = x2;
            this.x3 = x3;
        }
    }


    public static void main(String[] args) throws Exception {

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(in.readLine(), " ");
        int n = Integer.parseInt(s.nextToken());

        List<go> list = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            s = new StringTokenizer(in.readLine(), " ");
            String x1;
            int x2, x3, x4;
            x1 = s.nextToken();
            x2 = Integer.parseInt(s.nextToken());
            x3 = Integer.parseInt(s.nextToken());
            x4 = Integer.parseInt(s.nextToken());
            list.add(new go(x1, x2, x3, x4));
        }
        list.sort((x, y) -> {
            if (x.x1 != y.x1)
                return y.x1 - x.x1;
            if (x.x2 != y.x2)
                return x.x2 - y.x2;
            if (x.x3 != y.x3)
                return y.x3 - x.x3;
            return x.name.compareTo(y.name);
        });
        for (go a : list) {
            System.out.println(a.name );

        }


    }


}