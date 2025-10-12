import java.util.*;
class Solution {
    
    static List<List<Integer>>graph=new ArrayList<>();
    public void bfs(int[] visit,int start,int v1,int v2,int flag){
        
        Deque<Integer>q=new ArrayDeque<>();
        visit[start]=flag;
        q.add(start);
        while(!q.isEmpty()){
            int now=q.poll();
            for(int i : graph.get(now)){
                if(visit[i]!=0)
                    continue;
                if((now==v1&&i==v2)||(now==v2&&i==v1))
                    continue;
                visit[i]=flag;
                q.add(i);
            }
        }
    }
    
    public int solution(int n, int[][] wires) {
        int answer = 1000;
        //전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷 하도록 두 전력망 나누도록 하자
        for (int i=0;i<=n;i++){
            graph.add(new ArrayList<>());
        }
        
        for(int i=0;i<wires.length;i++){
            int v1=wires[i][0];
            int v2=wires[i][1];
            graph.get(v1).add(v2);
            graph.get(v2).add(v1);
        }
        
        for(int i=0;i<wires.length;i++){
            int v1=wires[i][0];
            int v2=wires[i][1];
            int[]visit=new int[n+1];
            int temp=1;
            for(int j=1;j<=n;j++){
                if (visit[j]==0){
                    bfs(visit,j,v1,v2,temp);
                    temp+=1;
                }
            }
            int left=0;
            int right=0;
            for(int j=1;j<=n;j++){
                if(visit[j]==1){
                    left+=1;
                }
                else{
                    right+=1;
                }
            }
            answer=Math.min(answer,Math.abs(left-right));
        }
        
        return answer;
    }
}