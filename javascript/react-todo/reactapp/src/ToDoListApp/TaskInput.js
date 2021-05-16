import React, { useState } from 'react'
import styled from 'styled-components';
import { Button } from './components/Button';
import { AddConfirm } from "./AddConfirm";

// inputタグのスタイル定義
const Input = styled.input`
  margin: 0 8px 0 0;
`

//***********************************
// タスクカラムの表示
//***********************************
const Task = (props) => {

    // タスクタイトル
    const [title, setTitle] = useState("");
  
    // タスク期限
    const [time_limit, setTime_limit] = useState("");

    // 確認ダイアログ表示有無
    const [showModal, setShowModal] = useState(false);

    // [追加]クリック時の処理
    const addTask = () => {
      const task = {id:"", done_flg:0, title:title, time_limit:time_limit};
    //   alert("Add [" + task.title + "], [" + task.time_limit + "]");
      props.addFunc(task);
      setTitle("");
      setTime_limit("");
      setShowModal(false);
    }

    return(
      <div>
          <Input type="text" name="title" value={title} onChange={(e) => setTitle(e.target.value)} />
          <Input type="date" name="time_limit" value={time_limit} onChange={(e) => setTime_limit(e.target.value)}/>
          <Button type="button" onClick={(e) => setShowModal(true)}>追加</Button>
          {
            // 確認ダイアログ
            showModal &&
              <AddConfirm
                confirm={() => addTask()}
                cancel={() => setShowModal(false)}
              />
          }
      </div>
    );
  }

export default Task