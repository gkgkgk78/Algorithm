

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.SQLOutput;
import java.util.*;

public class Main {

    static int n, m, k;
    static int graph[][];
    static boolean[][][] visit;

    static class go {
        int x, y, count, dis;

        go(int x, int y, int count, int dis) {
            this.x = x;
            this.y = y;
            this.count = count;
            this.dis = dis;
        }
    }

    static int bfs() {

        int[] tx = {-2, -2, -1, -1, 1, 1, 2, 2};
        int[] ty = {-1, 1, -2, 2, -2, 2, -1, 1};
        int dx[] = {-1, 0, 1, 0};
        int dy[] = {0, -1, 0, 1};
        visit[0][0][0] = true;
        Deque<go> q = new ArrayDeque<>();
        q.add(new go(0, 0, 0, 1));
        while (!q.isEmpty()) {
            go now = q.poll();
            if (now.x == n - 1 && now.y == m - 1) {
                return now.dis - 1;
            }
            if (now.count + 1 <= k) {
                for (int i = 0; i < tx.length; i++) {
                    int nx = now.x + tx[i];
                    int ny = now.y + ty[i];
                    if (0 <= nx && nx < n && 0 <= ny && ny < m && graph[nx][ny] == 0) {
                        if (!visit[nx][ny][now.count + 1]) {
                            visit[nx][ny][now.count + 1] = true;
                            q.add(new go(nx, ny, now.count + 1, now.dis + 1));
                        }
                    }
                }
            }
            for (int i = 0; i < dx.length; i++) {
                int zx = now.x + dx[i];
                int zy = now.y + dy[i];
                if (zx >= 0 && zx < n && zy >= 0 && zy < m) {
                    if (graph[zx][zy] == 0) {
                        if (!visit[zx][zy][now.count]) {
                            visit[zx][zy][now.count] = true;
                            q.add(new go(zx, zy, now.count, now.dis + 1));
                        }
                    }
                }

            }


        }
        return -1;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        k = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine(), " ");
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        graph = new int[n][m];
        visit = new boolean[n][m][k + 1];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        System.out.println(bfs());


    }

}
