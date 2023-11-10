import java.util.*;
class Solution {
    static int answer=0;
    static HashMap<Integer,Integer> map=new HashMap<>();
    public int check(int now)
    {
        if(now<2)
            return 0;
        for(int i=2;i<(int)Math.sqrt(now)+1;i++){
            if(now%i==0)
                return 0;
        }
    
        return 1;
    }
    
    
    
    public void perm(int cnt, int [] isvisit,int [] isselected,char[]temp)
    {  
        if(cnt==isselected.length)
        {
            String aa="";
            for(int i=0;i<isselected.length;i++){
                //System.out.print(isselected[i]);
                aa+=String.valueOf(temp[isselected[i]]);
            }
            //System.out.println(aa);
            if(map.containsKey(Integer.valueOf(aa)))
            {
                return;
            }
            
            int a1=check(Integer.valueOf(aa));
            
            //소수 판별 하기
            if (a1==1){
                answer+=1;
                map.put(Integer.valueOf(aa),1);
                System.out.println(Integer.valueOf(aa));
            }
            return;
        }
        for(int i=0;i<isvisit.length;i++)
        {
            if(isvisit[i]==0)
            {
                isvisit[i]=1;
                isselected[cnt]=i;
                perm(cnt+1,isvisit,isselected,temp);
                isvisit[i]=0;
            }
        }
        
        
    }
    
    
    
    public int solution(String numbers) {
        
        char [] temp=numbers.toCharArray();
        //완전 탐색을 진행 하게 될건데
        for(int i=1;i<=temp.length;i++)
        {
            int []isvisit=new int[temp.length];
            int [] isselected=new int[i];
            perm(0,isvisit,isselected,temp);
        }
        
        
        
        
        return answer;
    }
}