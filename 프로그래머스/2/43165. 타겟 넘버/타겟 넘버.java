import java.util.*;

class Solution {
    
    static int[]numbers;
    static int target;
    static int answer=0;
    
    public void dfs(char[] array,int now){
        if(now==numbers.length){
            int temp=0;
            for(int i=0;i<numbers.length;i++){
                if(array[i]=='-'){
                    temp-=numbers[i];
                }
                else{
                    temp+=numbers[i];
                }
            }
            if(temp==target)
                answer+=1;
            return;
        }

            array[now]='-';
            dfs(array,now+1);
            array[now]='+';
            dfs(array,now+1);
        
    }
    
    
    
    public int solution(int[] number, int targe) {
        numbers=number;
        target=targe;
        char [] array=new char[numbers.length];
        dfs(array,0);
        return answer;
    }
}