import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for(int i=0;i<commands.length;i++){
            int []temp=commands[i];
            int first=temp[0];
            int second=temp[1];
            int third=temp[2];
            List<Integer>last=new ArrayList<>();
            for(int i1=first-1;i1<second;i1++){
                last.add(array[i1]);
            }
            last.sort((x,y)->{return x-y;});
            answer[i]=last.get(third-1);       
        }
        
        
        
        return answer;
    }
}