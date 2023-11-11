import java.util.*;

class Solution {
    
    public static class go{
        int vertex;
        public go(int vertex){
            this.vertex=vertex;
        }    
    }
    
    static int answer=99999;
    static List<List<go>> list=new LinkedList<>();
    
    
    public static void bfs(int start, int[]visit,int x1,int x2,int count)
    {
        Queue<go>q=new LinkedList<>();
        visit[start]=count;
        q.add(new go(start));
        while(q.size()>0){
            go aa=q.poll();
            List<go> now=list.get(aa.vertex);
            for(go a1:now){
                if(aa.vertex==x1 &&a1.vertex==x2 )
                    continue;
                if(aa.vertex==x2 &&a1.vertex==x1 )
                    continue;
                if(visit[a1.vertex]==0)
                {
                    visit[a1.vertex]=count;
                    q.add(new go(a1.vertex));
                }
            }      
        }
    }
    
    
    public int solution(int n, int[][] wires) {
        
        for(int i=0;i<=n;i++)
            list.add(new LinkedList<>());
        for(int i=0;i<wires.length;i++)
        {
            int a1,a2;
            a1=wires[i][0];
            a2=wires[i][1];
            list.get(a1).add(new go(a2));
            list.get(a2).add(new go(a1));
        }
        
        for(int i=0;i<wires.length;i++)
        {
            int visit[]=new int[n+1];
            int a1,a2;
            a1=wires[i][0];
            a2=wires[i][1];
            //다 진행 한 후에 확인을 해보도록 하자, 전력망이 두개로 나뉘었는지
            int count=0;
            for(int j=1;j<=n;j++)
            {
                if(visit[j]==0)
                {
                    count+=1;
                    bfs(j,visit,a1,a2,count);
                }
            }
            if(count==2)
            {
                //이때 이제 갱신을 하도록 하면은 됨
                int x1,x2;
                x1=0;
                x2=0;
                for(int j=1;j<=n;j++)
                {
                    
                    if(visit[j]==1)
                    {
                        x1+=1;
                    }
                    else if(visit[j]==2)
                    {
                        x2+=1;
                    }
                }
                answer=Math.min(answer,Math.abs(x1-x2));
                
            }
            
        }
        
        
        return answer;
    }
}