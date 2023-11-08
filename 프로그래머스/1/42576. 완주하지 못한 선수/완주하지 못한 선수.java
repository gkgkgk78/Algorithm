import java.util.*;
class Solution {
 
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String,Integer>m=new HashMap<>();
        
        for(String s: participant)
        {
            if(!m.containsKey(s))
                m.put(s,1);
            else
                m.put(s,m.get(s)+1);
        }
        for(String s: completion)
        {
            if(!m.containsKey(s))
                return s;
            else
                m.put(s,m.get(s)-1);
        }
          for(String s: participant)
        {
            if(m.get(s)==1)
                return s;
        }
        
        return answer;
    }
}