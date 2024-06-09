import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {


    static int dx[] = {-1, 0, 1, 0};
    static int dy[] = {0, 1, 0, -1};

    static int graph[][];
    static int n, m;
    static int answer = 0;
    static int visit[][];

    static int canmove = 1;
    static int rx, ry, rdir;

    public static void move() {
        int zx, zy;

        //값이 0인경우 청소되지 않은 빈칸
        //1인 경우 벽이 있음

        if (graph[rx][ry] == 0 && visit[rx][ry] == 0) {
            visit[rx][ry] = 1;
            answer += 1;
        }
        //현재 칸의 주변 4칸중 청소되지 않은 빈칸이 없는지 판단한다
        int rotate_check = 0;
        for (int i = 0; i < 4; i++) {
            zx = dx[i] + rx;
            zy = dy[i] + ry;
            if (0 <= zx && zx < n && 0 <= zy && zy < m && visit[zx][zy] == 0) {
                //청소되지 않는 빈칸이 있는지 파악한다
                if (graph[zx][zy] == 0) {
                    rotate_check = 1;
                    break;
                }
            }
        }

        if (rotate_check == 1) {
            //빈칸이 존재하는 경우
            for (int i = 0; i < 4; i++) {
                rdir -= 1;
                if (rdir == -1)
                    rdir = 3;
                zx = rx + dx[rdir];
                zy = ry + dy[rdir];
                if (0 <= zx && zx < n && 0 <= zy && zy < m && graph[zx][zy] == 0 && visit[zx][zy] == 0) {
                    rx = zx;
                    ry = zy;
                    break;
                }
            }
        } else {
            //빈칸이 존재하지 않는 경우
            int temp_dir = (rdir + 2) % 4;
            zx = rx + dx[temp_dir];
            zy = ry + dy[temp_dir];
            if (0 <= zx && zx < n && 0 <= zy && zy < m) {
                if (graph[zx][zy] == 0) {
                    rx = zx;
                    ry = zy;
                }
                else if(graph[zx][zy]==1)
                    canmove=0;
            }

        }


    }


    public static void main(String[] args) throws IOException {

        //로봇 청소기가 있는데
        //아직 청소되지 않는 경우 현재칸 청소
        //주변 4칸중 청소되지 않은 빈칸이 없는 경우
        //바라보는 방향 유지한채 한칸 후진할수 있다면 후진하고, 1번으로 돌아간다
        //바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동 멈춘다

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(s.nextToken());
        m = Integer.parseInt(s.nextToken());
        graph = new int[n][m];
        visit = new int[n][m];


        //작동 시작한 후 멈출때 까지 청소하는 칸 개수 출력하기
        s = new StringTokenizer(br.readLine(), " ");
        rx = Integer.parseInt(s.nextToken());
        ry = Integer.parseInt(s.nextToken());
        rdir = Integer.parseInt(s.nextToken());
        for (int i = 0; i < n; i++) {
            s = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(s.nextToken());
            }

        }
        while (true) {
            if (canmove == 0)
                break;
            move();
        }
        System.out.println(answer);

    }


}