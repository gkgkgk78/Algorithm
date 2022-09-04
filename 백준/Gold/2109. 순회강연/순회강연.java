import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
	static class go implements Comparable<go>{
		int day,pay;

		public go(int pay, int day) {
			this.day = day;
			this.pay = pay;
		}

		@Override
		public int compareTo(go o) {
			// TODO Auto-generated method stub
			return Integer.compare( o.pay,this.pay);
		}
		
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader in=new BufferedReader(new InputStreamReader(System.in));
		//d일 p만큼의 강연료 를 지불하라
		//학자는 이를 바탕으로 가장 많은 돈을 벌수 있도록 순회강연을 하려 한다.
		//네 대학에서 제시한 p값이 각각 
		int n=Integer.parseInt(in.readLine());
		ArrayList<go>hi=new ArrayList<>();
		for(int i=0;i<n;i++) {
			StringTokenizer s=new StringTokenizer(in.readLine()," ");
			hi.add(new go(Integer.parseInt(s.nextToken()),Integer.parseInt(s.nextToken())));
		}
		Collections.sort(hi);
		int ma=Integer.MIN_VALUE;
		
		int visit[]=new int[10001];
		
		int day=-1;
		int temp=0;
		int price=0;
		for(int i=0;i<hi.size();i++) {
			go a=hi.get(i);
			if(i==0) {
				visit[a.day]=a.pay;
			}
			else {
				int check=a.day;
				for(int j=check;j>=1;j--) {
					if(visit[j]==0) {
						visit[j]=a.pay;
						break;
					}
				}
			}
		}
		for(int i=1;i<=10000;i++) {
			//System.out.print(visit[i]+" ");
			if(visit[i]>0)
				price+=visit[i];
		}
		
		
		System.out.println(price);
		
	}

}