import java.awt.*;
import java.io.*;
import java.security.cert.CertificateParsingException;
import java.util.*;


public class Main {

    static int n, m;

    public static class go {
        int x, y, delete;

        public go(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public go(int x, int y, int delete) {
            this.x = x;
            this.y = y;
            this.delete = delete;
        }
    }

    public static void bfs(int[][] graph, int sx, int sy,int visit[][]) {
        Deque<go> q = new ArrayDeque<>();
        visit[sx][sy] = 1;
        q.add(new go(sx, sy));
        int dx[] = {-1, 0, 1, 0};
        int dy[] = {0, -1, 0, 1};

        while (!q.isEmpty()) {
            go a = q.poll();
            for (int i = 0; i < 4; i++) {
                int zx = dx[i] + a.x;
                int zy = dy[i] + a.y;
                if (0 <= zx && zx < n && 0 <= zy && zy < m) {
                    if (visit[zx][zy] == 0 && graph[zx][zy] != 0) {
                        visit[zx][zy] = 1;
                        q.add(new go(zx, zy));
                    }
                }
            }
        }

    }


    public static int check(int[][] graph) {
        //두덩어리 이상으로 분리된 빙하가 있는지 파악하기
        int visit[][] = new int[n][m];
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 0)
                    continue;
                if (visit[i][j] == 1)
                    continue;
                bfs(graph, i, j,visit);
                count += 1;
            }
        }
        return count;
    }

    public static int check_last(int[][] graph) {
        //두덩어리 이상으로 분리된 빙하가 있는지 파악하기
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] != 0)
                    count += 1;
            }
        }
        return count;
    }


    public static int game(int[][] graph) {
        int time = 0;
        // 빙산이 다 분리 되는 최초의 시간 구하기
        int dx[] = {-1, 0, 1, 0};
        int dy[] = {0, -1, 0, 1};
        while (true) {
            // 게임 돌면서 한 빙하 몇개 제거 되어야 하는지 구해야 함
            Deque<go> q = new ArrayDeque<>();
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (graph[i][j] == 0)
                        continue;
                    int check1 = 0;
                    for (int i1 = 0; i1 < 4; i1++) {
                        int zx = dx[i1] + i;
                        int zy = dy[i1] + j;
                        if (0 <= zx && zx < n && 0 <= zy && zy < m) {
                            if (graph[zx][zy] == 0)
                                check1 += 1;
                        }
                    }
                    q.add(new go(i, j, check1));
                }
            }

            //빙하 개수 줄이기
            while (!q.isEmpty()) {
                go a = q.poll();
                graph[a.x][a.y] -= a.delete;
                if (graph[a.x][a.y] < 0)
                    graph[a.x][a.y] = 0;
            }
            //빙산 분리 되는거 개수 세기
            time += 1;
            int check1 = check(graph);
            if (check1 >= 2)
                return time;
            int checkLast = check_last(graph);
            if (checkLast == 0)
                return 0;
        }

    }


    public static void main(String[] args) throws IOException {


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(s.nextToken());
        m = Integer.parseInt(s.nextToken());
        int[][] graph = new int[n][m];
        for (int i = 0; i < n; i++) {
            s = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(s.nextToken());
            }
        }


        System.out.println(game(graph));


    }
}