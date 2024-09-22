import java.util.*;

class Solution {
    static int answer=0;
    //n개의 음이 아닌 정수들이 존재한다
    //적절히 더하거나 빼서 타겟 넘버를 만들려고 한다
    public void dfs(int[]numbers,String []go,int target,int last,int index){
        if(index==last)
        {
            int temp=0;
            for(int i=0;i<numbers.length;i++){
                if(go[i]=="-")
                {
                    temp-=numbers[i];
                }
                else
                    temp+=numbers[i];
            }

            if(temp==target){
                answer+=1;
        }

            return;
        }
        go[index]="-";
        dfs(numbers,go,target,last,index+1);
        go[index]="+";
        dfs(numbers,go,target,last,index+1);

        
    }
    
    
    public int solution(int[] numbers, int target) {
        String[] go=new String[numbers.length];  
        dfs(numbers,go,target,numbers.length,0);
        
        return answer;
    }
}