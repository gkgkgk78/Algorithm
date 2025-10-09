import java.util.*;
class Solution {
    
    public static int check=-1;
    
    class tx{
        int num;
        int total;
        tx(int num,int total){
            this.num=num;
            this.total=total;
        }
    }
    
    
    public tx go(int[]answers,int[] cal,int in){
        int index=0;
        int sumz=0;
        for (int i=0;i<answers.length;i++){
            if (index==cal.length){
                index=0;
            }
            if(answers[i]==cal[index])
                sumz+=1;
            index+=1;
        }
        check=Math.max(check,sumz);
        return new tx(in,sumz);
    }
    
    
    
    public int[] solution(int[] answers) {
        int[] answer = {};
        
        int[] solution1={1,2,3,4,5};
        int[] solution2={2,1,2,3,2,4,2,5};
        int[] solution3={3,3,1,1,2,2,4,4,5,5};
        
        List<tx>list=new LinkedList<>();
        List<Integer>an=new ArrayList<>();

        
        list.add(go(answers,solution1,1));
        list.add(go(answers,solution2,2));
        list.add(go(answers,solution3,3));
        for(tx t: list){
            if(t.total==check)
                an.add(t.num);
        }
      
        answer=new int[an.size()];
        for(int i=0;i<an.size();i++){
            answer[i]=an.get(i);
        }
        
        
        return answer;
    }
}