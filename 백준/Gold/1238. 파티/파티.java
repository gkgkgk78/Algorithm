

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {


    static class go {
        int vertex, value;

        go(int vertex, int value) {
            this.vertex = vertex;
            this.value = value;
        }
    }


    static List<List<go>> graph = new ArrayList<>();

    public static int dijk(int start, int fin, int n) {
        PriorityQueue<go> q = new PriorityQueue<>((x, y) -> {
            return x.value - y.value;
        });
        int distance[] = new int[n + 1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[start] = 0;
        q.add(new go(start, 0));
        int answer = -1;
        while (!q.isEmpty()) {
            go a = q.poll();
            if (a.value > distance[a.vertex])
                continue;
            if (a.vertex == fin) {
                answer = a.value;
                break;
            }
            for (go now : graph.get(a.vertex)) {
                int temp = now.value + a.value;
                if (temp < distance[now.vertex]) {
                    distance[now.vertex] = temp;
                    q.add(new go(now.vertex, temp));
                }
            }
        }
        return answer;

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n, m, x;
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int a, b, c;
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            graph.get(a).add(new go(b, c));
        }
        int temp = -1;
        int vertex = -1;
        for (int i = 1; i <= n; i++) {
            int first = dijk(i, x, n);
            int second = dijk(x, i, n);
            if (first + second > temp) {
                temp = first + second;
                vertex = i;
            }
        }
        System.out.println(temp);

    }


}
