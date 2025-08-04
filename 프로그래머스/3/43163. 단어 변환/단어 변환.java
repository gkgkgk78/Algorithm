import java.util.*;

class Solution {
    
    static int answer=Integer.MAX_VALUE;
    public boolean check(String a,String b){
        int count=0;
        for(int i=0;i<a.length();i++){
            if(a.charAt(i)!=b.charAt(i))
                count+=1;
        }
        if(count==1)
            return true;
        return false;
    }
    public void dfs(String now, String target, String[] words,int visit[],int count){
        if(now.equals(target)){
            answer=Math.min(answer,count);
            return;
        }
        for(int i=0;i<words.length;i++){
            if(visit[i]==0&&check(now,words[i])){
                visit[i]=1;
                dfs(words[i],target,words,visit,count+1);
                visit[i]=0;
            }
        }
    }
    
    
    
    
    public int solution(String begin, String target, String[] words) {
        //begin 에서 target어 변환하는 가장 짧은 과정을 찾고자 한다
        int count=0;
        for(String s : words){
            if(target.equals(s))
                count+=1;
        }
        if(count==0)
            return 0;
        int visit[]=new int[words.length];
        for(int i=0;i<words.length;i++){
            if(check(begin,words[i])){
                visit[i]=1;
                dfs(words[i],  target,  words,visit,1);
                visit[i]=0;
            }
        }
        if(answer==Integer.MAX_VALUE)
            return 0;
        return answer;
    }
}