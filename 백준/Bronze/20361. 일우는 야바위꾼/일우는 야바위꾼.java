import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static StringBuffer buffer;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));// 입력을 진행받는 부분
		
		buffer = new StringBuffer();
		//result=-1;
			StringTokenizer s = new StringTokenizer(in.readLine());//줄단위로 입력받음

			int n, x, k;
			n = Integer.parseInt(s.nextToken());// 각각 입력받은 데이터를 할당해 주는 부분
			x = Integer.parseInt(s.nextToken());// 각각 입력받은 데이터를 할당해 주는 부분
			k = Integer.parseInt(s.nextToken());// 각각 입력받은 데이터를 할당해 주는 부분
			int graph[] = new int[n + 1];

			for (int j = 1; j <= n; j++)// 종이컵의 수에 맞춰 초기화 작업
			{
				graph[j] = j;

			}
			int find = graph[x];// 현재 간식이 들어있는 종이컵을 파악
			int result;
			result=x;//찾을 인덱스
			for (int j = 0; j < k; j++)// k번동안 종이컵의 위치를 변경
			{
				// 입력받은 두 위치에 대하여 변경을 해주는 부분
				s = new StringTokenizer(in.readLine());//줄단위로 입력받음
				int a1 = Integer.parseInt(s.nextToken());// 각각 입력받은 데이터를 할당해 주는 부분
				int a2 = Integer.parseInt(s.nextToken());// 각각 입력받은 데이터를 할당해 주는 부분
				int temp = graph[a2];
				graph[a2] = graph[a1];
				graph[a1] = temp;
				if(graph[a1]==find)//변경된 곳의 값이 같으면 바꿔줌
					result=a1;
				else if(graph[a2]==find)//바로 위와 동일
					result=a2;
			}
//			for (int j = 1; j <= n; j++) {
//				if (graph[j] == find)// 모든 위치 이동이 끝난후 찾아낸 종이컵의 위치를 찾아내 주는 부분
//				{
//					buffer.append("#" + i + " " + j + "\n");
//					break;
//				}
//
//			}
			buffer.append(result + "\n");//변경된 최종 인덱스를 넣어줌

		
		System.out.println(buffer);// 모든 테스트케이스에 대해 출력

	}

}