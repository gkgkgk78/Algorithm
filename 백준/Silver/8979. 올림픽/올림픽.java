import java.io.*;
import java.util.*;

public class Main {

    public static class go {
        int vertex;
        int gold, silver, dong;

        public go(int vertex, int gold, int silver, int dong) {
            this.vertex = vertex;
            this.gold = gold;
            this.silver = silver;
            this.dong = dong;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        //비공식적 국가간 순위 정하고 있다
        //금,은,동
        int n, m;
        n = Integer.parseInt(s.nextToken());
        m = Integer.parseInt(s.nextToken());
        List<go> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int a1, a2, a3, a4;
            s = new StringTokenizer(br.readLine(), " ");
            a1 = Integer.parseInt(s.nextToken());
            a2 = Integer.parseInt(s.nextToken());
            a3 = Integer.parseInt(s.nextToken());
            a4 = Integer.parseInt(s.nextToken());
            list.add(new go(a1 - 1, a2, a3, a4));
        }
        list.sort((x, y) -> {
            if (x.gold != y.gold)
                return y.gold - x.gold;
            else if (x.silver != y.silver) {  // 두 번째 기준: silver
                return y.silver - x.silver;
            } else {  // 세 번째 기준: bronze
                return y.dong - x.dong;
            }
        });
        int start = 1;
        int count = 0;
        int answer[] = new int[n];
        int before1 = -1;
        int before2 = -1;
        int before3 = -1;

        for (go a : list) {
            //동점자 있으면 작업해줘야함
            if (before1 == -1 && before2 == -1 && before2 == -1) {
                before1 = a.gold;
                before2 = a.silver;
                before3 = a.dong;
                count += 1;

            } else {
                if (a.gold == before1 && a.silver == before2 && a.dong == before3) {
                    count += 1;
                } else {
                    before1 = a.gold;
                    before2 = a.silver;
                    before3 = a.dong;
                    start += count;
                    count = 1;
                }

            }
            answer[a.vertex] = start;
        }
        System.out.println(answer[m - 1]);

    }

}