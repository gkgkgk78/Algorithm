

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {


    static int n, m;
    static int graph[][];
    static int dir[][];
    static int answer = -1;

    static void calc() {

        //이제 계산을 해보도록 하자
        //가로
        int cal = 0;
        for (int i = 0; i < n; i++) {
            int temp = 0;
            for (int j = 0; j < m; j++) {
                if (dir[i][j] == 0) {
                    temp = (temp * 10 + graph[i][j]);
                } else {
                    cal += temp;
                    temp = 0;
                }
            }
            cal += temp;
        }

        //세로
        for (int j = 0; j < m; j++) {
            int temp = 0;
            for (int i = 0; i < n; i++) {
                if (dir[i][j] == 1) {
                    temp = temp * 10 + graph[i][j];
                } else {
                    cal += temp;
                    temp = 0;
                }
            }
            cal += temp;
        }
        answer = Math.max(answer, cal);

    }


    static void dfs(int x, int y) {

        if (x == n - 1 && y == m) {
            calc();
            return;
        }
        if (y == m) {
            x += 1;
            y = 0;
        }
        dir[x][y] = 0;
        dfs(x, y + 1);

        dir[x][y] = 1;
        dfs(x, y + 1);

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n][m];
        dir = new int[n][m];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                graph[i][j] = line.charAt(j) - '0';
            }
        }
        dfs(0, 0);
        System.out.println(answer);
    }


}
