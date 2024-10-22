import java.io.*;
import java.security.cert.CertificateParsingException;
import java.util.*;


public class Main {

    static int[][][] visit;
    static int[][] graph;
    static int max = 100000000;

    static public class go {
        int x, y, count, last;

        public go(int x, int y, int count, int last) {
            this.x = x;
            this.y = y;
            this.count = count;
            this.last = last;
        }
    }

    public static int bfs(int n, int m) {
        PriorityQueue<go> q = new PriorityQueue<>((x, y) -> {
            return x.last - y.last;
        });
        int dx[] = {-1, 0, 1, 0};
        int dy[] = {0, -1, 0, 1};

        visit[0][0][0] = 1;
        visit[0][0][1] = 1;
        q.add(new go(0, 0, 0, 1));
        while (!q.isEmpty()) {
            go a = q.poll();
            if (a.x == n - 1 && a.y == m - 1)
                return a.last;
            for (int i = 0; i < 4; i++) {
                int zx = dx[i] + a.x;
                int zy = dy[i] + a.y;
                if (0 <= zx && zx < n && 0 <= zy && zy < m) {
                    if (graph[zx][zy] == 0) {
                        if (visit[a.x][a.y][a.count] + 1 < visit[zx][zy][a.count]) {
                            visit[zx][zy][a.count] = visit[a.x][a.y][a.count] + 1;
                            q.add(new go(zx, zy, a.count, a.last + 1));
                        }
                    } else {
                        if (a.count == 1)
                            continue;
                        if (visit[a.x][a.y][a.count] + 1 < visit[zx][zy][a.count + 1]) {
                            visit[zx][zy][a.count + 1] = visit[a.x][a.y][a.count] + 1;
                            q.add(new go(zx, zy, a.count + 1, a.last + 1));
                        }
                    }
                }
            }
        }
        return -1;


    }


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        int n, m;
        n = Integer.parseInt(s.nextToken());
        m = Integer.parseInt(s.nextToken());
        //나는 최단 경로로 이동하려고 한다
        //이동하는 도중 한개의 벽 부수고 이동하는게 더 짧아 지면 한개까지 부수고 가도 된다
        //벽이 있을경우에는 그거를 부수냐 안부수냐 겠네
        visit = new int[n][m][2];
        graph = new int[n][m];
        for (int i = 0; i < n; i++) {
            String temp = br.readLine();
            for (int j = 0; j < m; j++) {
                graph[i][j] = temp.charAt(j) - '0';
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                for (int k = 0; k < 2; k++) {
                    visit[i][j][k] = max;
                }
            }
        }
        int answer = bfs(n, m);

        System.out.println(answer);


    }
}