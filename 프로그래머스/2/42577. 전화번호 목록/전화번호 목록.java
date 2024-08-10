import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        
        HashMap<String,Integer>map=new HashMap<>();
        for(String s:phone_book)
            map.put(s,0);
        //이제 찾아 보도록 하자
        for(String s: phone_book){
            int now=s.length();
            for(int i=1;i<s.length();i++){
                String temp=s.substring(0,i);
                if(map.containsKey(temp))
                    return false;
            }
        }
   
        return answer;
    }
}