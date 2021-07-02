package java8.funcif;

public class Example1 {

    @FunctionalInterface
    interface IHobby{
        public String getHobby(String hobby);
    }
    
    
	public static void main(String[] args) {

        // 関数インターフェースを実装（Newせずに使える）
        IHobby hb = (String hobby) -> {
            return "my hobby : " + hobby;
        };

        // 実装した関数を呼び出す
        System.out.println( hb.getHobby("cycling") );
		
		
	}

}
