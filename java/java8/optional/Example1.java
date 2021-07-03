package java8.optional;

import java.util.Optional;
import java.util.stream.Stream;

public class Example1 {

	public static void main(String[] args) {


		// 値のあるものだけ後の処理をしたい
		Stream.of(
			Optional.empty(),
	        Optional.of("hoge"),
	        Optional.ofNullable(null),
	        Optional.of("fuga"),
	        Optional.ofNullable("piyo")
		).filter(Optional::isPresent)
		 .map(Optional::get)
		 .forEach(System.out::println);
	
		
		System.out.println("----------------------");
		
		// オプショナル（String）
		Optional<String> str = Optional.of("hoge")
		        .map(String::toUpperCase);
		assert str.get().equals("HOGE");
		
		System.out.println(str.get());
		
		
		System.out.println("----------------------");

		// オプショナル（Integer）
		Optional<Integer> length = Optional.of("hoge")
		        .map(String::length);
		assert length.get().equals(4);		

		System.out.println(length.get());

	
		System.out.println("----------------------");

		// flatMap
		Optional<Object> result = Optional.of("hoge")
		        .flatMap(value -> Optional.of(value + "fuga"))
		        .flatMap(Optional::of)
		        .flatMap(value -> Optional.of(value + "piyo"));
//		assertThat(result.toString(), is("Optional[hogefugapiyo]"));
		System.out.println(result.get());

		// 単にmapに Function<String, Optional<String>> を渡したら素敵なことになる。
		Optional<Object> result2 = Optional.of("hoge")
		        .map(value -> Optional.of(value + "fuga"))
		        .map(Optional::of)
		        .map(value -> Optional.of(value + "piyo"));
//		assertThat(result2.toString(), is("Optional[Optional[Optional[Optional[hogefuga]]piyo]]"));		
		System.out.println(result2.get());
	
	}

}
