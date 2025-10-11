import java.util.*;

class Solution {
    
    static Set<Integer>list=new HashSet<>();
    static int[]visit;
    static int[]isSelected;


    public void perm(String number,int cnt,int last){
    
        if (cnt==last){
            
            String temp="";
            for(int i=0;i<isSelected.length;i++){
                temp+=number.charAt(isSelected[i]);
            }
            int now=Integer.parseInt(temp);
            list.add(now);
            return;
        }
        
        for(int i=0;i<number.length();i++){
            if(visit[i]==1)
                continue;
            visit[i]=1;
            isSelected[cnt]=i;
            perm(number,cnt+1,last);
            visit[i]=0;
        }
    }
    
    
    public int check(int now){
        
        if(now<2)
            return 0;
        if(now==2)
            return 1;
        for(int i=2;i<=Math.sqrt(now);i++){
            if(now%i==0)
                return 0;
        }
        return 1;        
        
        
    }
    
    
    public int solution(String numbers) {
        int answer = 0;
        
        for(int i=1;i<=numbers.length();i++){
            //1부터 n까지 순열 조합 구하기
            visit=new int[numbers.length()];
            isSelected=new int[i];
            perm(numbers,0,i);
                
        }
        
        for(int i: list){
            answer+=check(i);
        }
        
        
        
        
        
        
        return answer;
    }
}