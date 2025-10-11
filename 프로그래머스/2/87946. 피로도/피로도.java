import java.util.*;
class Solution {
    
    static int answer=-1;
    static int []visit,isSelected;
    
    public void game(int k, int[][]dungeons){
        
        int temp=0;
        int tempK=k;
        for(int i : isSelected){
            int first=dungeons[i][0];
            int second=dungeons[i][1];
            if(tempK>=first){
                tempK-=second;
                temp+=1;
            }
            else{
                answer=Math.max(answer,temp);
                return;
            }
        }
        answer=Math.max(answer,temp);
    }
    
    
    public void make(int k, int[][]dungeons,int cnt){
        int n=dungeons.length;
        if(cnt==n){
            game(k,dungeons);
            return;
        }
        for(int i=0;i<n;i++){
            if(visit[i]==1)
                continue;
            visit[i]=1;
            isSelected[cnt]=i;
            make(k,dungeons,cnt+1);
            visit[i]=0;
            
        }
        
    }
    
    
    
    public int solution(int k, int[][] dungeons) {
        
        visit=new int[dungeons.length];
        isSelected=new int[dungeons.length];
        make(k,dungeons,0);
        
        
        
        return answer;
    }
}