import java.io.*;
import java.util.*;

public class Main {

    public static class go {
        int vertex, value;

        public go(int vertex, int value) {
            this.vertex = vertex;
            this.value = value;
        }
    }

    public static class go1 {
        int vertex1, vertex2;

        public go1(int vertex, int vertex2) {
            this.vertex2 = vertex2;
            this.vertex1 = vertex;
        }
    }

    public static int dijk_first(int start, int last, int n, ArrayList<go> list[], int[] path) {
        int visit[] = new int[n];
        for (int i = 0; i < n; i++)
            visit[i] = Integer.MAX_VALUE;
        visit[start] = 0;
        PriorityQueue<go> q = new PriorityQueue<>((x, y) -> {
            return x.value - y.value;
        });
        q.add(new go(start, 0));
        while (!q.isEmpty()) {
            go a = q.poll();
            if (a.value > visit[a.vertex])
                continue;
            for (go a1 : list[a.vertex]) {
                int now = a1.value + a.value;
                if (visit[a1.vertex] > now) {
                    visit[a1.vertex] = now;
                    q.add(new go(a1.vertex, now));
                    path[a1.vertex] = a.vertex;
                }
            }
        }
        //이제 끝부터 해서 돌아가면 될듯 하다
        return visit[last];
    }

    public static int dijk(int start, int last, int n, ArrayList<go> list[], int check1, int check2) {
        int visit[] = new int[n];
        for (int i = 0; i < n; i++)
            visit[i] = Integer.MAX_VALUE;
        visit[start] = 0;
        PriorityQueue<go> q = new PriorityQueue<>((x, y) -> {
            return x.value - y.value;
        });
        q.add(new go(start, 0));
        while (!q.isEmpty()) {
            go a = q.poll();
            if (a.value > visit[a.vertex])
                continue;
            for (go a1 : list[a.vertex]) {
                int now = a1.value + a.value;
                if (visit[a1.vertex] > now) {
                    if (a1.vertex == check1 && a.vertex == check2)
                        continue;
                    if (a1.vertex == check2 && a.vertex == check1)
                        continue;
                    visit[a1.vertex] = now;
                    q.add(new go(a1.vertex, now));
                }
            }
        }
        return visit[last];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        int n, m;
        n = Integer.parseInt(s.nextToken());
        m = Integer.parseInt(s.nextToken());
        ArrayList<go> list[] = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            list[i] = new ArrayList<>();
        }
        List<Integer> check = new LinkedList<>();
        for (int i = 0; i < m; i++) {
            s = new StringTokenizer(br.readLine(), " ");
            int a1, a2, a3;
            a1 = Integer.parseInt(s.nextToken());
            a2 = Integer.parseInt(s.nextToken());
            a3 = Integer.parseInt(s.nextToken());
            a1 -= 1;
            a2 -= 1;
            list[a1].add(new go(a2, a3));
            list[a2].add(new go(a1, a3));
        }
        //경찰이 도로를 막음으로써 지연시킬수 있는 최대 시간을 정수로 출력하자

        int path[] = new int[n];
        int first = dijk_first(0, n - 1, n, list, path);
        check.add(n-1);
        int index=n-1;
        while (true) {
            int now = path[index];
            index=now;
            check.add(now);
            if (now == 0)
                break;
        }
        int last[] = new int[check.size()];
        for (int i = 0; i < check.size(); i++) {
            last[i] = check.get(i);
        }

        if (first == Integer.MAX_VALUE)
            System.out.println(-1);
        else {
            int answer = -2;
            for (int i = 0; i < last.length-1; i++) {
                int a1 = last[i];
                int a2 = last[i + 1];
                int now = dijk(0, n - 1, n, list, a1, a2);
                if (now == Integer.MAX_VALUE) {
                    answer = -1;
                    break;
                }
                answer = Math.max(answer, now - first);

            }
            if (answer == -2)
                System.out.println(0);
            else
                System.out.println(answer);


        }

    }

}