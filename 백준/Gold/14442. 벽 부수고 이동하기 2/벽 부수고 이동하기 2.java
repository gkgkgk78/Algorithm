import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.SQLOutput;
import java.util.*;

public class Main {

    static int n, m,k;
    static int graph[][];
    static int[][][] visit;


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
        PriorityQueue<go> q = new PriorityQueue<>((x, y) -> {
            return x.dis - y.dis;
        });

        visit[0][0][0]=1;
        q.add(new go(0, 0, 0, 1));
        int dx[] = {-1, 0, 1, 0};
        int dy[] = {0, -1, 0, 1};

        while (!q.isEmpty()) {
            go now = q.poll();
            if(now.x==n-1&&now.y==m-1)
                return now.dis;
            for (int i = 0; i < 4; i++) {
                int zx = dx[i] + now.x;
                int zy = dy[i] + now.y;
                if (0 <= zx && zx < n && 0 <= zy && zy < m) {
                    if(graph[zx][zy]==0&&visit[zx][zy][now.count]>now.dis+1){
                        visit[zx][zy][now.count]=now.dis+1;
                        q.add(new go(zx,zy,now.count,now.dis+1));
                    }
                    else{
                        if(now.count+1<=k&&visit[zx][zy][now.count+1]>now.dis+1){
                            visit[zx][zy][now.count+1]=now.dis+1;
                            q.add(new go(zx,zy,now.count+1,now.dis+1));
                        }
                    }
                }
            }

        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        graph=new int[n][m];
        visit= new int[n][m][k+1];
        for (int i = 0; i < n; i++) {
            String line = br.readLine().trim();
            for (int j = 0; j < m; j++) {
                graph[i][j] = line.charAt(j) - '0';
                for (int k1 = 0; k1 <= k; k1++) {
                    visit[i][j][k1] = 9999999;
                }
            }
        }
        System.out.println(bfs());

    }

}
