import java.util.*;
class Solution {
    
    public class go{
        
        int x,y,size;
        public go(int x, int y, int size){
            this.x=x;
            this.y=y;
            this.size=size;
        }
        
        
    }
    
    
    public int bfs(int [][]maps){
     
        PriorityQueue<go>q=new PriorityQueue<>((x,y)->{
            return x.size-y.size;
        });
        int n=maps.length;
        int m=maps[0].length;
        int visit[][]=new int[maps.length][maps[0].length];
        q.add(new go(0,0,1));
        visit[0][0]=1;
        int dx[]={-1,0,1,0};
        int dy[]={0,1,0,-1};
        while(!q.isEmpty()){
            go now=q.poll();
            if(now.x==n-1 && now.y==m-1)
                continue;
            for(int i=0;i<4;i++){
                int zx=dx[i]+now.x;
                int zy=dy[i]+now.y;
                if (0<=zx&&zx<n &&0<=zy&&zy<m &&maps[zx][zy]==1){
                    if(visit[zx][zy]==0){
                        visit[zx][zy]=now.size+1;
                        q.add(new go(zx,zy,now.size+1));
                    }
                    else{
                        if(now.size+1<visit[zx][zy]){
                            visit[zx][zy]=now.size+1;
                            q.add(new go(zx,zy,now.size+1));
                        }
                    }
                }
            }
            
        }
        if(visit[n-1][m-1]==0)
            return -1;
        return visit[n-1][m-1];
    }
    
    
    
    public int solution(int[][] maps) {
        int answer = 0;
        return bfs(maps);
    }
    
}