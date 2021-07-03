package java8.lambda2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

public class Example2 {

	public static void main(String[] args) {

		// ベースのArrayList
		final List<String> cities = Arrays.asList("Kyoto", "Osaka", "Kobe");
		cities.forEach(System.out::println);		


		System.out.println("1. --------------------------------");

		// 普通にfor文を回してtoUpper
		final List<String> startWithK = new ArrayList<>(); // 新しい配列の変数を宣言して生成！
		
		for (String city : cities) {                       // ループしてリストを読み込み・・・
		  if (city.startsWith("K")) {                      // 「K」から始まる場合は・・・
		    startWithK.add(city);                          // 配列に追加！
		  }
		}
		// 結果を確認
		startWithK.forEach(System.out::println);		

		
		System.out.println("2. --------------------------------");

		
		// filter() メソッドを利用するように書き換え、ラムダ式も当てはめる。
		final List<String> startWithK2 = 
				  cities.stream()
				    .filter(city -> city.startsWith("K"))   // boolean型を返すラムダ式を期待
				    .collect(Collectors.toList());          // 結果をリストに変換
		
		// 結果を確認
		startWithK2.forEach(System.out::println);		
		

		System.out.println("3. --------------------------------");

		// 要素を 1 つ検索
		String foundCity = null;
		for (String city : cities) {
		  if (city.startsWith("K")) {
		    foundCity = city;
		    break;
		  }
		}
		if (foundCity != null) {
		  System.out.println(foundCity);    // 標準出力：存在する場合
		} else {
		  System.out.println("Not found!"); // 標準出力：存在しない場合
		}
	
		
		System.out.println("4. --------------------------------");
		final Optional<String> foundCity1 = 
				  cities.stream()
				    .filter(city -> city.startsWith("K"))
				    .findFirst(); // 最初の要素または空

		foundCity1.ifPresentOrElse(System.out::println,System.out::println);
		
	
	}

}
