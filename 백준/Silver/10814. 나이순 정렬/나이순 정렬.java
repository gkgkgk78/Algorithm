import java.util.*;
import java.io.*;

class Student {

    String name;
    int age;
    int order;

    public Student(int s2, String s1, int s3) {
        this.name = s1;
        this.age = s2;
        this.order = s3;
    }
}


public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s;


        s = new StringTokenizer(in.readLine(), " ");
        int n = Integer.parseInt(s.nextToken());
        List<Student> list = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            String s2;
            int s1;
            s = new StringTokenizer(in.readLine(), " ");
            s1 = Integer.parseInt(s.nextToken());
            s2 = s.nextToken();
            list.add(new Student(s1, s2, i));
        }
        list.sort((x, y) -> {
            if (x.age != y.age)
                return x.age - y.age;
            return x.order - y.order;
        });
        for (Student ss : list) {
            System.out.println(ss.age + " " + ss.name);
        }


    }
}