import java.util.*;



class Solution {
    
    public void bfs(int start,int[][]computers,int[]visit)
    {
        Queue<Integer>q=new LinkedList<>();
        visit[start]=1;
        q.add(start);
        while(q.size()>0)
        {
            int aa=q.poll();
            for(int i=0;i<computers[0].length;i++)
            {
                if(computers[aa][i]==1 && visit[i]==0)
                {
                    visit[i]=1;
                    q.add(i);
                }
                
            }
                
        }
        
        
    }
    
    
    
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        int visit[]=new int[n];
        for(int i=0;i<n;i++)
        {
            if(visit[i]==0)
            {
                answer+=1;
                bfs(i,computers,visit);
            }
        }
        
        
        
        return answer;
    }
}