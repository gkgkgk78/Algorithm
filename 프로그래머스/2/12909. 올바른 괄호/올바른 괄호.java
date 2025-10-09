import java.util.*; 
class Solution {
    boolean solution(String s) {
        boolean answer = true;
        
        Deque<Integer>q=new ArrayDeque<>();
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='('){
                q.add(1);
            }
            else{
                if(q.isEmpty())
                    return false;
                q.pollFirst();
            }
        }
        if(!q.isEmpty())
            return false;

        return answer;
    }
}