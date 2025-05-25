import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        HashMap<String,Integer> completionHashMaps=new HashMap<>();

        for(String s : completion){
            if(completionHashMaps.containsKey(s))
                completionHashMaps.put(s,completionHashMaps.get(s)+1);
            else
                completionHashMaps.put(s,1);
        }
        for(String s : participant){
            if(!completionHashMaps.containsKey(s)||completionHashMaps.get(s)==0){
                answer=s;
                break;
            }           
            completionHashMaps.put(s,completionHashMaps.get(s)-1);
        }
        
        
        return answer;
    }
}