import java.util.*;
class Solution {
    public class go{
        int index, num,time;
        go(int index,int num,int time){
            this.index=index;
            this.num=num;
            this.time=time;
        }
    }
    
    
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        Deque<go>q=new ArrayDeque<>();
        
        q.offer(new go(0,prices[0],1));
        int time=2;
        
        for(int i=1;i<prices.length;i++){
            int now=prices[i];
            while(!q.isEmpty()){
                go temp=q.pollLast();
                if(temp.num>now){
                    answer[temp.index]=time-temp.time;
                }
                else{
                    q.addLast(temp);
                    break;
                }
            }
            q.addLast(new go(i,now,time));
            time+=1;
        }
        time-=1;
        while(!q.isEmpty()){
            go temp=q.pollLast();
            answer[temp.index]=time-temp.time;
        }
        
        
        
        
        return answer;
    }
}