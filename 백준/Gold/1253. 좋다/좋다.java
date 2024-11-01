import java.io.*;
import java.util.*;

public class Main {



    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        int n;
        n=Integer.parseInt(s.nextToken());
        int[]array=new int[n];
        s = new StringTokenizer(br.readLine(), " ");
        for(int i=0;i<n;i++){
            array[i]=Integer.parseInt(s.nextToken());
        }
        Arrays.sort(array);
        int answer=0;
        for(int i=0;i<n;i++){
            int left=0;
            int right=n-1;
            while (left<right){
                if (left==i) {
                    left += 1;
                    continue;
                }
                if (right==i){
                    right-=1;
                    continue;
                }
                int now=array[left]+array[right];
                if (now==array[i]){
                    answer+=1;
                    break;
                }
                if (now<=array[i])
                    left+=1;
                else
                    right-=1;
            }
        }
        System.out.println(answer);


    }

}