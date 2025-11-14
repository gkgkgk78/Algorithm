import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    static int n, m, a, b;
    static long C;
    static List<List<Edge>> graph;
    static long[] dist;

    static class Edge implements Comparable<Edge> {
        int vertex;
        long cost;   // 이 간선까지의 누적 비용 or 간선 비용

        Edge(int vertex, long cost) {
            this.vertex = vertex;
            this.cost = cost;
        }

        @Override
        public int compareTo(Edge o) {
            return Long.compare(this.cost, o.cost);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        C = Long.parseLong(st.nextToken());

        graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        long maxEdge = 0;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph.get(from).add(new Edge(to, w));
            graph.get(to).add(new Edge(from, w));
            maxEdge = Math.max(maxEdge, w);
        }

        dist = new long[n + 1];

        long left = 0;
        long right = maxEdge;
        long answer = -1;

        // 이분 탐색: "허용할 최대 간선 비용"을 최소화
        while (left <= right) {
            long mid = (left + right) / 2;   // 현재 허용할 최대 간선 비용

            if (dijkstra(mid)) {             // 이 max 간선 비용으로 C 이하로 도달 가능
                answer = mid;
                right = mid - 1;             // 더 줄여보기
            } else {
                left = mid + 1;              // 더 늘려야 도달 가능
            }
        }

        System.out.println(answer);
    }

    // maxEdgeCost 이하의 간선만 사용해서
    // a -> b 최단 비용이 C 이하인지 여부
    static boolean dijkstra(long maxEdgeCost) {
        final long INF = C + 1;              // C 넘으면 의미 없음
        Arrays.fill(dist, INF);

        PriorityQueue<Edge> pq = new PriorityQueue<>();
        dist[a] = 0;
        pq.offer(new Edge(a, 0));

        while (!pq.isEmpty()) {
            Edge cur = pq.poll();
            int v = cur.vertex;
            long costSoFar = cur.cost;

            // 이미 더 좋은 경로 있으면 스킵
            if (costSoFar > dist[v]) continue;
            // 가진 돈 초과 상태도 더 볼 필요 없음
            if (costSoFar > C) continue;

            // 도착 노드에 최소 비용으로 도달
            if (v == b) {
                return true;                 // dist[b] <= C 보장
            }

            for (Edge next : graph.get(v)) {
                // 간선 비용이 maxEdgeCost를 초과하면 이분탐색 조건 위반
                if (next.cost > maxEdgeCost) continue;

                long nextCost = costSoFar + next.cost;
                if (nextCost > C) continue;             // 가진 돈 초과
                if (nextCost >= dist[next.vertex]) continue;

                dist[next.vertex] = nextCost;
                pq.offer(new Edge(next.vertex, nextCost));
            }
        }

        return dist[b] <= C;
    }
}
