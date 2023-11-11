import java.util.*;
import java.io.*;


public class Main {


    public static class go {
        int vertex;
        long value;

        public go(int vertex, long value) {
            this.vertex = vertex;
            this.value = value;
        }
    }

    public static List<go> list[];

    public static long[] dijk(int start, int last, int n, long value, long total) {
        long distace[] = new long[n + 1];
        for (int i = 0; i < distace.length; i++)
            distace[i] = 1000000001;
        PriorityQueue<go> q = new PriorityQueue<>((x, y) -> {
            return (int) (x.value - y.value);
        });
        distace[start] = 0;
        q.add(new go(start, 0));
        while (q.size() > 0) {
            go a = q.poll();
            if (distace[a.vertex] > a.value)
                continue;
            List<go> gg = list[a.vertex];
            for (go a1 : gg) {
                if (a1.value > value)
                    continue;
                long mi = a1.value + a.value;
                if (distace[a1.vertex] > mi && mi <= total) {
                    distace[a1.vertex] = mi;
                    q.add(new go(a1.vertex, mi));
                }
            }
        }

        return distace;

    }

    public static void main(String[] args) throws Exception {

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(in.readLine(), " ");
        int n, m, a, b, c;
        n = Integer.parseInt(s.nextToken());
        m = Integer.parseInt(s.nextToken());
        a = Integer.parseInt(s.nextToken());
        b = Integer.parseInt(s.nextToken());
        c = Integer.parseInt(s.nextToken());
        list = new List[n + 1];
        for (int i = 0; i <= n; i++)
            list[i] = new LinkedList<>();
        for (int i = 0; i < m; i++) {
            int a1, a2;
            long a3;
            s = new StringTokenizer(in.readLine(), " ");
            a1 = Integer.parseInt(s.nextToken());
            a2 = Integer.parseInt(s.nextToken());
            a3 = Long.parseLong(s.nextToken());
            list[a1].add(new go(a2, a3));
            list[a2].add(new go(a1, a3));
        }
        //이제 시작 해 보도록 하자

        long left = -1;
        long right = c + 1;
        long answer = 10000000000000001L;
        while (left + 1 < right) {
            long mid = (left + right) / 2;
            long[] arr = dijk(a, b, n, mid, c);
            //System.out.println(mid+" "+Arrays.toString(arr));
            if (arr[b] <= c) {
                right = mid;
                answer = Math.min(answer, right);
            } else
                left = mid;
        }

        if (answer == 10000000000000001L)
            System.out.println(-1);
        else
            System.out.println(answer);

    }


}