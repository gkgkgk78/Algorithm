import java.util.*;
class Solution {
 
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String,Integer>left=new HashMap<>();
        HashMap<String,Integer>right=new HashMap<>();

        for(String s:completion){
            if(right.containsKey(s))
            {
                right.put(s,right.get(s)+1);
            }
            else
            {
                right.put(s,1);
            }
        }
        
        for(String s:participant){
            if(!right.containsKey(s))
                return s;
            int now=right.get(s);
            if(now==0)
                return s;
            else
                right.put(s,now-1);
        }
        
        
        return answer;
    }
}