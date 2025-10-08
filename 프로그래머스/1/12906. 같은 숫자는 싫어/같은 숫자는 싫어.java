import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        List<Integer>list=new ArrayList<>();
        int last=-1;
        for(int i : arr){
            if (last==-1){
                last=i;
                list.add(i);
                continue;
            }
            if(i==last)
                continue;
            last=i;
            list.add(i);
        }
        answer=new int[list.size()];
        for(int i=0;i<list.size();i++){
            answer[i]=list.get(i);
        }
       

        return answer;
    }
}