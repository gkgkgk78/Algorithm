import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer = {};
        Deque<Integer> queue=new ArrayDeque<>();
        for(int i=0;i<progresses.length;i++){
            int div=(100-progresses[i])/speeds[i];
            int mod=(100-progresses[i])%speeds[i];
            if(mod!=0)
                div+=1;
            queue.add(div);
        }
        List<Integer>list=new LinkedList<>();
        int first=-1;
        int size=0;
        while(!queue.isEmpty())
        {
            int s=queue.removeFirst();
            if(first==-1)
            {
                size=1;
                first=s;
            }
            else
            {
                if(s<=first)
                {
                    size+=1;
                }
                else
                {
                    list.add(size);
                    first=s;
                    size=1;
                }
            }
        }
        list.add(size);

        answer=list.stream().mapToInt(i->i).toArray();
        
        
        
        
        return answer;
    }
}