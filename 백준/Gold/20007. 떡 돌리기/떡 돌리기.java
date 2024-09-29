import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {

    public static LinkedList<go1>[] list;

    public static class go {
        int from, value;

        public go(int x, int y) {
            this.from = x;
            this.value = y;
        }

    }

    public static class go1 {
        int to, val;

        public go1(int x, int y) {
            this.to = x;
            this.val = y;
        }

    }

    public static void dijk(Integer visit[],int start) {
        PriorityQueue<go> q = new PriorityQueue<>((x, y) -> {
            return x.value - y.value;
        });
        q.add(new go(start, 0));
        while (!q.isEmpty()) {
            go now = q.poll();
            if (now.value > visit[now.from]) {
                continue;
            }
            for (go1 g : list[now.from]) {
                int temp = now.value + g.val;
                if (visit[g.to] > temp) {
                    visit[g.to] = temp;
                    q.add(new go(g.to, temp));
                }
            }
        }

    }

    public static void main(String[] args) throws IOException {


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        int n, m, x1, y;
        n = Integer.parseInt(s.nextToken());
        m = Integer.parseInt(s.nextToken());
        x1 = Integer.parseInt(s.nextToken());
        y = Integer.parseInt(s.nextToken());
        Integer[] visit = new Integer[n];
        for (int i = 0; i < n; i++) {
            visit[i] = 10000001;
        }

        visit[y] = 0;
        list = new LinkedList[n];
        for(int i=0;i<n;i++){
            list[i]=new LinkedList<>();
        }
        for (int i = 0; i < m; i++) {
            s = new StringTokenizer(br.readLine(), " ");
            int a1, a2, a3;
            a1 = Integer.parseInt(s.nextToken());
            a2 = Integer.parseInt(s.nextToken());
            a3 = Integer.parseInt(s.nextToken());
            list[a1].add(new go1(a2, a3));
            list[a2].add(new go1(a1, a3));
        }
        dijk(visit,y);
        List<Integer> list1 = Arrays.asList(visit);
        list1.sort((x, y1) -> {
            return x - y1;
        });
        int day = 1;
        int sum = 0;
        for (Integer s1 : list1) {
            if (s1*2 > x1) {
                day = -1;
                break;
            } else {
                sum += s1 * 2;
                if (sum > x1) {
                    day += 1;
                    sum = s1 * 2;
                }
            }
        }

        System.out.println(day);


    }
}