import React, { useState } from 'react'
import styled from 'styled-components';
import { Button } from './components/Button';
import { ConfirmDialog } from "./components/ConfirmDialog";

// inputタグのスタイル定義
const Input = styled.input`
  margin: 0 8px 0 0;
`

//***********************************
// タスク入力コンポーネント
//***********************************
export const TaskInput = React.memo((props) => {
console.log("Render     新しいタスクを追加")
  //-------------------------------
  // プロパティ
  //-------------------------------
  // タスクタイトル
  const [title, setTitle] = useState("");

  // タスク期限
  const [time_limit, setTime_limit] = useState("");

  // 確認ダイアログ表示有無
  const [showModal, setShowModal] = useState(false);


  //-------------------------------
  // インナー関数
  //-------------------------------
  // [追加]クリック時の処理
  const addInputTask = () => {
    const task = {id:"", done_flg:0, title:title, time_limit:time_limit};
    props.addFunc(task);
    setTitle("");
    setTime_limit("");
    setShowModal(false);
  }

  //-------------------------------
  // JSX
  //-------------------------------
  return(
    <div>
        {/* タスク */}
        <Input type="text" name="title" value={title} onChange={(e) => setTitle(e.target.value)} />

        {/* 期限 */}
        <Input type="date" name="time_limit" value={time_limit} onChange={(e) => setTime_limit(e.target.value)}/>

        {/* 追加ボタン */}
        <Button type="button" onClick={(e) => setShowModal(true)}>追加</Button>

        {
          // 確認ダイアログ
          showModal &&
            <ConfirmDialog
              message="タスクを追加しますか？"
              confirm={() => addInputTask()}
              cancel={() => setShowModal(false)}
            />
        }
    </div>
  );
});
