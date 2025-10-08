import java.util.*;
class Solution {
    
    public class go{
        int index;
        int count;
        go(int index,int count){
            this.index=index;
            this.count=count;
        }
    }
    public class first{
        String name;
        int count;
        first(String name,int count){
            this.name=name;
            this.count=count;
        }
    }
    
    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};
        HashMap<String,Integer> sum=new HashMap<>();
        HashMap<String,List<go>>total=new HashMap<>();
        
        for(int i=0;i<genres.length;i++){
            String gen=genres[i];
            int now=plays[i];
            if(!sum.containsKey(gen)){
                sum.put(gen,0);
                total.put(gen,new ArrayList<>());
            }  
            sum.put(gen,sum.get(gen)+now);
            total.get(gen).add(new go(i,now));
        }
        List<first>test=new LinkedList<>();
        for(String s:sum.keySet()){
            test.add(new first(s,sum.get(s)));
        }
        test.sort((x,y)->{
            return y.count-x.count;
        });
        List<Integer>last=new LinkedList<>();
        for(first f:test){
            List<go>temp=total.get(f.name);
            temp.sort((x,y)->{
                if(x.count!=y.count)
                    return y.count-x.count;
                return x.index-y.index;
            });
            for(int i=0;i<temp.size();i++){
                if(i>1)
                    break;
                last.add(temp.get(i).index);
            }
        }
        answer=new int[last.size()];
        for(int i=0;i<last.size();i++){
            answer[i]=last.get(i);
        }

        return answer;
    }
}