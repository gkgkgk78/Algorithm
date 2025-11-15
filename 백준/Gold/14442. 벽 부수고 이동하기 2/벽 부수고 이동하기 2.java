

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

    static int[][] graph;
    static int[][][] visit;
    static int n, m, k;

    static class go {
        int x, y, count, dis;

        go(int x, int y, int count, int dis) {
            this.x = x;
            this.y = y;
            this.count = count;
            this.dis = dis;
        }
    }


    public static int bfs(int k) {

        Deque<go> q = new ArrayDeque<>();
        //1이면은 이동할 수 없는 벽이고
        //0이면은 이동 가능한 곳을 나타낸다
        visit[0][0][0] = 1;
        q.add(new go(0, 0, 0, 0));
        int dx[] = {-1, 0, 1, 0};
        int dy[] = {0, -1, 0, 1};
        while (!q.isEmpty()) {
            go a = q.poll();
            if (a.x == n - 1 && a.y == m - 1)
                return a.dis + 1;
            for (int i = 0; i < 4; i++) {
                int zx = dx[i] + a.x;
                int zy = dy[i] + a.y;
                if (0 <= zx && zx < n && 0 <= zy && zy < m) {
                    if (graph[zx][zy] == 1) {
                        //1이면은 이동할 수 없는 벽을 의미한다
                        if (a.count + 1 > k || visit[zx][zy][a.count + 1] <= a.dis + 1)
                            continue;
                        visit[zx][zy][a.count + 1] = a.dis + 1;
                        q.add(new go(zx, zy, a.count + 1, a.dis + 1));
                    } else {
                        if (visit[zx][zy][a.count] <= a.dis + 1)
                            continue;
                        visit[zx][zy][a.count] = a.dis + 1;
                        q.add(new go(zx, zy, a.count, a.dis + 1));
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
        k = Integer.parseInt(st.nextToken());
        graph = new int[n][m];
        visit = new int[n][m][k + 1];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                graph[i][j] = line.charAt(j) - '0';
                for (int l = 0; l <= k; l++) {
                    visit[i][j][l] = Integer.MAX_VALUE;
                }
            }
        }
        int answer = bfs(k);
        System.out.println(answer);


    }


}
