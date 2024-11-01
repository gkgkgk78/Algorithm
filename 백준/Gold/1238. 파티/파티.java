import javax.print.ServiceUIFactory;
import java.io.*;
import java.util.*;

public class Main {

    //n명의 학생이 x마을에 모여서 파티를 벌이기로 했다

    public static class go {
        int end, value;

        public go(int end, int value) {
            this.end = end;
            this.value = value;
        }
    }

    public static int dijk(int n, ArrayList<go> list[], int start, int last) {

        int visit[] = new int[n];
        for (int i = 0; i < n; i++) {
            visit[i] = Integer.MAX_VALUE;
        }
        visit[start] = 0;
        PriorityQueue<go> q = new PriorityQueue<>((x, y) -> {
            return x.value - y.value;
        });
        q.add(new go(start, 0));

        while (!q.isEmpty()) {
            go a = q.poll();
            if (a.value > visit[a.end])
                continue;
            for (go vertex : list[a.end]) {
                int now = vertex.value + a.value;
                if (visit[vertex.end] > now) {
                    visit[vertex.end] = now;
                    q.add(new go(vertex.end, now));
                }
            }
        }
        return visit[last];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        //이 마을 사이에는 총 m개의 단방향 도로들이 있고

        int n, m, x;
        n = Integer.parseInt(s.nextToken());
        m = Integer.parseInt(s.nextToken());
        x = Integer.parseInt(s.nextToken());
        x -= 1;

        ArrayList<go> list[] = new ArrayList[n];

        for (int i = 0; i < n; i++) {
            list[i] = new ArrayList<>();
        }
        for (int i = 0; i < m; i++) {
            s = new StringTokenizer(br.readLine(), " ");
            int a1, a2, a3;
            a1 = Integer.parseInt(s.nextToken());
            a2 = Integer.parseInt(s.nextToken());
            a3 = Integer.parseInt(s.nextToken());
            a1 -= 1;
            a2 -= 1;
            list[a1].add(new go(a2, a3));
//            list[a2].add(new go(a1, a3));
        }
        int visit[] = new int[n];
        int answer = -1;
        for (int i = 0; i < n; i++) {
            int go = dijk(n, list, i, x);
            int back = dijk(n, list, x, i);
            visit[i] = go + back;
            answer = Math.max(answer, visit[i]);
        }
        System.out.println(answer);

    }

}