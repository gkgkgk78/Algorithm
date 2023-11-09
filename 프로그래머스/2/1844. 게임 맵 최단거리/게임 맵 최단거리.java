import java.util.*;



class Solution {
    
    public class go{
        int x,y,count;
        
        public go(int x,int y, int count)
        {
            this.x=x;
            this.y=y;
            this.count=count;
        }
        
    }
    
    
    
    
    public int bfs(int [][]graph){
        Queue<go>q=new LinkedList<>();
        int [][]visit=new int[graph.length][graph[0].length];
        int answer=-1;
        visit[0][0]=1;
        q.add(new go(0,0,1));
        int n=graph.length;
        int m=graph[0].length;
        int dx[]={-1,0,1,0};
        int dy[]={0,1,0,-1};
        while(q.size()>0)
        {
            go a=q.poll();
            if (a.x==n-1 &&a.y==m-1)
            {
                return a.count;
            }
            for(int i=0;i<4;i++)
            {
                int zx,zy;
                zx=dx[i]+a.x;
                zy=dy[i]+a.y;
                if(0<=zx && zx<n && 0<=zy && zy<m)
                {
                    if(graph[zx][zy]==1 &&visit[zx][zy]==0)
                    {
                        visit[zx][zy]=1;
                        q.add(new go(zx,zy,a.count+1));
                    }
                }
            }
        
        }
        
        
        
        
        
        
        return answer;
    }
    
    
    
    public int solution(int[][] maps) {
        int answer = 0;
        answer=bfs(maps);
        
        
        return answer;
    }
}