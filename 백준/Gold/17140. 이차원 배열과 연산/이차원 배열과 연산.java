import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {


    static int r, c, k;

    static int graph[][];

    public static class go {
        int x, y;

        public go(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }


    public static void game_r() {
        List<List<Integer>> list = new LinkedList<>();
        //이제 체크를 해봐야 함
        for (int i = 0; i < graph.length; i++) {
            Map<Integer, Integer> map = new HashMap<>();
            for (int j = 0; j < graph[0].length; j++) {
                if (graph[i][j] == 0)
                    continue;
                int first = 0;
                if (map.containsKey(graph[i][j])) {
                    first = map.get(graph[i][j]);
                }
                first += 1;
                map.put(graph[i][j], first);
            }
            //다 넣은 후에 이제 결과 값을 얻어와 보자
            Set keys = map.keySet();
            List<go> list1 = new LinkedList<>();
            for (Object s : keys) {
                int aa = Integer.parseInt(s.toString());
                list1.add(new go(aa, map.get(aa)));
            }
            list1.sort((a, b) -> {
                if (a.y == b.y)
                    return a.x - b.x;
                return a.y - b.y;
            });
            //이제 찾아낸 만큼 배열 만들어 주면 될듯
            List<Integer> temp = new LinkedList<>();
            for (go g : list1) {
                temp.add(g.x);
                temp.add(g.y);
            }
            //만들어 준후에
            list.add(temp);
        }
        //가장 긴 행에 대해서 배열 재구성 하면 될듯
        int r = graph.length;
        int c = graph[0].length;
        for (List<Integer> gg : list) {
            c = Integer.max(c, gg.size());
        }
        graph = new int[r][c];
        for (int i = 0; i < r; i++) {
            List<Integer> li = list.get(i);
            for (int j = 0; j < li.size(); j++) {
                graph[i][j] = li.get(j);
            }
        }
    }

    public static void game_c() {
        List<List<Integer>> list = new LinkedList<>();
        //이제 체크를 해봐야 함
        for (int i = 0; i < graph[0].length; i++) {
            Map<Integer, Integer> map = new HashMap<>();
            for (int j = 0; j < graph.length; j++) {
                if (graph[j][i] == 0)
                    continue;
                int first = 0;
                if (map.containsKey(graph[j][i])) {
                    first = map.get(graph[j][i]);
                }
                first += 1;
                map.put(graph[j][i], first);
            }
            //다 넣은 후에 이제 결과 값을 얻어와 보자
            Set keys = map.keySet();
            List<go> list1 = new LinkedList<>();
            for (Object s : keys) {
                int aa = Integer.parseInt(s.toString());
                list1.add(new go(aa, map.get(aa)));
            }
            list1.sort((a, b) -> {
                if (a.y == b.y)
                    return a.x - b.x;
                return a.y - b.y;
            });
            //이제 찾아낸 만큼 배열 만들어 주면 될듯
            List<Integer> temp = new LinkedList<>();
            for (go g : list1) {
                temp.add(g.x);
                temp.add(g.y);
            }
            //만들어 준후에
            list.add(temp);
        }
        //가장 긴 행에 대해서 배열 재구성 하면 될듯
        int r = graph.length;
        int c = graph[0].length;
        for (List<Integer> gg : list) {
            r = Integer.max(r, gg.size());
        }
        graph = new int[r][c];
        for (int i = 0; i < c; i++) {
            List<Integer> li = list.get(i);
            for (int j = 0; j < li.size(); j++) {
                graph[j][i] = li.get(j);
            }
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        r = Integer.parseInt(s.nextToken());
        c = Integer.parseInt(s.nextToken());
        r -= 1;
        c -= 1;
        k = Integer.parseInt(s.nextToken());
        graph = new int[3][3];
        for (int i = 0; i < 3; i++) {
            s = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < 3; j++) {
                graph[i][j] = Integer.parseInt(s.nextToken());
            }
        }
        int count = -1;
        for (int i = 0; i <= 100; i++) {
            if (r < graph.length && c < graph[0].length) {
                if (graph[r][c] == k) {
                    count = i;
                    break;
                }
            }
            int row = graph.length;
            int col = graph[0].length;
            if (row >= col) {
                game_r();
            } else {
                game_c();
            }
            if (r < graph.length && c < graph[0].length) {
                if (graph[r][c] == k) {
                    count = i + 1;
                    break;
                }
            }
        }
        System.out.println(count);
    }
}