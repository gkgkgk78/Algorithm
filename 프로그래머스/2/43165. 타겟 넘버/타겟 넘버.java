import java.util.*;
class Solution {
    
    static int [] array;
    
    static int answer=0;
    
    public void dfs(int depth, int [] numbers,int target){
        if(depth==numbers.length){
            int temp=0;
            for(int i=0;i<numbers.length;i++){
                if(array[i]==1){
                    temp+=numbers[i];
                }
                else{
                    temp-=numbers[i];
                }
            }
            if(temp==target)
                answer+=1;
            return;
        }
        array[depth]=1;
        dfs(depth+1,numbers,target);
        array[depth]=-1;
        dfs(depth+1,numbers,target);
    
    }
    
     
    public int solution(int[] numbers, int target) {
        array=new int[numbers.length];
        dfs(0,numbers,target);
        return answer;
    }
    
}