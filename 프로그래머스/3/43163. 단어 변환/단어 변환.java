class Solution {
    static int answer=0;
    
    public int check(String s1, String s2){
        
        int check=0;
        for(int i=0;i<s1.length();i++){
            if(s1.charAt(i)!=(s2.charAt(i)))
                check+=1;
        }
        return check;
    }
    
    
    public void dfs(String begin, String target, String[] words, int[] visit,int now,int count){
            if(begin.equals(target)){
                if(count<answer || answer==0)
                    answer=count;
                return ;
            }
        
        
          for(int i=0;i<words.length;i++){
            if(visit[i]==1)
                continue;
            int check=check(begin,words[i]);
            if (check==1){
                visit[i]=1;
                dfs(words[i],target,words,visit,i,count+1);
            
                visit[i]=0;
            }
        }
       
        
        
    }
    
    
    
    public int solution(String begin, String target, String[] words) {
        
        for(int i=0;i<words.length;i++){
            int check=check(begin,words[i]);
            if (check==1){
                int[] visit=new int[words.length];
                visit[i]=1;
                dfs(words[i],target,words,visit,i,1);
            }
        }
        return answer;
    }
}