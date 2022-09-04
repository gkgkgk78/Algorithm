import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	static StringBuffer buffer;

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		buffer = new StringBuffer();
		// 모음이 하나 나왔으면 그 뒤 두개의 문자를 지우면 되겠네
		char[] s = in.readLine().toCharArray();// 예시를 입력받아 문자열 배열로 전환!
		// System.out.println(Arrays.toString(s));
		for (int i = 0; i < s.length; i++)// 길이만큼 순회 하면서 탐색을 진행
		{
			if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u')// 모음에 해당되는 문자들이 존재할경우
			{
				s[i + 1] = '-';// 해당 문자 뒤에 p
				s[i + 2] = '-';// 해당 문자 뒤 뒤에 모음이 추가 되었으니 -표시로 바꿔줌
			}
		}
		// System.out.println(Arrays.toString(s));
		for (int i = 0; i < s.length; i++) {
			if (s[i] != '-')// -표시가 된부분은 없어진 부분이라 판단을 하고 답에 포함시키지 않음
				buffer.append(s[i]);
		}
		System.out.println(buffer);// 최종 결과 출력

	}

}