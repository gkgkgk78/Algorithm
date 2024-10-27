import javax.swing.*;
import java.io.*;
import java.util.*;

public class Main {

    static int n, m;
    static char[][] graph;

    static class go {
        int x, y;

        public go(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int[] isSelected = new int[2];
    static List<go> list;
    static int answer = -1;

    public static void comb(int start, int cnt, int size) {
        if (cnt == 2) {
            game();
            return;
        }
        for (int i = start; i < size; i++) {
            isSelected[cnt] = i;
            comb(i + 1, cnt + 1, size);
        }
    }

    public static void game() {

        go first = list.get(isSelected[0]);
        go second = list.get(isSelected[1]);
        int size = 0;
        if (first.x==2&&first.y==2&&second.x==2&&second.y==5)
            size=0;


        for (int i = 0; i < 8; i++) {
            //첫번째 부터 만들어 보자
            int visit[][] = new int[n][m];
            int sizeFirst = makeFirst(first.x, first.y, visit, i);
            if (sizeFirst == -1)
                break;
            if (visit[second.x][second.y]==1)
                continue;
            makeSecond(second.x, second.y, visit, size, sizeFirst);
        }


    }

    public static int makeFirst(int x, int y, int visit[][], int size) {
        int dx[] = {-1, 0, 1, 0};
        int dy[] = {0, -1, 0, 1};
        int size1 = 1;
        for (int i = 1; i <= size; i++) {
            for (int j = 0; j < 4; j++) {
                int zx = x + dx[j] * i;
                int zy = y + dy[j] * i;
                if (0 <= zx && zx < n && 0 <= zy && zy < m) {
                    if (graph[zx][zy] == '#' && visit[zx][zy] == 0)
                        continue;
                    else {
                        return -1;
                    }
                } else {
                    return -1;
                }
            }
            size1 += 4;
            for (int j = 0; j < 4; j++) {
                int zx = x + dx[j] * i;
                int zy = y + dy[j] * i;
                visit[zx][zy] = 1;
            }
        }
        return size1;
    }

    public static int makeSecond(int x, int y, int visit[][], int size, int sizeFirst) {
        int dx[] = {-1, 0, 1, 0};
        int dy[] = {0, -1, 0, 1};
        int size1 = 1;
        answer = Math.max(answer, size1 * sizeFirst);
        for (int i = 1; i <= 8; i++) {
            for (int j = 0; j < 4; j++) {
                int zx = x + dx[j] * i;
                int zy = y + dy[j] * i;
                if (0 <= zx && zx < n && 0 <= zy && zy < m) {
                    if (graph[zx][zy] == '#' && visit[zx][zy] == 0)
                        continue;
                    else {
                        return -1;
                    }
                } else {
                    return -1;
                }
            }
            size1 += 4;
            for (int j = 0; j < 4; j++) {
                int zx = x + dx[j] * i;
                int zy = y + dy[j] * i;
                visit[zx][zy] = 1;
            }
            answer = Math.max(answer, size1 * sizeFirst);
        }
        return size1;
    }


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");

        n = Integer.parseInt(s.nextToken());
        m = Integer.parseInt(s.nextToken());
        graph = new char[n][m];
        list = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            String now = br.readLine();
            for (int j = 0; j < m; j++) {
                graph[i][j] = now.charAt(j);
                if (graph[i][j] == '#')
                    list.add(new go(i, j));
            }
        }
        //놓은 십자가 넓이의 곱의 최댓값을 구하라
        comb(0, 0, list.size());
        System.out.println(answer);


    }


}