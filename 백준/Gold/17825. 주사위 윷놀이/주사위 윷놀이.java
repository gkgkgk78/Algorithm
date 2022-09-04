import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static int numbers[];
	static int li[];
	static int first[] = { 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 100 };
	static int second[] = { 10, 13, 16, 19, 25, 30, 35, 40, 100 };
	static int third[] = { 20, 22, 24, 25, 30, 35, 40, 100 };
	static int four[] = { 30, 28, 27, 26, 25, 30, 35, 40, 100 };
	
	static ArrayList<go> hi;
	static int result = Integer.MIN_VALUE;

	static class go {
		int now, sumz;// 현재 있는 판을 의미함, 그리고 지금까지의 합계를 의미함
		int no;// 번호
		int now_val;// 현재 서있는 크기를 의미
		int now_index;// 현재 ㅅ있는 인덱스

		public go(int no, int now, int sumz, int now_val, int now_index) {
			this.now = now;
			this.no = no;
			this.sumz = sumz;
			this.now_val = now_val;
			this.now_index = now_index;
		}

	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer s = new StringTokenizer(in.readLine(), " ");
		li = new int[10];
		numbers = new int[10];
		for (int i = 0; i < 10; i++) {
			li[i] = Integer.parseInt(s.nextToken());
		}
		perm(0);
		System.out.println(result);

	}

	private static void perm(int cnt) {
		// TODO Auto-generated method stub
		if (cnt == 10) {
			// System.out.println(Arrays.toString(numbers));
			// 이제 이렇게 해서 진행을 해보도록 하자구

			game();

			return;
		}
		for (int i = 0; i < 4; i++) {
			numbers[cnt] = i;
			perm(cnt + 1);
		}

	}

	private static void game() {
		// TODO Auto-generated method stub
		int sum = 0;
		hi = new ArrayList<>();
		for (int i = 0; i < 4; i++) {
			hi.add(new go(i, 0, 0, 0, 0));
		} // 이렇게 해서 게임을 시작하도록 하지
		for (int i = 0; i < 10; i++) {
			int a = numbers[i];// 움직일순서를 의미
			go temp = hi.get(a);// 이제 움직을 말을 의미함
			if(temp.now_val==100)
				return;
			if (temp.now_val == 10) {
				temp.now = 1;
				temp.now_index = 0;
			} else if (temp.now_val == 20) {
				temp.now = 2;
				temp.now_index = 0;
			} else if (temp.now_val == 30&&temp.now==0) {
				temp.now = 3;
				temp.now_index = 0;
			}
			int u = move(temp, li[i]);
			if (u == -1)
				return;
		}
		int su = 0;
		for (go ii : hi) {
			su += ii.sumz;
		}
		
		if (result < su) {
			result = su;
		}
	}

	private static int move(go temp, int i) {
		// TODO Auto-generated method stub
		temp.now_index = temp.now_index + i;
		int u=temp.now_index;
		if (temp.now == 0) {
			if (u < first.length - 1) {
				temp.sumz += first[u];// 합계 갱신
				temp.now_val = first[u];// 현재 서있는 크기를 의미
			} else {
				temp.now_val = 100;
			}

		} else if (temp.now == 1) {
			if (u < second.length - 1) {
				temp.sumz += second[u];// 합계 갱신
				temp.now_val = second[u];// 현재 서있는 크기를 의미
			} else {
				temp.now_val = 100;
			}
		}

		else if (temp.now == 2) {
			if (u < third.length - 1) {
				temp.sumz += third[u];// 합계 갱신
				temp.now_val = third[u];// 현재 서있는 크기를 의미
			} else {
				temp.now_val = 100;
			}
		} else if (temp.now == 3) {
			if (u < four.length - 1) {
				temp.sumz += four[u];// 합계 갱신
				temp.now_val = four[u];// 현재 서있는 크기를 의미
			} else {
				temp.now_val = 100;
			}
		}
		// 모두 다 돌고나서 이제 중복 되는게 있는지 체크를 함
		int uu = temp.no;
		int a1 = temp.now;
		int a2 = temp.now_index;
		int a3=temp.now_val;
		for (go a : hi) {
			int now=a.now;
			int index=a.now_index;
			
			if (uu != a.no) {
				if (a.now_val == 100)
					continue;
				if (now == a1 && index == a2)
					{
						return -1;
					}
				if(a3== a.now_val) {
					
					if(a3==30||a3==25||a3==35) {
						if(a1!=0&&now!=0)
							return -1;
					}
					if(a3==40)
						return -1;
				}
			}
		}

		return 0;
	}

}