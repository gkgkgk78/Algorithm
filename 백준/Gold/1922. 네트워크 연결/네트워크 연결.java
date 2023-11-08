import java.util.*;
import java.io.*;

class Node {


    int vertex1;
    int vertex2;
    int value;

    public Node(int vertex1, int vertex2, int value) {
        this.value = value;
        this.vertex1 = vertex1;
        this.vertex2 = vertex2;
    }
}


public class Main {

    static int[] parents;

    public static void make(int n) {
        for (int i = 1; i <= n; i++) {
            parents[i] = i;
        }
    }

    public static int find(int x) {
        if (parents[x] == x)
            return x;
        parents[x] = find(parents[x]);
        return parents[x];
    }

    public static void union(int a1, int a2) {
        int a = find(a1);
        int b = find(a2);
        if (a < b)
            parents[b] = a;
        else
            parents[a] = b;
    }


    public static void main(String[] args) throws Exception {

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s;

        int n, m;
        s = new StringTokenizer(in.readLine(), " ");
        n = Integer.parseInt(s.nextToken());
        parents = new int[n + 1];
        s = new StringTokenizer(in.readLine(), " ");
        m = Integer.parseInt(s.nextToken());
        PriorityQueue<Node> q = new PriorityQueue<>((x, y) -> {
            return x.value - y.value;
        });
        make(n);
        for (int i = 0; i < m; i++) {
            int a1, a2, a3;
            s = new StringTokenizer(in.readLine(), " ");
            a1 = Integer.parseInt(s.nextToken());
            a2 = Integer.parseInt(s.nextToken());
            a3 = Integer.parseInt(s.nextToken());
            q.add(new Node(a1, a2, a3));
        }
        int answer = 0;
        while (q.size() > 0) {
            Node aa = q.poll();
            int a1 = find(aa.vertex1);
            int a2 = find(aa.vertex2);
            if (a1 != a2) {
                union(a1, a2);
                answer += aa.value;
            }
        }

        System.out.println(answer);
    }


}