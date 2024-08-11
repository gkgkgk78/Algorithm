import java.util.*;
class Solution {
    boolean solution(String s) {
        boolean answer = false;
        Deque<Character>deque=new ArrayDeque<>();
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            if(ch=='(')
            {
                deque.add(ch);
            }
            else
            {
                if(deque.size()==0)
                    return false;
                else
                    deque.removeLast();
            }
        }
        if(deque.size()==0)
            return true;
        
        
        return answer;
    }
}