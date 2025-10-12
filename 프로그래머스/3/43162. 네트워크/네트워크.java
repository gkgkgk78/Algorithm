import java.util.*;
class Solution {
    
    static List<List<Integer>>list=new ArrayList<>();
    
    public void bfs(int[]visit,int start){
        visit[start]=1;
        Deque<Integer>q=new ArrayDeque<>();
        q.add(start);
        while(!q.isEmpty()){
            int now=q.poll();
            for(int i: list.get(now)){
                if(visit[i]==1)
                    continue;
                visit[i]=1;
                q.add(i);   
            }            
        }     
    }
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        for(int i=0;i<n;i++){
            list.add(new ArrayList<>());
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(i==j||computers[i][j]==0)
                    continue;
                list.get(i).add(j);
            }
        }
        int[]visit=new int[n];
        for(int i=0;i<n;i++){
            if(visit[i]==0){
                bfs(visit,i);
                answer+=1;
            }
        }
        
        
        return answer;
    }
}