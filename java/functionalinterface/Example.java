public class Example{

    @FunctionalInterface
    interface IHobby{
        public String getHobby(String hobby);
    }

    public static void main(String[] args){

        System.out.println("---------------------------------");

        // 関数インターフェースを実装（Newせずに使える）
        IHobby hb = (String hobby) -> {
            return "my hobby : " + hobby;
        };

        // 実装した関数を呼び出す
        System.out.println(hb.getHobby("cycling"));


        System.out.println("---------------------------------");
        // メソッド参照の例
        Hoge hogeObj = new Hoge();
        hogeObj.hoge();


        System.out.println("---------------------------------");
        // デフォルトメソッドを使って再起的に呼び出した例
        Piyo piyoObj = new Piyo();
        piyoObj.piyo();
  

        System.out.println("---------------------------------");
        // インターフェースを継承して関数インターフェースの例
        Fuga fugaObj = new Fuga();
        fugaObj.fuga();

    }

}
