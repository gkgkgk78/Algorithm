import java.util.*;
import java.io.*;

//Main 클래스에서 Solution클래스 선언해주기
public class Main {

    static class go {
        int x, y, dir, count;

        public go(int x, int y, int dir, int count) {
            this.x = x;
            this.y = y;
            this.dir = dir;
            this.count = count;
        }
    }

    public static void bfs(int sx, int sy, int sdir, int fx, int fy, int fdir) {
        Queue<go> q = new LinkedList<>();
        q.add(new go(sx, sy, sdir, 0));
        visit[sx][sy][sdir] = 1;
        int dx[] = {-1, 0, 1, 0};
        int dy[] = {0, 1, 0, -1};
        while (q.size() > 0) {
            go t = q.poll();
            //System.out.println(t.x+" "+t.y+" "+t.dir+" "+t.count);
            if (t.x == fx && t.y == fy && t.dir == fdir) {
                System.out.println(t.count);
                System.exit(0);
            }
            //우선 해당 방향으로 3번 까지 이동 해보도록 하자
            int zx, zy;
            zx = t.x;
            zy = t.y;
            for (int i = 1; i < 4; i++) {
                zx += dx[t.dir];
                zy += dy[t.dir];
                if (0 <= zx && zx < n && 0 <= zy && zy < m &&graph[zx][zy]==0) {
                    if (visit[zx][zy][t.dir] == 0) {
                        visit[zx][zy][t.dir] = 1;
                        q.add(new go(zx, zy, t.dir, t.count + 1));
                    }
                } else
                    break;
            }
            //이제 방향 변경해서 해보도록 하자
            int temp = -1;
            temp = t.dir;
            temp -= 1;
            if (temp == -1)
                temp = 3;
            if (visit[t.x][t.y][temp] == 0) {
                visit[t.x][t.y][temp] = 1;
                q.add(new go(t.x, t.y, temp, t.count + 1));
            }
            temp = t.dir;
            temp += 1;
            if (temp == 4)
                temp = 0;
            if (visit[t.x][t.y][temp] == 0) {
                visit[t.x][t.y][temp] = 1;
                q.add(new go(t.x, t.y, temp, t.count + 1));
            }


        }


    }

    public static int check(int x) {
        if (x == 4) {
            return 0;
        } else if (x == 1) {
            return 1;
        } else if (x == 3) {
            return 2;
        } else
            return 3;
    }


    static int n, m;
    static int graph[][];
    static int visit[][][];

    public static void main(String[] ars) throws IOException {

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(in.readLine(), " ");
        n = Integer.parseInt(s.nextToken());
        m = Integer.parseInt(s.nextToken());
        int sx, sy, sdir;
        int fx, fy, fdir;
        graph = new int[n][m];
        visit = new int[n][m][4];
        for (int i = 0; i < n; i++) {
            s = new StringTokenizer(in.readLine(), " ");
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(s.nextToken());
            }
        }
        s = new StringTokenizer(in.readLine(), " ");
        sx = Integer.parseInt(s.nextToken());
        sy = Integer.parseInt(s.nextToken());
        sdir = Integer.parseInt(s.nextToken());
        s = new StringTokenizer(in.readLine(), " ");
        fx = Integer.parseInt(s.nextToken());
        fy = Integer.parseInt(s.nextToken());
        fdir = Integer.parseInt(s.nextToken());
        sdir = check(sdir);
        fdir = check(fdir);
        sx -= 1;
        sy -= 1;
        fx -= 1;
        fy -= 1;
        bfs(sx, sy, sdir, fx, fy, fdir);

    }
}

