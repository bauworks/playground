import java.util.function.Supplier;

public class Hoge{

    // 通常のメソッド
    private String method(){
        return("通常のメソッド");
    }

    // 文字列を返す関数オブジェクト（プロパティ）
    Supplier<String> supplier = () -> "Stfingを返す関数オブジェクト";


    public void hoge() {

        // メソッドを呼び出す
        System.out.println("     this Method : " + this.method());

        // プロパティの関数オブジェクトを呼び出す
        System.out.println("   this Supplier : " + this.supplier.get());

        // プロパティなので変数に代入できる
        Supplier<String> w_supplier = this.supplier;
        System.out.println("  Local Variable : " + w_supplier.get());


        // メソッドもメソッド参照を使えば変数に代入できる
        Supplier<String> methodReference = this::method;
        System.out.println("Method Reference : " + methodReference.get());

    }


}