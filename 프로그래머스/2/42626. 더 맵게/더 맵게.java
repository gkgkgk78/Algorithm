import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer>q=new PriorityQueue<>();
        for(int i:scoville){
            q.add(i);
        }
        
        while(!q.isEmpty()){
            int now=q.poll();
            if(now>=K)
                return answer;
            if(q.isEmpty())
                return -1;
            int now1=q.poll();
            q.add(now+now1*2);
            answer+=1;

        
        }

        return -1;
    }
}