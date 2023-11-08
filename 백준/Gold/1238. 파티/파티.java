import java.util.*;
import java.io.*;

class Node {


    int vertex;
    int value;

    public Node(int vertex, int value) {
        this.value = value;
        this.vertex = vertex;
    }
}


public class Main {

    static List<List<Node>> list;
 

    public static void main(String[] args) throws Exception {

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s;

        int n, m, x;
        s = new StringTokenizer(in.readLine(), " ");
        n = Integer.parseInt(s.nextToken());
        m = Integer.parseInt(s.nextToken());
        x = Integer.parseInt(s.nextToken());
        list = new LinkedList<>();

        for (int i = 0; i <= n; i++) {
            list.add(new LinkedList<>());

        }

        for (int i = 0; i < m; i++) {
            s = new StringTokenizer(in.readLine(), " ");
            int a1, a2, a3;
            a1 = Integer.parseInt(s.nextToken());
            a2 = Integer.parseInt(s.nextToken());
            a3 = Integer.parseInt(s.nextToken());
            list.get(a1).add(new Node(a2, a3));


        }
        int answer = -1;
        //우선 역으로 해서 돌아 오는 것부터 구해 보도록 하자
        int[] reverse = dijk(x, list, n);
        for (int i = 1; i <= n; i++) {
            int[] now = dijk(i, list, n);
            answer = Math.max(answer, now[x] + reverse[i]);
        }
        System.out.println(answer);

    }

    public static int[] dijk(int start, List<List<Node>> li, int n) {
        int[] distance = new int[n + 1];
        PriorityQueue<Node> q = new PriorityQueue<>((x, y) -> {
            return x.value - y.value;
        });
        for (int i = 0; i <= n; i++) {
            distance[i] = 9999999;
        }
        distance[start] = 0;
        q.add(new Node(start, 0));
        while (q.size() > 0) {
            Node a1 = q.poll();
            if (distance[a1.vertex] < a1.value)
                continue;
            List<Node> now = li.get(a1.vertex);
            for (Node a : now) {
                int temp = a.value + a1.value;
                if (distance[a.vertex] > temp) {
                    distance[a.vertex] = temp;
                    q.add(new Node(a.vertex, temp));
                }
            }
        }


        return distance;
    }


}