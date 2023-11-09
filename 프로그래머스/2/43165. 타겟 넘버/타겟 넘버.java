import java.util.*;
class Solution {
    static int answer=0;
    
    public void dfs(int index,int sumz,int target,int[]arr){
        
        if(index==arr.length){
            if(sumz==target)
                answer+=1;
            return ;
        }
        dfs(index+1,sumz+arr[index],target,arr);
        dfs(index+1,sumz-arr[index],target,arr);

        return ;
    };
    
    
    
    public int solution(int[] numbers, int target) {
        
        dfs(0,0,target,numbers);
        
        
        
        
        return answer;
    }
}