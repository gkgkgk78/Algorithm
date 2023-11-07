import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> q = new PriorityQueue<>();
        
        for(int i=0;i<scoville.length;i++)
        {
            q.add(scoville[i]);
        }
        int count=0;
        //모든 음식의 스코빌 지수가 k이상이 될때 까지 반복 한다
        while(true)
        {
            if(q.size()==0)
                break;
            int a1=q.poll();
            if(a1>=K)
                return count;
            if(q.size()==0)
                break;
            int a2=q.poll();
            q.add(a1+a2*2);           
            count+=1;
        }
    
        
        return -1;
    }
}