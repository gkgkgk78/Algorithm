import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {

    static int n;
    static LinkedList<go>[] list;

    static class go {
        int x, y, value;

        public go(int x, int y, int value) {
            this.x = x;
            this.y = y;
            this.value = value;
        }

        public go(int x, int value) {
            this.x = x;
            this.value = value;
        }
    }

    static int dijk(int start, int fin) {
        int distance[]=new int[n+1];
        for(int i=1;i<n+1;i++){
            distance[i]=99999999;
        }
        distance[start]=0;
        PriorityQueue<go>q=new PriorityQueue<>((x,y)->{
            return x.value-y.value;
        });
        q.add(new go(start,0));

        while(!q.isEmpty()){
            go now=q.poll();
            if (now.value>distance[now.x])
                continue;
            for(go a:list[now.x]){
                int temp=a.value+now.value;
                if(temp<distance[a.x]){
                    distance[a.x]=temp;
                    q.add(new go(a.x,temp));
                }
            }
        }
        return distance[fin];
    }


    public static void main(String[] args) throws IOException {


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        int m;
        n = Integer.parseInt(s.nextToken());
        m = Integer.parseInt(s.nextToken());
        list = new LinkedList[n+1];
        for (int i = 0; i < n+1; i++) {
            list[i] = new LinkedList<>();
        }

        for (int i = 0; i < m; i++) {
            int a1, a2, a3;
            s = new StringTokenizer(br.readLine(), " ");
            a1 = Integer.parseInt(s.nextToken());
            a2 = Integer.parseInt(s.nextToken());
            a3 = Integer.parseInt(s.nextToken());
            list[a1].add(new go(a2, a3));
            list[a2].add(new go(a1, a3));
        }
        int start, fin;
        s = new StringTokenizer(br.readLine(), " ");
        start = Integer.parseInt(s.nextToken());
        fin = Integer.parseInt(s.nextToken());
        int result1=dijk(1,start)+dijk(start,fin)+dijk(fin,n);
        int result2=dijk(1,fin)+dijk(fin,start)+dijk(start,n);
        int answer=Math.min(result1,result2);
        if(answer>=99999999)
        {
            System.out.println(-1);
        }
        else
            System.out.println(answer);

    }
}