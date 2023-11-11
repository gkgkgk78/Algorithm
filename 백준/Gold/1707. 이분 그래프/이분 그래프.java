import java.util.*;
import java.io.*;


public class Main {


    static List<Integer> list[] ;

    static class go {
        int x, y;

        public go(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void bfs(int x, int visit[]) {
        Queue<go> q = new LinkedList<>();
        visit[x] = 1;
        q.add(new go(x, 1));
        while (q.size() > 0) {
            go a = q.poll();
            List<Integer> now = list[a.x];
            for (int aa : now) {
                if (visit[aa] == 0) {
                    int next = 0;
                    if (a.y == 1)
                        next = 2;
                    else
                        next = 1;
                    visit[aa] = next;
                    q.add(new go(aa, next));

                }
            }
        }

    }

    public static void main(String[] args) throws Exception {

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(in.readLine(), " ");
        int t = Integer.parseInt(s.nextToken());
        List<String>ss=new LinkedList<>();
        for (int i = 0; i < t; i++) {
            s = new StringTokenizer(in.readLine(), " ");
            int v, e;
            v = Integer.parseInt(s.nextToken());
            list = new LinkedList[v+1];
            e = Integer.parseInt(s.nextToken());
            List<go> last = new LinkedList<>();
            for (int j = 0; j <= v; j++)
                list[j]=new LinkedList<>();
            for (int j = 0; j < e; j++) {
                s = new StringTokenizer(in.readLine(), " ");
                int a1, a2;
                a1 = Integer.parseInt(s.nextToken());
                a2 = Integer.parseInt(s.nextToken());
                list[a1].add(a2);
                list[a2].add(a1);
                last.add(new go(a1, a2));
            }
            int visit[] = new int[v + 1];
            for (int j = 1; j <= v; j++) {

                if (visit[j] == 0) {
                    bfs(j, visit);
                }
                //System.out.println(Arrays.toString(visit));
            }
            int answer = 0;
            for (go a : last) {
                if (visit[a.x] == visit[a.y]) {
                    answer = 1;
                    break;
                }
            }
            if (answer == 0)
                ss.add("YES");
                //System.out.println("YES");
            else
                ss.add("NO");
                //System.out.println("NO");


        }
        for (String sa:ss)
            System.out.println(sa);

    }


}