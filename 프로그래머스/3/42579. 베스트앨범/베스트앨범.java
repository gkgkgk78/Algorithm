import java.util.*;

class go{
    String name;
    int plays;
    int num;
    public go(String name,int plays,int num){
        this.name=name;
        this.plays=plays;
        this.num=num;
    }
}
class check{
    String name;
    int count;
    public check(String name, int count){
        this.name=name;
        this.count=count;
    }
}


class Solution {
    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};
        //장르별로 가장 많이 재생된 노래를 두개씩 모아 베스트 앨범을 출시 한다
        HashMap<String,Integer>genre_count=new HashMap<>();
        HashMap<String,List<go>>genre=new HashMap<>();
        for(int i=0;i<genres.length;i++){
            if(!genre_count.containsKey(genres[i])){
                genre_count.put(genres[i],plays[i]);
                List<go>list=new LinkedList<>();
                list.add(new go(genres[i],plays[i],i));
                genre.put(genres[i],list);
            }
            else{
                genre_count.put(genres[i],genre_count.get(genres[i])+plays[i]);
                List<go> list=genre.get(genres[i]);
                list.add(new go(genres[i],plays[i],i));
                genre.put(genres[i],list);
            }
        }
        //속한 노래가 많이 재생된 장르를 먼저 수록 한다.
        List<check>check_list=new LinkedList<>();
        for(String s:genre_count.keySet()){
            check_list.add(new check(s,genre_count.get(s)));
        }
        check_list.sort((x,y)->{
            return y.count-x.count;            
        });
        List<Integer>last=new LinkedList<>();
        for(check s:check_list){
            List<go> now=genre.get(s.name);
            now.sort((x,y)->{
                if(x.plays!=y.plays)
                    return y.plays-x.plays;
                else
                    return x.num-y.num;
            });
            for(int i=0;i<now.size();i++){
                last.add(now.get(i).num);
                if(i==1)
                    break;
            }
        }
        answer=new int[last.size()];
        for(int i=0;i<last.size();i++)
            answer[i]=last.get(i);
       
        
        
        
        
        return answer;
    }
}