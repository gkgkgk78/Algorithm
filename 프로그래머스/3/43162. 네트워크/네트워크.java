import java.util.*;

class Solution {
    
    static int visit[];
    
    public void bfs(int start,int n, int[][]computers){
        
        Deque<Integer>queue=new LinkedList<>();
        visit[start]=1;
        queue.add(start);
        while(!queue.isEmpty()){
            int now=queue.poll();
            for(int i=0;i<computers[now].length;i++){
                int temp=computers[now][i];
                if(temp==1&&visit[i]==0){
                    visit[i]=1;
                    queue.add(i);
                    // System.out.println(Arrays.toString(visit));
                }
            }
        }
        
    }
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visit=new int[n];
        for(int i=0;i<n;i++){
            if(visit[i]==1)
                continue;
            bfs(i,n,computers);    
            answer+=1;
        }
        
        return answer;
    }
}