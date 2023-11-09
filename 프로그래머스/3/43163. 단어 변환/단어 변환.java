import java.util.*;
class Solution {
    static int answer=99999;
    public int check(String s1, String s2)
    {
        int count=0;
        for(int i=0;i<s1.length();i++)
        {
            if(s1.charAt(i)==s2.charAt(i))
                count+=1;
        }
        //System.out.println(s1+" "+s2+" "+count);
        if(count==s1.length()-1)
            return 1;
        return 0;
    }
    
    public void dfs(String begin,String target,String[] words, String now,int [] visit,int count)
    {
        
        
        if(now.equals(target))
        {
            answer=Math.min(answer,count);
            return;
        }
            
        for(int i=0;i<words.length;i++)
        {
            if(visit[i]==0)
            {
                int z=check(now,words[i]);
                //이제 확인을 해보도록 하자
                if(z==1)
                {
                    visit[i]=1;
                    dfs(begin,target,words,words[i],visit,count+1);
                    visit[i]=0;
                }
            }
        }
    
    }
    
    
    
    public int solution(String begin, String target, String[] words) {
        
        int visit[]=new int[words.length];
        dfs(begin,target,words, begin,visit,0);
        
        if(answer==99999)
            answer=0;
        
        
        return answer;
    }
}