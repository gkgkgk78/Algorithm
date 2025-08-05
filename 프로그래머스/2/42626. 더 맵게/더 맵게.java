import java.util.*;
class Solution {
    
    public int solution(int[] scoville, int k) {
        int answer = 0;
        //모든 음식의 스코빌 지수를 k이상으로 만들고자 한다.
        PriorityQueue<Integer>q=new PriorityQueue<>((a,b)->a-b);
        
        for(int i=0;i<scoville.length;i++){
            q.add(scoville[i]);
        }
        while(!q.isEmpty()){
            int a1=q.poll();
            // System.out.println(a1);
            if(a1>=k){
                return answer;
            }
            if(q.isEmpty())
                return -1;
            int a2=q.poll();
            // System.out.println(a2);
            q.add(a1+a2*2);
            answer+=1;
        }
        return -1;
    }
}