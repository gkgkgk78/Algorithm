import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        HashSet<Integer>set=new HashSet<>();
        for(int i=0;i<nums.length;i++){
            set.add(nums[i]);
        }
        int temp=nums.length/2;
        if(set.size()>temp)
            return temp;
        answer=set.size();
        
        return answer;
    }
}