import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        List<Integer>list=new LinkedList<>();
        int check=arr[0];
        list.add(arr[0]);
        for(int i=1;i<arr.length;i++){
            if(arr[i]==check)
                continue;
            else
            {
                check=arr[i];
                list.add(arr[i]);
            }
        }
        answer=list.stream().mapToInt(i->i).toArray();
        return answer;
    }
}