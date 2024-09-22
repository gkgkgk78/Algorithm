import java.util.*;
class Solution {
    
    public void bfs(int []visit,int[][]computers,int vertex,int n){
        Deque<Integer>q=new LinkedList<>();
        visit[vertex]=1;
        q.add(vertex);
        while(!q.isEmpty()){
            Integer now=q.poll();
            for (int i=0;i<n;i++){
                if(computers[now][i]==1 && visit[i]==0){
                    visit[i]=1;
                    q.add(i);
                }
            }
        }
        
    }
    
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        int visit[]=new int[n];
        for(int i=0;i<n;i++){
            if(visit[i]==0){
                answer+=1;
                bfs(visit,computers,i,n);
            }
        }
        
        return answer;
    }
    
    
    
    
}