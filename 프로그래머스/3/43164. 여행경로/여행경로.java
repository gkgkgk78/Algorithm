import java.util.*;
class Solution {
    
    static String check="";
    static String[] anan; 
    
    public String make(List<String> sum){
        String now="";
        for (String s:sum){
            now+=s;
        }
        return now;
    }
    public void make_array(List<String> sum){
        
        int now=0;
        for(String s:sum){
            anan[now]=s;
            now+=1;
        }
    }
    
    
    public void dfs(String[][] tickets,int visit[],List<String> sum,String before){
        int temp=0;
        for(int i=0;i<visit.length;i++){
            if(visit[i]==1)
                temp+=1;
        }
        if(temp==visit.length)
        {
            if(check.length()==0)
            {
                check=make(sum);
                make_array(sum);
            }
            else{
                String s1=make(sum);
                if(s1.compareTo(check)<0){
                    check=s1;
                    make_array(sum);
                }
            }
            return;
        }
        
        for(int i=0;i<tickets.length;i++){
            if(visit[i]==0){
                String s1=tickets[i][0];
                if(before.equals(s1)){
                    visit[i]=1;
                    sum.add(tickets[i][1]);
                    dfs(tickets,visit,sum,tickets[i][1]);
                    visit[i]=0;
                    sum.remove(sum.size() - 1);
                }  
            }
        }    
        
    }
    


    
    public String[] solution(String[][] tickets) {
        String[] answer = {};
        anan=new String[tickets.length+1];
        for(int i=0;i<tickets.length;i++){
            int visit[]=new int[tickets.length];
            String s1=tickets[i][0];
            List<String>an=new LinkedList<>();
            if(s1.equals("ICN")){
                visit[i]=1;
                an.add("ICN");
                an.add(tickets[i][1]);
                dfs(tickets,visit,an,tickets[i][1]);
            }  
            
        }
        
        
        
        return anan;
    }
    
}