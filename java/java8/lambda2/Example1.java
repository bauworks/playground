package java8.lambda2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;

public class Example1 {

	public static void main(String[] args) {

		// ベースのArrayList
		final List<String> cities = Arrays.asList("Kyoto", "Osaka", "Kobe");
		cities.forEach(System.out::println);		


		System.out.println("--------------------------------");

		// 普通にfor文を回してtoUpper
		final List<String> uppercaseCities = new ArrayList<String>();
		for(String city : cities) {
			uppercaseCities.add(city.toUpperCase());  // 大文字に変換
		}
		
		for(String city : uppercaseCities) {
			System.out.println(city);                 // 標準出力
		}
		
		
		System.out.println("--------------------------------");

		// ListのforEachで回してConsumerアクション
		final List<String> uppercaseCities2 = new ArrayList<String>();
		cities.forEach(new Consumer<String>() {
			public void accept(final String city) {
				uppercaseCities2.add(city.toUpperCase());
			}
		});
		
		uppercaseCities2.forEach(System.out::println);		
		

		System.out.println("--------------------------------");

		// ListのforEachで回してラムダ式を当てはめる
		final List<String> uppercaseCities3 = new ArrayList<String>();
		cities.forEach(city -> uppercaseCities3.add(city.toUpperCase()));

		uppercaseCities3.forEach(System.out::println);		
		
		
		System.out.println("--------------------------------");
	
		// Stream インターフェースを利用して値の変換と結果出力を一度に行う
		cities.stream().map(city -> city.toUpperCase()).forEach(city -> System.out.println(city));
		

		System.out.println("--------------------------------");
		
		//  さらにシンプルに。
		cities.stream().map(String::toUpperCase).forEach(System.out::println);
		cities.stream().map(String::toLowerCase).forEach(System.out::println);
		
		
	}

}
