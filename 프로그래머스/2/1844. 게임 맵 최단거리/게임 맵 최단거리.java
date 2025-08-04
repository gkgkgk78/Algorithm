import java.util.*;

class Solution {
    
    public class go{
        int x,y;
        go(int x, int y){
            this.x=x;
            this.y=y;
        }
    }
    
    
    public int bfs(int[][]maps){
        int dx[]={-1,0,1,0};
        int dy[]={0,1,0,-1};
        int n=maps.length;
        int m=maps[0].length;
        int visit[][]=new int[n][m];
        Deque<go>q=new LinkedList<>();
        q.add(new go(0,0));
        visit[0][0]=1;
        while(!q.isEmpty()){
            go a=q.poll();
            int now=visit[a.x][a.y];
            for(int i=0;i<4;i++){
                int zx=dx[i]+a.x;
                int zy=dy[i]+a.y;
                if(0<=zx&&zx<n &&0<=zy&&zy<m){
                    if (visit[zx][zy]!=0 || maps[zx][zy]==0)continue;
                    visit[zx][zy]=now+1;
                    if(zx==n-1 &&zy==m-1)
                        return now+1;
                    q.add(new go(zx,zy));
                }
            }
        }
        
        return -1;
    }
    
    
    public int solution(int[][] maps) {
        int answer = 0;
        //상대팀 진영에 최대한 빨리 도착 하도록 하
        
        answer=bfs(maps);
        
        return answer;
    }
}