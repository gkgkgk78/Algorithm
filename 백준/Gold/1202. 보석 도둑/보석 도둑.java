import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static class data {
        int weight, value;

        public data(int a, int b) {
            this.weight = a;
            this.value = b;
        }

    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");

        int n, m;
        n = Integer.parseInt(s.nextToken());
        m = Integer.parseInt(s.nextToken());
        PriorityQueue<data> pq = new PriorityQueue<>((x, y) -> {
            return x.weight - y.weight;
        });

        for (int i = 0; i < n; i++) {
            s = new StringTokenizer(br.readLine(), " ");
            int a1, a2;
            a1 = Integer.parseInt(s.nextToken());
            a2 = Integer.parseInt(s.nextToken());
            pq.add(new data(a1, a2));
        }
        int bag[] = new int [m];
        for (int i = 0; i < m; i++) {
            s = new StringTokenizer(br.readLine(), " ");
            bag[i]=Integer.parseInt(s.nextToken());
        }
        Arrays.sort(bag);
        PriorityQueue<Integer> pq1 = new PriorityQueue<>((x, y) -> {
            return y - x;
        });
        Long answer = 0l;
        for (int i = 0; i < m; i++) {
            int now = bag[i];
            while (!pq.isEmpty()) {
                data temp = pq.peek();
                if (temp.weight <= now) {
                    pq1.add(temp.value);
                    pq.poll();
                } else {
                    break;
                }
            }
            if (!pq1.isEmpty()) {
                answer += Long.valueOf(pq1.poll());
            }
        }
        System.out.println(answer);

    }
}