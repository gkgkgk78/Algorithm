import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

	static int result;
	static int  dx[] = { -1, -1, 0, 1, 1, 1, 0, -1 };
	static int dy[] = { 0, -1, -1, -1, 0, 1, 1, 1 };
	static int graph[][];

	static class shark {

		int x, y, dir, num;
		int alive;

		public shark() {
			super();
		}

		public shark(int x, int y, int dir, int num, int alive) {
			super();
			this.x = x;
			this.y = y;
			this.dir = dir;
			this.num = num;
			this.alive = alive; // 1이면은 산거 0이면은 죽은거를 의미함

		}

	}

	// 만약에 교차가 되는것을 완전탐색으로 푼다면?
	static shark fish[];

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		// 먹을수 있는 물고기 번호의 최댓 값을 구해야함
		graph = new int[4][4];
		fish = new shark[17];// 여기에다가 다 넣어줄거임
		// 근데 어차피 16개라고는 하지만.....
		// 그래도 복사를 해야 맘이 편할듯 한데
		result = Integer.MIN_VALUE;

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		// 모든 입력 처리를 함
		for (int i = 0; i < 4; i++) {
			StringTokenizer s = new StringTokenizer(in.readLine(), " ");
			int count = 0;
			for (int j = 0; j < 4; j++) {
				int a1, a2;
				a1 = Integer.parseInt(s.nextToken());
				a2 = Integer.parseInt(s.nextToken());

				a2--;
				
				graph[i][j] = a1;
				fish[a1] = new shark(i, count, a2, a1, 1);
				count++;
			}
		}

		int temp = graph[0][0];
		shark first = new shark(0, 0, fish[temp].dir, -1, 1);
		// -1이면 상어를 의미함
		graph[0][0] = -1;
		fish[temp].alive = 0;
		game(first, graph, temp,fish);
		// dir 은 : ↑0, ↖1, ←2, ↙3, ↓4, ↘5, → 6, ↗7
				// 0: x,y-1 1: x-1,y-1 2:x,y-1 3:x+1,y-1
				// 4: x+1,y 5:x+1,y+1 6:x,y+1 7: x-1,y+1
//		for (int i = 1; i <= 16; i++) {
//			System.out.println(fish[i].x+" "+fish[i].y+" "+fish[i].num+" "+fish[i].dir);
//		}
		System.out.println(result);

	}

	private static void game(shark shark, int[][] graph2, int score, shark[] fish2) {
		// TODO Auto-generated method stub

		// 가장 처음은 0,0으로 상어가 들어옴
		// 상어가 들어옴 물고기를 먹고 들어감
		// 이후 물고기가 이동을 하고
		result = Math.max(score, result);
		
		int x, y;
		x = shark.x;
		y = shark.y;

		// 물고기 이동을 하자
		movefish(graph2,fish2);
		

		int zx = x + dx[shark.dir];
		int zy = y + dy[shark.dir];

		if (zx < 0 || zx >= 4 || zy < 0 || zy > 4) {
			return;
		}

		// 상어가 이동을 함
		// 상어가 이동 가능한 모든곳 다 탐색후 정리 하면됨
		// 복사를 해서 이동 가능한 경로가 있을시 넘겨 주도록 하자
		int count = 0;
		while (zx >= 0 && zx < 4 && zy >= 0 && zy < 4) {
			if (graph2[zx][zy]!=0) {
				//상어가 잡아먹는 것을 의미함
				int[][] tgraph = new int[4][4];
				for (int i = 0; i < 4; i++) {
					for (int j = 0; j < 4; j++) {
						tgraph[i][j] = graph2[i][j];
					}
				}
				shark fishz[]=new shark[17];
				for(int i=1;i<=16;i++) {
					shark s2=fish2[i];
					fishz[i]=new shark(s2.x, s2.y, s2.dir, s2.num, s2.alive);
				}
				// 이때 dfs를 하면됨
				// 상어를 잡아먹고 어레이 리스트에서 지워주고 상어를 옮기고 dfs
				// 상어를잡아먹고 지워지고 상어를 그자리에 옮긴후에 dfs를 실행
				tgraph[shark.x][shark.y]=0;
				shark temps = new shark(zx, zy, shark.dir, shark.num, shark.alive);
				temps.dir = fishz[tgraph[zx][zy]].dir;
				shark zz=fishz[tgraph[zx][zy]];
				zz.alive=zz.alive;
				fishz[tgraph[zx][zy]].alive=0;
				shark.num=tgraph[zx][zy];
				int score2=score;
				score2 += tgraph[zx][zy];
				tgraph[zx][zy] = -1;
				game(temps, tgraph, score2, fishz);
				
				// 값을 더해주고
				// 상어를 어레이리스트에서 지워줌
				count++;
			}

			zx = zx + dx[shark.dir];
			zy = zy + dy[shark.dir];

		}


	}

	private static void movefish(int[][] graph, shark[] fish2) {
		// TODO Auto-generated method stub
		// dir 은 : ↑0, ↖1, ←2, ↙3, ↓4, ↘5, → 6, ↗7
		// 0: x,y-1 1: x-1,y-1 2:x,y-1 3:x+1,y-1
		// 4: x+1,y 5:x+1,y+1 6:x,y+1 7: x-1,y+1
		int dx[] = { -1, -1, 0, 1, 1, 1, 0, -1 };
		int dy[] = { 0, -1, -1, -1, 0, 1, 1, 1 };
		for (int i = 1; i <= 16; i++) {
//			System.out.println(i);
//			for (int i1 = 0; i1 < 4; i1++) {
//				System.out.println(Arrays.toString(graph[i1]));
//			}
//			System.out.println();
			shark s = fish2[i];
			if (s.alive == 0)
				continue;

			int x, y;
			x = s.x;
			y = s.y;
			int dir = s.dir;
			int count = 0;
			int next = 0;

			while (count < 9) {
				int zx = x + dx[dir];
				int zy = y + dy[dir];
				if (0 <= zx && zx < 4 && 0 <= zy && zy < 4 && graph[zx][zy] != -1) {
					// 이때는 이동 가능한 상태이므로 이동을 해주면 되고
					if (graph[zx][zy] == 0) {
						graph[zx][zy] = s.num;
						graph[x][y] = 0;// 그전 그래프 비워줌
						s.x = zx;
						s.y = zy;
						s.dir = dir;
						fish2[s.num].x = zx;
						fish2[s.num].y = zy;
					} else {

						// 이때는 그래프 서로 변경을 해주면됨
						int temp = graph[x][y];
						shark temps = fish2[graph[zx][zy]];
						graph[x][y] = graph[zx][zy];
						graph[zx][zy] = temp;						
						
						s.x = zx;
						s.y = zy;
						s.dir = dir;
						//System.out.println(s.num);
						fish2[s.num].x = zx;
						fish2[s.num].y = zy;						
						temps.x=x;
						temps.y=y;	
						
						break;
					}
					break;
				} else {
					dir++;
				}
				if (dir == 8)
					dir = 0;
			}

		}

	}

}