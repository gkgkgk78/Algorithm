

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {


    static int n, m;

    static class go {
        int vertex;
        long value;

        go(int vertex, long value) {
            this.vertex = vertex;
            this.value = value;
        }
    }

    static List<List<go>> graph = new ArrayList<>();

    public static int dijk(int start, int fin, long cost, long ma) {
        //cost 가 최대 비용
        //ma가 하나의  edgd당 갈수있는지

        long distnace[] = new long[n + 1];
        for (int i = 0; i <= n; i++) {
            distnace[i] = Integer.MAX_VALUE;
        }
        PriorityQueue<go> q = new PriorityQueue<>((x, y) -> {
            return Long.compare(x.value, y.value);
        });
        q.add(new go(start, 0));
        distnace[start] = 0;
        while (!q.isEmpty()) {
            go a = q.poll();
            if(a.value>distnace[a.vertex])
                continue;
            for (go now : graph.get(a.vertex)) {
                long temp = a.value + now.value;
                if (temp > distnace[now.vertex] || now.value > ma || temp > cost)
                    continue;
                distnace[now.vertex] = temp;
                q.add(new go(now.vertex, temp));
                if (now.vertex == fin) {
                    return 1;
                }
            }
        }
        return -1;

    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int a, b;
        long c;
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        c = Long.parseLong(st.nextToken());
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        long right = 0;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            graph.get(from).add(new go(to, weight));
            graph.get(to).add(new go(from, weight));
            right = Math.max(right, weight);
        }
        long left = -1;
        long answer = Long.MAX_VALUE;
        right += 1;
        while (left + 1 < right) {
            long mid = (left + right) / 2;
            int temp = dijk(a, b, c, mid);
            if (temp == 1) {
                right = mid;
                answer = mid;
            } else
                left = mid;
        }
        if (answer == Long.MAX_VALUE)
            System.out.println(-1);
        else
            System.out.println(answer);


    }


}
