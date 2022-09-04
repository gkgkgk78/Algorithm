import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

	static int visit[][];
	static int s;
	static class go{
		int x,y,time;
		public go(int x, int y,int time) {
			this.x = x;
			this.y = y;
			this.time=time;
			
		}
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub

		BufferedReader in=new BufferedReader(new InputStreamReader(System.in));
		
		s=Integer.parseInt(in.readLine());
		visit=new int[1001][1001];

		bfs(1,0,0);//화면 이모티콘 수를 의미함
	}

	private static void bfs(int dis, int emo,int time) {
		// TODO Auto-generated method stub
		Queue<go> q=new LinkedList<>();
		visit[1][0]=1;
		q.add(new go(dis,emo,time));
		
		while(!q.isEmpty()) {

			go a=q.poll();

			if(a.x==s)
			{
				System.out.println(a.time);
				System.exit(0);
			}
			if(a.x<s&&visit[a.x][a.x]==0)
			{
				visit[a.x][a.x]=1;
				q.add(new go(a.x,a.x,a.time+1));
			}
			if(a.y>0&&a.x+a.y<=s&&visit[a.x+a.y][a.y]==0)
			{
				if(a.x+a.y==s)
				{
					System.out.println(a.time+1);
					System.exit(0);
				}
				visit[a.x+a.y][a.y]=1;
				q.add(new go(a.x+a.y,a.y,a.time+1));
			}
			if(a.x>0&&visit[a.x-1][a.y]==0)
			{
				if(a.x-1==s)
				{
					System.out.println(a.time+1);
					System.exit(0);
				}
				visit[a.x-1][a.y]=1;
				q.add(new go(a.x-1,a.y,a.time+1));
			}
			
			
			
			
			
			
		}
		
		
		
		
		
	}

}