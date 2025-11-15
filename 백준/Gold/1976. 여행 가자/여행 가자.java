

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {


    static int[] parents;
    static int n;

    public static void make() {
        for (int i = 0; i < n; i++) {
            parents[i] = i;
        }
    }

    public static int find(int v) {
        if (parents[v] == v)
            return v;
        return find(parents[v]);
    }

    public static void union(int v1, int v2) {
        int f1 = find(v1);
        int f2 = find(v2);
        if (f1 != f2) {
            if (f1 < f2) {
                parents[f2] = f1;
            } else {
                parents[f1] = f2;
            }
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine(), " ");
        parents = new int[n];
        int m = Integer.parseInt(st.nextToken());

        make();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < n; j++) {
                int a = Integer.parseInt(st.nextToken());
                if (a == 1) {
                    union(i, j);
                }
            }
        }
        st = new StringTokenizer(br.readLine(), " ");
        int size = st.countTokens();
        int[] plan = new int[size];
        for (int i = 0; i < size; i++) {
            plan[i] = Integer.parseInt(st.nextToken());
            plan[i] -= 1;
        }
        for (int i = 0; i < n; i++) {
            parents[i] = find(i);
        }
        String answer = "YES";
        int first = parents[plan[0]];
        for (int i = 1; i < size; i++) {
            if (first != parents[plan[i]]) {
                answer = "NO";
                break;
            }
        }
        System.out.println(answer);


    }


}
