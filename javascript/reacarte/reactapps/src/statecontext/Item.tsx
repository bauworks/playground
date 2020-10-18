import React from "react";
import { useItemsContext } from "./ItemsProvider";

type Props = {
  data: number;
  index: number;
};

export const Item = (props: Props) => {
  const { data, index } = props;
  const { deleteItem } = useItemsContext();
  //上記は以下と同義
  //import { ItemsContext } from "./ItemsProvider";
  //const itemcontext = React.useContext(ItemsContext);
  //const deleteItem = itemcontext.deleteItem;

  const clickHandler = () => deleteItem({ index });

  return (
    <div onClick={clickHandler}>
      Item data: {data} index: {index}
    </div>
  );
};
