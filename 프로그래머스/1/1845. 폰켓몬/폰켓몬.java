import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        //같은 종류의 폰켓몬은 같은 번호를 가지고 있다
        HashMap<Integer,Integer>map=new HashMap<>();
        int count=0;
        for (int i=0;i<nums.length;i++){
            int now=nums[i];
            if(!map.containsKey(now)){
                count+=1;
                map.put(now,1);
            }   
        }
        int test=nums.length/2;
        if(count>=test)
        {
            return test;
        }
        else
            return count;

        
    }
}