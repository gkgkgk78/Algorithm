import java.util.*;

class Solution {
    
    public static int isselected[];
    public static int isvisit[];
    public int game=0;
    public static int answer=-1;
    
    
    public static void game(int k,int [][]dungeons)
    {
        int now=k;
        int index=0;
        int count=0;
        for(int i=0;i<isselected.length;i++)
        {
            int first=dungeons[isselected[i]][0];
            int second=dungeons[isselected[i]][1];
            if(now>=first)
            {
                now-=second;
                count+=1;
            }
            else
                break;
            
            
        }
        
        answer=Math.max(answer,count);
        
    }
    
    
    public static void perm(int cnt,int n,int k,int [][]dungeons)
    {
        if(cnt==n)
        {
            game(k,dungeons);            
            return;
        }
        for(int i=0;i<n;i++)
        {
            if(isvisit[i]==1)
                continue;
            isselected[cnt]=i;
            isvisit[i]=1;
            perm(cnt+1,n,k,dungeons);
            isvisit[i]=0;            
        }
        
        
    }
    
    
    
    public int solution(int k, int[][] dungeons) {
        
        isselected=new int[dungeons.length];
        isvisit=new int[dungeons.length];
        //던전을 최대한 많이 탐험 하고자 한다
        //던전 탐험 계획을 조합 으로 만들어서 하면 되겠다
        perm(0,dungeons.length,k,dungeons);
        
        
        return answer;
    }
}