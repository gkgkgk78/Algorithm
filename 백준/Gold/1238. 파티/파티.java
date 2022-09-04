import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

	static StringBuffer buffer;
	// node를 담은 list 가 있다(정점에 해당됨) 그 정점들을 관리하는 list가 존재
	static List<List<Node>> list, reverselist;
	static int[] dist, reversedist;
	static int INF = 1000000000;
	static int n;

	static class Node implements Comparable<Node> {

		int index;
		int distance;

		public Node(int index, int distance) {
			this.index = index;
			this.distance = distance;
		}

		public int compareTo(Node o) {

			return this.distance - o.distance;
		}

	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub

		

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int m, x;
		StringTokenizer s = new StringTokenizer(in.readLine());
		n = Integer.parseInt(s.nextToken());
		m = Integer.parseInt(s.nextToken());
		x = Integer.parseInt(s.nextToken());

		list = new ArrayList<>();
		reverselist = new ArrayList<>();

		for (int i = 0; i <= n; i++) {
			list.add(new ArrayList<>());
			reverselist.add(new ArrayList<>());
		}
		

		for (int i = 1; i <= m; i++) {
			s = new StringTokenizer(in.readLine());
			int u = Integer.parseInt(s.nextToken());
			int v = Integer.parseInt(s.nextToken());
			int w = Integer.parseInt(s.nextToken());

			list.get(u).add(new Node(v, w));
			reverselist.get(v).add(new Node(u, w));

		}

		int sum=Integer.MIN_VALUE;

		for (int i = 1; i <= n; i++)
		{

			int h1[]=dijkstra(list, i);
			int h2[]=dijkstra(list, x);

			int temp=h1[x]+h2[i];
			//System.out.println(temp);
			if(temp>sum)
				sum=temp;
		}
		//System.out.println();
		//System.out.println(sum);
		System.out.println(sum);
	}

	public static int[] dijkstra(List<List<Node>> list,int start) {

		boolean visited[] = new boolean[n + 1];
		int []distance = new int[n + 1];
		Arrays.fill(distance, INF);

		PriorityQueue<Node> q = new PriorityQueue<>();
		distance[start]=0;
		q.add(new Node(start, 0));/// index 거리

		while (!q.isEmpty()) {
			Node hi = q.poll();
			int index = hi.index;
			int dis = hi.distance;
			if (distance[index] < dis)
				continue;
			for (Node node : list.get(index)) {// 방문한 노드에서 갈수있는데
				// 새로 방문한 곳이 그전보다 더 멀었다면
				if (distance[node.index] > distance[index] + node.distance) {
					distance[node.index] = distance[index] + node.distance;
					q.add(new Node(node.index, distance[node.index]));

				}

			}

		}
		
		return distance;

	}

}