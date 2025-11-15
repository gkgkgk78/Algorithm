

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {


    static int n, m;
    static int[][] graph;
    static int[][] add;
    static int h, w, sr, sc, fr, fc;


    static class go {
        int x, y;

        go(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int check(int zx, int zy) {
        if (1 <= zx && zx <= n && 1 <= zy && zy <= m)
            return 1;
        return -1;
    }

    public static int bfs() {

        Deque<go> q = new ArrayDeque<>();
        int[][] visit = new int[n + 2][m + 2];
        visit[sr][sc] = 1;
        int dx[] = {-1, 0, 1, 0};
        int dy[] = {0, -1, 0, 1};
        q.add(new go(sr, sc));

        while (!q.isEmpty()) {
            go a = q.poll();
            if (a.x == fr && a.y == fc) {
                return visit[fr][fc] - 1;
            }
            for (int i = 0; i < 4; i++) {
                int zx = dx[i] + a.x;
                int zy = dy[i] + a.y;
                int tx = zx + h - 1;
                int ty = zy + w - 1;
                if (check(zx, zy) == 1) {
                    if (visit[zx][zy] !=0 || check(tx, ty) != 1)
                        continue;
                    //이제 벽이 있는지 확인해 봐야함
                    int temp = 0;
                    for (int i1 = zx; i1 < zx + h; i1++) {
                        temp += add[i1][ty] - add[i1][zy - 1];
                        if (temp > 0)
                            break;
                    }
                    if (temp == 0) {
                        visit[zx][zy] += visit[a.x][a.y] + 1;
                        q.add(new go(zx, zy));
                    }
                }
            }
        }


        return -1;

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n + 2][m + 2];
        add = new int[n + 2][m + 2];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 1; j <= m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                add[i][j] = graph[i][j];
            }
            for (int j = 2; j <= m; j++) {
                add[i][j] += add[i][j - 1];
            }
        }
        st = new StringTokenizer(br.readLine(), " ");
        h = Integer.parseInt(st.nextToken());
        w = Integer.parseInt(st.nextToken());
        sr = Integer.parseInt(st.nextToken());
        sc = Integer.parseInt(st.nextToken());
        fr = Integer.parseInt(st.nextToken());
        fc = Integer.parseInt(st.nextToken());

        System.out.println(bfs());

    }


}
