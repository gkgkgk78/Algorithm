import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;
import java.util.*;

public class Main {

    static int n, m;
    static int shark_x, shark_y, shark_size;
    static int graph[][];
    static int time = 0;
    static int shark_temp = 0;

    public static class fish {
        int x, y, dir;

        public fish(int x, int y, int dir) {
            this.x = x;
            this.y = y;
            this.dir = dir;
        }
    }

    public static class go {
        int x, y;

        public go(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }


    public static int[][] move() {

        //이제 상어의 입장에서 물고기에 도달할수 있는지 확인해보자
        int visit[][] = new int[n][n];
        visit[shark_x][shark_y] = 1;
        Queue<go> q = new LinkedList<>();
        int dx[] = {-1, 0, 1, 0};
        int dy[] = {0, 1, 0, -1};
        q.add(new go(shark_x, shark_y));
        while (!q.isEmpty()) {
            go a = q.poll();

            for (int i = 0; i < 4; i++) {
                int zx = dx[i] + a.x;
                int zy = dy[i] + a.y;
                if (0 <= zx && zx < n && 0 <= zy && zy < n) {
                    if (visit[zx][zy] == 0 && graph[zx][zy] <= shark_size) {
                        visit[zx][zy] = visit[a.x][a.y] + 1;
                        q.add(new go(zx, zy));
                    }
                }
            }
        }
        return visit;
    }


    public static int find() {
        //이제 물고기 찾아야 함
        //자신의 크기보다 작거나 같은 물고기 리스트들 확인하기
        List<fish> fishes = new LinkedList();
        int visit[][] = move();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == shark_x && j == shark_y)
                    continue;
                //찾아보자
                if (graph[i][j] != 0 && graph[i][j] < shark_size && visit[i][j] != 0) {
                    fishes.add(new fish(i, j, visit[i][j]));
                }
            }
        }
        //이제 정렬 하자
        fishes.sort((x, y) -> {
            if (x.dir != y.dir)
                return x.dir - y.dir;
            else if (x.x != y.x)
                return x.x - y.x;
            else
                return x.y - y.y;
        });
        if (fishes.size() == 0)
            return 0;
        //이제 찾은거 하나로 해서 이동하면 될듯하다
        fish first = fishes.get(0);
        time += first.dir - 1;
        shark_x = first.x;
        shark_y = first.y;
        shark_temp += 1;
        if (shark_temp == shark_size) {
            shark_temp = 0;
            shark_size += 1;
        }
        graph[first.x][first.y] = 0;
        return 1;
    }


    public static void main(String[] args) throws IOException {


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(s.nextToken());
        //n*m공간에 물고기 m마리와 아기상어 1마리가 존재 한다
        //한 칸에는 물고기가 최대 1마리 존재 한다
        shark_size = 2;
        graph = new int[n][n];
        for (int i = 0; i < n; i++) {
            s = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(s.nextToken());
                if (graph[i][j] == 9) {
                    shark_x = i;
                    shark_y = j;
                    graph[i][j] = 0;
                }
            }
        }
        while (true) {
            int check = find();
            if (check == 0)
                break;
        }
        System.out.println(time);


    }
}