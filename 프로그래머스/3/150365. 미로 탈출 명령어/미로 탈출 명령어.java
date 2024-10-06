import java.util.*;

class Solution {
    static String answer="";
    class go{
        int x,y,count;
        String s;
        public go(int x, int y, int check,String s){
            this.x=x;
            this.y=y;
            this.count=check;
            this.s=s;
        }
    }
    
    public int check(int x, int y, int r, int c){
        
        int temp=Math.abs(r-x)+Math.abs(c-y);
        
        return temp;
    }
    
    
    public String dfs(int n, int m, int x, int y, int r, int c, int k,String s){
        
            if(answer.length()>0)
                return answer;
            int zx=x;
            int zy=y;
            if(zx==r&&zy==c&&k==0){
                answer=s;
                return answer;
            }
            //d
            if(zx+1<=n&&zy<=m){
                int temp=check(zx+1,zy,r,c);
                if(k>=temp&&(temp%2==(k-1)%2)){
                    dfs(n,m,zx+1,zy,r,c,k-1,s+"d");
                }
                if(answer.length()>0)
                    return answer;
            }
            //l
            if(zx<=n&&zy-1>=1){
                int temp=check(zx,zy-1,r,c);
                if(k>=temp&&(temp%2==(k-1)%2)){
                    dfs(n,m,zx,zy-1,r,c,k-1,s+"l");
                }
                if(answer.length()>0)
                    return answer;
            }
            
            //r
            if(zx<=n&&zy+1<=m){
                int temp=check(zx,zy+1,r,c);
                if(k>=temp&&(temp%2==(k-1)%2)){
                    dfs(n,m,zx,zy+1,r,c,k-1,s+"r");
                }
                if(answer.length()>0)
                    return answer;
            }
            
            //u
            if(zx-1>=1&&zy>=1&&zy<=m){
                int temp=check(zx-1,zy,r,c);
                if(k>=temp&&(temp%2==(k-1)%2)){
                    dfs(n,m,zx-1,zy,r,c,k-1,s+"u");
                }
                if(answer.length()>0)
                    return answer;
            }
        
        return answer;
    }
    
    
    
    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        answer=dfs(n,m,x,y,r,c,k,"");
        if (answer.length()==0){
            answer="impossible";
        }
        return answer;
    }
    
    
}