import java.util.*;
class Solution {
    class go{
        int x,y;
        public go(int x, int y){
            this.x=x;
            this.y=y;
        }
    }
    
    
    
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        //중앙에는 노란색, 테두리 1줄은 갈색으로 칠해져 있음
        List<go>list=new ArrayList<>();
        for(int i=1;i<=Math.sqrt(yellow);i++){
            if(yellow%i!=0)
                continue;
            int bo=i;
            int up=yellow/bo;
            int total=(bo+2)*2+up*2;
            if(total==brown){
                bo+=2;
                up+=2;
                if(bo>=up)
                    return new int[] {bo,up};
                else
                    return new int[]{up,bo};
            }
        }
        
        
        
        
        return answer;
    }
}