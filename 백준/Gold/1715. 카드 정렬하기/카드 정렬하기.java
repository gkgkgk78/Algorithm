import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {

    public static int go(PriorityQueue<Integer>q){
        int now=0;
        while(true){
            if (q.isEmpty())
                break;
            int a1=0;
            int a2=0;
            if (!q.isEmpty())
                a1=q.poll();
            if (!q.isEmpty())
                a2=q.poll();
            if(a1==0 || a2==0)
                break;
            now+=(a1+a2);
            q.add(a1+a2);
        }
        return now;
    }




    public static void main(String[] args) throws IOException {

        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(s.nextToken());
        PriorityQueue<Integer> q = new PriorityQueue<>((x, y) -> {
            return x - y;
        });

        for (int i = 0; i < n; i++) {
            s = new StringTokenizer(br.readLine(), " ");
            q.add(Integer.parseInt(s.nextToken()));
        }
        int answer=go(q);
        System.out.println(answer);




    }
}
