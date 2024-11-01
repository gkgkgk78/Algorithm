import java.io.*;
import java.util.*;

public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        int n,m;
        n=Integer.parseInt(s.nextToken());
        m=Integer.parseInt(s.nextToken());
        boolean digit[]=new boolean[m+1];
        digit[0]=true;//false: 소수 아님
        digit[1]=true;
        for (int i=2;i<=Math.sqrt(m);i++){
            if (digit[i])
                continue;
            int count=2;
            while (true){
                int now=i*count;
                if (now>m)
                    break;
                digit[now]=true;
                count+=1;
            }
        }
        StringBuilder sb=new StringBuilder();
        for(int i=n;i<=m;i++){
            if (!digit[i])
                sb.append(i+"\n");
        }
        System.out.println(sb);


    }

}