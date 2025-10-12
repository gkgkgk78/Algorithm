import java.util.*;
class Solution {
    
    static int[] isSelected;
    static char[] go=new char[]{'A', 'E', 'I', 'O', 'U'};
    static List<String>list=new ArrayList<>();
    
    public void make(String now,int cnt){
        if(cnt>=5){
            return; 
        }
        for(int i=0;i<5;i++){
            String temp=now;
            temp+=go[i];
            list.add(temp);
            make(temp,cnt+1);
        }
    }
    
    
    public int solution(String word) {
        int answer = 0;
        
        make("",0);
        for(int i=0;i<list.size();i++){ if(list.get(i).equals(word)) return i+1; }
        
        
        return answer;
    }
}