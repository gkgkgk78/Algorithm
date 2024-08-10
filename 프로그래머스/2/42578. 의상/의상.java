import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        //코니는 매일 다른 옷을 조합하여 입는것을 좋아한다
        //얼굴 상의 하의 겉옷
        int different=0;
        HashMap<String,Integer>map=new HashMap<>();
        for(String[] s: clothes){
            String name=s[0];
            String type=s[1];
            if(map.containsKey(type)){
                map.put(type,map.get(type)+1);
            }
            else{
                map.put(type,1);
            }
        }
        for(String s:map.keySet()){
            answer*=map.get(s)+1;
        }
       
        
        
        return answer-1;
    }
}