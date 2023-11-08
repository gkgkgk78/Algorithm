import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        //n/2 마리 가져 가도 좋다
        HashSet<Integer>set=new HashSet<>();
        for(Integer a:nums)
            set.add(a);
        if(set.size()>=nums.length/2)
            answer= nums.length/2;
        else
            answer=set.size();
        
        return answer;
    }
}