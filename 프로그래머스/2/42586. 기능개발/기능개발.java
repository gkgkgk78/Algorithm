import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer = {};
        //각 배포마다 몇개의 기능이 배포되는지?
        List<Integer>an=new ArrayList<>();
        ArrayDeque<Integer>temp=new ArrayDeque<>();
        
        for(int i=0;i<progresses.length;i++){
            double check=(100-(double)progresses[i])/(double)speeds[i];
            temp.add((int)Math.ceil(check));
        }
        int day=0;
        while(!temp.isEmpty()){
            int check=0;
            int first=temp.pollFirst();
            check+=1;
            day=first;
            while(!temp.isEmpty()){
                int second=temp.pollFirst();
                if(second<=day){
                    check+=1;
                }
                else{
                    temp.addFirst(second);
                    break;
                }
            }
            an.add(check);
        }
        answer=new int[an.size()];
        for(int i=0;i<an.size();i++){
            answer[i]=an.get(i);
        }
       
        
        
        return answer;
    }
}