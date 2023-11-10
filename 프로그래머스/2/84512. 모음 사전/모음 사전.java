import java.util.*;
class Solution {
    
    static int answer=0;
    static int count=0;
    static char[] ss={'A','E','I','O','U'};
    public static void dfs(int index,String word,String now)
    {
        if(now.equals(word)){
                answer=count;
                return;
            }
        if(index==5)
        {    
            return;
        }
        for(int i=0;i<5;i++)
        {
            //System.out.println(now);
            count+=1;
            String ss1=now+String.valueOf(ss[i]);
            dfs(index+1,word,ss1);
        }

    }
    
    
    
    public int solution(String word) {
        dfs(0,word,"");
        
        return answer;
    }
}