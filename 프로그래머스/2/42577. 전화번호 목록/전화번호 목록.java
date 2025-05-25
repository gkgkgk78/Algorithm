import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        
        HashMap<String,String>map=new HashMap<>();
        for(String s : phone_book){
            map.put(s,s);
        }
        for(int i=0;i<phone_book.length;i++){
            String now=phone_book[i];
            for(int j=0;j<now.length();j++){
                String temp=now.substring(0,j);
                if(map.containsKey(temp))
                    return false;
            }
        }
        
        
        return answer;
    }
}