package java8.lambda2;

import java.util.stream.IntStream;

public class Example3 {

	public static void main(String[] args) {

		// Parallelの例
		IntStream.rangeClosed(1, 10).parallel().forEach(System.out::println);
		
	}

}
