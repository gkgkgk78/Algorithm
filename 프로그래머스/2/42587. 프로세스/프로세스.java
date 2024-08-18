import java.util.*;

class go{
    int prior,location;
    public go(int x,int y){
        this.prior=x;
        this.location=y;
    }
}

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        //특정 프로세스가 몇 번째로 실행되는지 알아보기
        PriorityQueue<Integer> pq=new PriorityQueue<>((x,y)->{
            return y-x;
        });
        Deque<go>deque=new ArrayDeque<>();
        for (int i=0;i<priorities.length;i++)
        {
            pq.add(priorities[i]);
            deque.add(new go(priorities[i],i));
        }
        int check=0;
        while(deque.size()>0){
            go a=deque.removeFirst();
            int now=pq.poll();
            //System.out.println(a.prior+" "+a.location);
            if(a.prior>=now){
                check+=1;
                if(a.location==location){
                    return check;
                }
            }
            else
            {
                deque.add(a);
                pq.add(now);
            }
            
        }
        
        
        
        return answer;
    }
}