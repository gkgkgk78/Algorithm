import java.io.*;
import java.util.*;

//https://www.acmicpc.net/problem/11967
public class Main {

    public static class vertex {
        int x, y;

        public vertex(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static class go {
        List<vertex> list = new ArrayList<>();

        public go(List<vertex> list) {
            this.list = list;
        }
    }

    static int answer = 0;

    public static void bfs(go[][] array, int n, int m) {
        int visit[][] = new int[n][m];
        int light[][] = new int[n][m];
        Deque<vertex> q = new ArrayDeque<>();
        visit[0][0] = 1;
        light[0][0]=1;
        q.add(new vertex(0, 0));
        int dx[] = {-1, 0, 1, 0};
        int dy[] = {0, -1, 0, 1};
        answer += 1;
        while (!q.isEmpty()) {
            vertex a = q.poll();
            for (vertex a1 : array[a.x][a.y].list) {
                if (light[a1.x][a1.y] == 0) {
                    light[a1.x][a1.y] = 1;
                    answer+=1;
                    for (int i = 0; i < 4; i++) {
                        int zx = dx[i] + a1.x;
                        int zy = dy[i] + a1.y;
                        if (0 <= zx && zx < n && 0 <= zy && zy < m) {
                            if (light[zx][zy] == 1 && visit[zx][zy] == 1) {
                                q.add(new vertex(zx, zy));
                            }
                        }
                    }
                }
            }
            for (int i = 0; i < 4; i++) {
                int zx = dx[i] + a.x;
                int zy = dy[i] + a.y;
                if (0 <= zx && zx < n && 0 <= zy && zy < m) {
                    if (light[zx][zy] == 1 && visit[zx][zy] == 0) {
                        visit[zx][zy] = 1;
                        q.add(new vertex(zx, zy));
                    }
                }
            }
        }
        visit[0][0] = 1;

    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        int n, m;
        n = Integer.parseInt(s.nextToken());
        m = Integer.parseInt(s.nextToken());
        go[][] array = new go[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                array[i][j] = new go(new ArrayList<>());
            }
        }
        for (int i = 0; i < m; i++) {
            s = new StringTokenizer(br.readLine(), " ");
            int a1, a2, a3, a4;
            a1 = Integer.parseInt(s.nextToken());
            a2 = Integer.parseInt(s.nextToken());
            a3 = Integer.parseInt(s.nextToken());
            a4 = Integer.parseInt(s.nextToken());
            go now = array[a1 - 1][a2 - 1];
            now.list.add(new vertex(a3 - 1, a4 - 1));
        }
        bfs(array, n, m);
        System.out.println(answer);


    }

}