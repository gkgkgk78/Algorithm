import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {

    static int n, m;

    public static class go {
        int x, y;

        public go(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int answer = 0;

    public static void bfs(int x, int y, int[][] graph, int[][] visit) {


        Deque<go> q = new LinkedList<>();
        List<go>list =new LinkedList<>();

        int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dy = {-1, 0, 1, -1, 1, -1, 0, 1};
        q.add(new go(x, y));
        list.add(new go(x,y));
        int count=0;
        visit[x][y]=1;
        boolean flag=true;
        while (!q.isEmpty()) {
            go a = q.poll();
            for (int i = 0; i < dx.length; i++) {
                int zx = dx[i] + a.x;
                int zy = dy[i] + a.y;
                if (0 <= zx && zx < n && 0 <= zy && zy < m) {

                    if (graph[zx][zy] == graph[a.x][a.y]&&visit[zx][zy]==0) {
                        visit[zx][zy] = 1;
                        q.addFirst(new go(zx, zy));
                        list.add(new go(zx,zy));
                    } else if (graph[zx][zy] > graph[a.x][a.y])
                        flag=false;
                }
            }
        }
        if(!flag)
            return;
        answer += 1;


    }


    public static void main(String[] args) throws IOException {


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(s.nextToken());
        m = Integer.parseInt(s.nextToken());
        int graph[][] = new int[n][m];
        for (int i = 0; i < n; i++) {
            s = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(s.nextToken());
            }
        }
        int[][] visit = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (visit[i][j] == 1)
                    continue;
                bfs(i, j, graph, visit);
            }
        }
        System.out.println(answer);

    }
}