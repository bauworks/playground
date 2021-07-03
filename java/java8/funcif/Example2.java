package java8.funcif;
import java.util.function.Supplier;

public class Example2 {

    // 通常のメソッド
    private String method(){
        return("通常のメソッド");
    }
	
    private int methodInt(){
        return(1);
    }

    
    // 文字列を返す関数オブジェクト（プロパティ）
    Supplier<String> supplier = () -> "Stringを返す関数オブジェクト";

    
    /*
     * メソッド参照の例
     */
    private void exec() {
    	
        // 1. 普通にメソッドを呼び出す
        System.out.println("1. this Method      : " + this.method());

        // 2. プロパティとして持っている関数オブジェクトを呼び出す
        System.out.println("2. this Supplier    : " + this.supplier.get());

        // 3. オブジェクトなので変数に代入できる
        Supplier<String> w_supplier = this.supplier;
        System.out.println("3. Local Variable   : " + w_supplier.get());


        // 4. 普通のメソッドもメソッド参照を使えば変数に代入できる
        Supplier<String> methodReference = this::method;
        System.out.println("4. Method Reference : " + methodReference.get());

        
        Supplier<Integer> methodReferenceInt = this::methodInt;
        System.out.println("5. Method Reference Int : " + methodReferenceInt.get());
        
        
    }
    
    
    public static void main(String[] args) {

    	var my = new Example2();
    	my.exec();
    	
	}

}
