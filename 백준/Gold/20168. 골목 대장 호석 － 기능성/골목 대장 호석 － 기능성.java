

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {


    public static class go {
        int ver, weight;

        go(int ver, int weight) {
            this.ver = ver;
            this.weight = weight;
        }
    }

    static List<List<go>> graph;
    static int[] distance;
    static int n;

    public static int dijk(int start, int gone, int c, long check) {

        PriorityQueue<go> q = new PriorityQueue<>((x, y) -> {
            return x.weight - y.weight;
        });
        for (int i = 1; i <= n; i++) {
            distance[i] = Integer.MAX_VALUE;
        }
        distance[start] = 0;
        q.add(new go(start, 0));
        int temp = Integer.MAX_VALUE;

        while (!q.isEmpty()) {
            go a = q.poll();
            if (a.ver == gone) {
                temp = Math.min(temp, distance[gone]);
                continue;
            }
            if (a.weight > distance[a.ver]) continue;

            for (go g : graph.get(a.ver)) {
                int now = a.weight + g.weight;
                if (distance[g.ver] < now || g.weight > check)
                    continue;
                if (now > c)
                    continue;
                distance[g.ver] = now;
                q.add(new go(g.ver, now));
            }
        }
        if (temp == Integer.MAX_VALUE)
            return -1;
        else
            return 1;

    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int m, a, b, c;
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        graph = new ArrayList<>();
        distance = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        long left = 0;
        long right = c + 1;
        long answer = Integer.MAX_VALUE;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            graph.get(from).add(new go(to, weight));
            graph.get(to).add(new go(from, weight));

        }

        while (left + 1 < right) {
            long mid = (left + right) / 2;
            int result = dijk(a, b, c, mid);
            if (result == 1) {
                right = mid;
                answer = mid;
            } else {
                left = mid;
            }
        }
        if (answer == Integer.MAX_VALUE)
            System.out.println(-1);
        else
            System.out.println(answer);


    }

}
