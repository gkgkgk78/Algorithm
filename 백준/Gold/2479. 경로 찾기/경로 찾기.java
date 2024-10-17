import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.AnnotatedWildcardType;
import java.sql.SQLOutput;
import java.util.*;
import java.util.concurrent.locks.ReentrantReadWriteLock;


public class Main {

    static int start, finish;
    static String answer="";

    public static class go {
        int vertex;
        String now;
        String last;

        go(int v, String last, String now) {
            this.vertex = v;
            this.last = last;
            this.now = now;
        }
    }

    public static int check(String s1, String s2) {

        int count = 0;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i))
                count += 1;
        }
        if (count == 1)
            return 1;
        return 0;
    }

    public static void bfs(int start, int finish, int n, String[] data) {
        int[] visit = new int[n];
        visit[start] = 1;
        Deque<go> q = new ArrayDeque<>();

        q.add(new go(start, Integer.toString(start+1)+" ", data[start]));

        while (!q.isEmpty()) {
            go a = q.poll();
            if (a.vertex == finish) {
                answer = a.last;
                return;
            }
            for (int i = 0; i < n; i++) {
                if (visit[i] == 1)
                    continue;
                int check = check(a.now, data[i]);
                if (check == 1) {
                    visit[i] = 1;
                    q.add(new go(i, a.last + Integer.toString(i+1)+" ", data[i]));
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        int n, m;
        n = Integer.parseInt(s.nextToken());
        m = Integer.parseInt(s.nextToken());
        String[] temp = new String[n];
        for (int i = 0; i < n; i++) {
            s = new StringTokenizer(br.readLine(), " ");
            temp[i] = s.nextToken();
        }
        s = new StringTokenizer(br.readLine(), " ");
        start = Integer.parseInt(s.nextToken());
        finish = Integer.parseInt(s.nextToken());
        bfs(start-1, finish-1, n, temp);
        if (answer.length() == 0)
            System.out.println(-1);
        else {

            System.out.println(answer);
        }


    }
}