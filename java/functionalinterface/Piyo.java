import java.io.PrintStream;

@FunctionalInterface
interface IPiyoFunc<T> {

    // 抽象メソッド（T型をもらって何も返さない関数）
    void accept(T t);
    
    // デフォルトメソッド（IPiyoFunc型をもらってIPiyoFunc型を返す）
    default IPiyoFunc<T> andThen(IPiyoFunc<? super T> after) {
        return (T t) -> {
            accept(t);
            after.accept(t);
        };
    }
}

public class Piyo{
    public void piyo() {
        IPiyoFunc<PrintStream> piyo1 = stream -> stream.print("ABC ");
        IPiyoFunc<PrintStream> piyo2 = stream -> stream.println("DEF");
        IPiyoFunc<PrintStream> piyo3 = stream -> stream.println("GHI");
    
        piyo1.accept(System.out);   // ABC
        piyo2.accept(System.out);   // DEF

        System.out.println("-----");

        piyo1.andThen(
            piyo2.andThen(
                piyo3
            )
        ).accept(System.out);

        // 以下と同じ（piyopiyo の accept にネストした andThen() が入る）
        // IPiyoFunc<PrintStream> piyopiyo = piyo1.andThen(
        //     piyo2.andThen(
        //         piyo3
        //     )
        // );
        // piyopiyo.accept(System.out);
    }
}