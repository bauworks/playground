import React from "react";

import { Item } from "./Item";
import { useItemsContext } from "./ItemsProvider";

export const List = () => {
  const { items } = useItemsContext();
  //上記は以下と同義
  //import { ItemsContext } from "./ItemsProvider";
  //const itemscontext = React.useContext(ItemsContext);
  //const items = itemscontext.items;

  return (
    <div>
      {items.map((o, index) => (
        <Item data={o} index={index} />
      ))}
    </div>
  );
};

export default List;