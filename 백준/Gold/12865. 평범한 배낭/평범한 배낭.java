import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());
        int m=Integer.parseInt(st.nextToken());
        int [][]item=new int[n+1][2];
        for(int i=1;i<=n;i++){
            st=new StringTokenizer(br.readLine());
            item[i][0]=Integer.parseInt(st.nextToken());
            item[i][1]=Integer.parseInt(st.nextToken());
        }
        int [][]arr=new int[m+1][n+1];
        for(int i=1;i<=m;i++){
            for(int j=1;j<=n;j++){
                int weight=item[j][0];
                int val=item[j][1];
                arr[i][j]=arr[i][j-1];
                if (i-weight<0) {
                    continue;
                }
                arr[i][j]=Math.max(arr[i][j-1],arr[i-weight][j-1]+val);
            }
        }
        System.out.println(arr[m][n]);
    }
}