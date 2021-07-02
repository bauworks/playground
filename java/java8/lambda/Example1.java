package java8.lambda;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.function.UnaryOperator;
import java.util.stream.Collectors;
public class Example1 {

	
	/*
	 * ラムダ式コレクション
	 */
    public static void main(String[] args){

        System.out.println("\n***** forEach() *****");
        {
            List<String> list = List.of("a", "b", "c");

            // list.forEach(t -> System.out.println(t));
            list.forEach(System.out::println);
        }

        System.out.println("\n***** Map.computeIfAbsent() *****");
        {
        	// computeIfAbsent
        	// 指定したkeyの要素が存在しない、または値がNULLの場合に指定したkeyと任意の処理で算出した値をputする。
            Map<String, Integer> map = new HashMap<>();
            System.out.println( map.computeIfAbsent("cherry", (str)->str.length()) );
            System.out.println( map.computeIfAbsent("cherry", String::length) );
        }

        System.out.println("\n***** List.replaceAll() *****");
        {
            List<String> list = new ArrayList<>();
            list.add("Apple");
            list.add("Banana");
            list.add("Cherry");

            System.out.println("toUpperCase()");
            list.replaceAll( t -> t.toUpperCase() );
            list.forEach(System.out::println);
            
            System.out.println("toLowerCase()");
            list.replaceAll(String::toLowerCase);
            list.forEach(System.out::println);
        }

        System.out.println("\n***** List -> Map *****");
        {
            class Item {
                private long id;
                private String name;
                public Item(long id, String name){
                    this.id = id;
                    this.name = name;
                }
                public long getId() {return this.id;}
            }

            List<Item> list = new ArrayList<>();
            list.add(new Item(1L, "apple"));
            list.add(new Item(2L, "banana"));
            list.add(new Item(3L, "cherry"));

            //Map<Long, Item> fruitIdMap = list.stream()
            //              .collect(Collectors.toMap(Item::getId, i -> i));
            // more than better
            Map<Long, Item> fruitIdMap = list.stream()
                                            .collect(
                                                Collectors.toMap(
                                                    Item::getId,
                                                    UnaryOperator.identity()
                                            ));

            fruitIdMap.forEach( (key, map) -> {System.out.println(key + " : " + map.name);} );
        }
    }
}
