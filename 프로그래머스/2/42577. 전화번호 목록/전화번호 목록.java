import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        
        HashMap<String,Integer>map=new HashMap<>();
        for (String s: phone_book){
            map.put(s,1);
        }
        
        for(String s : map.keySet()){
            
            String temp="";
            for(int i=0;i<s.length()-1;i++){
                temp+=s.charAt(i);
                if(map.containsKey(temp))
                    return false;
            }
        }
        return answer;
    }
}