package java8.funcif;

// インターフェースの定義
interface IFuga {
    String greeting();
    String nameGreeting(String name);
}


// 関数インターフェース
@FunctionalInterface
interface INameFuga extends IFuga {
    // 抽象メソッドが greeting だけになったので、FunctionalInterface にできる。
    @Override
    default String nameGreeting(String name) {
        return name + "さん、" + greeting() + "!!";
    }
}


public class Example4 {

    // INameFugaを呼び出すメソッド
    private static String greetMethod(INameFuga fuga) {
        return fuga.nameGreeting("システム開発事業部");
    }

    
    public static void main(String[] args) {

        // 関数インターフェースを実装してそれぞれのメソッドを呼び出す
        INameFuga nf = () -> "おはよう";
        System.out.println( nf.greeting());
        System.out.println( nf.nameGreeting("モラブ") );

        // メソッド経由で呼び出す。
        System.out.println( greetMethod(() -> "こんにちは"));

        INameFuga wk_fuga = () -> "こんにちは";
        System.out.println( greetMethod(wk_fuga) );
        
	}

}
