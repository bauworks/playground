interface IFuga {
    String greeting();
    String nameGreeting(String name);
}

@FunctionalInterface
interface INameFuga extends IFuga {
    // 抽象メソッドが greeting だけになったので、FunctionalInterface にできる。
    @Override
    default String nameGreeting(String name) {
        return name + "さん、" + greeting() + "!!";
    }
}

public class Fuga {

    // INameFugaを呼び出すメソッド
    private static String greetMethod(INameFuga fuga) {
        return fuga.nameGreeting("WORKS");
    }

    public void fuga() {
        // 関数インターフェースを実装してそれぞれのメソッドを呼び出す
        INameFuga nf = ( () -> "おはよう" );
        System.out.println( nf.greeting());
        System.out.println( nf.nameGreeting("BAU") );

        // メソッド経由で呼び出す。
        System.out.println( greetMethod(() -> "こんにちは"));

    }

}
