
import java.util.*;
import java.io.*;

//Main 클래스에서 Solution클래스 선언해주기
public class Main {

    static class go {

        int x, y;

        public go(int x, int y) {

            this.x = x;
            this.y = y;
        }

    }

    static char[][] graph;
    static int time;

    public static List<go> bfs(List<go> now, int flag, int n, int m) {

        Queue<go> q = new LinkedList<>();
        int[][] visit = new int[n][m];

        for (go a : now) {
            visit[a.x][a.y] = 1;
            q.add(a);
        }
        List<go> aa = new LinkedList<>();

        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};
        while (q.size() > 0) {
            go a = q.poll();
            for (int i = 0; i < 4; i++) {
                int zx, zy;
                zx = dx[i] + a.x;
                zy = dy[i] + a.y;
                if (0 <= zx && zx < n && 0 <= zy && zy < m) {
                    if ((graph[zx][zy] == '.' || graph[zx][zy] == 'D') && visit[zx][zy] == 0) {
                        if (flag == 1 && graph[zx][zy] == 'D')
                            continue;
                        visit[zx][zy] = 1;
                        if (graph[zx][zy] == 'D') {
                            System.out.println(time);
                            System.exit(0);
                        }
                        if (flag == 1)
                            graph[zx][zy] = '*';
                        else
                            graph[zx][zy] = 'S';
                        aa.add(new go(zx, zy));

                    }
                }
            }
        }
        //System.out.println(day);


        return aa;
    }

    static int count = 0;

    public static void main(String[] ars) throws IOException {

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(in.readLine(), " ");
        //난 최소일수가 궁금해
        int n, m;
        n = Integer.parseInt(s.nextToken());
        m = Integer.parseInt(s.nextToken());
        List<go> now = new LinkedList<>();
        graph = new char[n][m];
        time = 1;
        List<go> water = new LinkedList<>();
        List<go> gosm = new LinkedList<>();
        //이렇게 해서 n,m을 구했음
        for (int i = 0; i < n; i++) {
            char[] t = in.readLine().toCharArray();
            for (int j = 0; j < m; j++) {
                graph[i][j] = (t[j]);
                if (graph[i][j] == 'S') {
                    gosm.add(new go(i, j));
                } else if (graph[i][j] == '*') {
                    water.add(new go(i, j));
                }
            }
        }


        while (true) {

            //물먼저 이동
            //고슴도치 이동
            water = bfs(water, 1, n, m);
            gosm = bfs(gosm, 0, n, m);
            time += 1;
            if (gosm.size() == 0)
                break;
        }
        System.out.println("KAKTUS");

    }
}



