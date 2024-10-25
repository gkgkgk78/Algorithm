import java.awt.*;
import java.beans.VetoableChangeListener;
import java.io.*;
import java.security.cert.CertificateParsingException;
import java.util.*;
import java.util.List;


public class Main {


    public static class go {
        int index, color;

        public go(int index, int color) {
            this.index = index;
            this.color = color;
        }
    }

    static ArrayList<Integer>[] list;

    static void bfs(int[] visit, int vertex) {
        Deque<go> q = new ArrayDeque<>();
        visit[vertex] = 1;
        q.add(new go(vertex, 1));
        while (!q.isEmpty()) {
            go a = q.poll();
            for (int v : list[a.index]) {
                if (visit[v] == 0) {
                    int next = 0;
                    if (a.color == 1)
                        next = 2;
                    else
                        next = 1;
                    q.add(new go(v, next));
                    visit[v]=next;
                }
            }
        }
    }


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        //청팀과 백팀으로 팀을 나누어 팀전을 진행하자
        int n = Integer.parseInt(s.nextToken());
        //사람들이 각각 싫어하는 사람들의 정보가 주어질시에 , 서로 싫어하는 사람은 같은 팀에 넣지 않으려 한다
        list = new ArrayList[n + 1];
        for (int i = 1; i < n + 1; i++) {
            list[i] = new ArrayList<>();
        }
        for (int i = 1; i <= n; i++) {
            s = new StringTokenizer(br.readLine(), " ");
            int leng = Integer.parseInt(s.nextToken());
            for (int j = 0; j < leng; j++) {
                list[i].add(Integer.parseInt(s.nextToken()));
            }
        }

        //이제 시작하자
        int visit[] = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            if (visit[i] == 0) {
                bfs(visit, i);
            }
        }
        List<Integer>blue=new ArrayList<>();
        List<Integer>white=new ArrayList<>();
        for(int i=1;i<=n;i++){
            if (visit[i]==1)
                blue.add(i);
            else
                white.add(i);
        }
        System.out.println(blue.size());
        for (int a:blue)
            System.out.print(a+" ");
        System.out.println();
        System.out.println(white.size());
        for (int a:white)
            System.out.print(a+" ");

    }


}