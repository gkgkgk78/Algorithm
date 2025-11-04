import java.util.*;
class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        long left=-1;
        long right=-1;
        for(int i:times){
            right=Math.max(right,i);
        }
        right=right*n+1;
        
        while(left+1<right){
            long mid=(left+right)/2;
            long temp=0;
            for(int i: times){
                temp+=mid/i;
                if(temp>=n)
                    break;
            }
            
            if(temp>=n){
                right=mid;
                answer=mid;
            }
            else{
                left=mid;
            }
            
        }
            
        return answer;
    }
}