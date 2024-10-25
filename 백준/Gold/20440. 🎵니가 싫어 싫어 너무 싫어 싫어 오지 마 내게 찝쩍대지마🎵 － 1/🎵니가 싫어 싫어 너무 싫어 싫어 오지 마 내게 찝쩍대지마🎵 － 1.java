import javax.naming.spi.ObjectFactory;
import java.awt.*;
import java.awt.image.AreaAveragingScaleFilter;
import java.beans.VetoableChangeListener;
import java.io.*;
import java.util.*;
import java.util.List;


public class Main {


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(s.nextToken());
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            s = new StringTokenizer(br.readLine(), " ");
            int a1, a2;
            a1 = Integer.parseInt(s.nextToken());
            a2 = Integer.parseInt(s.nextToken());
            if(map.containsKey(a1))
                map.put(a1,map.get(a1)+1);
            else
                map.put(a1,1);
            if(map.containsKey(a2))
                map.put(a2,map.get(a2)-1);
            else
                map.put(a2,-1);
        }

        List<Integer>list=new LinkedList<>();
        for(int i:map.keySet()){
            list.add(i);
        }
        list.sort((x,y)->{
            return x-y;
        });
        int left=-1;
        int right=0;
        int answer=0;
        int sum=0;
        int before=0;
        for(int i:list){
            sum+=map.get(i);
            if (sum>answer){
                left=i;
                answer=sum;
                before=1;
            }
            else if (sum<answer&&before==1){
                right=i;
                before=0;
            }
        }
        System.out.println(answer);
        System.out.println(left+" "+right);





    }


}