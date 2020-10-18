import * as React from "react";


//Itemsコンテキストを生成してエクスポート
//（useContext()は使う側で呼んだほうが動き自体はわかりやすいかも）
type ItemsContextType = {
  items: number[];
  deleteItem: React.Dispatch<Action>;
};
const ItemsContext = React.createContext<ItemsContextType>({
  items: [],
  deleteItem: () => {}
});
export const useItemsContext = () => React.useContext(ItemsContext);


//ItemsコンテキストのReducer関数を定義
type State = number[];
type Action = { index: number };
const itemsReducer = (state: State, action: Action) => {
  return state.filter((_, i) => i !== action.index);
};

//--------------------
//関数コンポーネント
//--------------------
export const ItemsContextProvider: React.FC = ({ children }) => {
  //useReducer()でItemsコンテキストの初期値とReducer関数を紐付ける
  const [items, deleteItem] = React.useReducer(itemsReducer, [
    0,
    11,
    22,
    33,
    44,
    55,
    66,
    77
  ]);

  return (
    //Itemsコンテキストを提供可能にする
    <ItemsContext.Provider value={{ deleteItem, items }}>
      {children}
    </ItemsContext.Provider>
  );
};
