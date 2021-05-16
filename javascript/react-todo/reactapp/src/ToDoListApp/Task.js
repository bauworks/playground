import React, { useState, useEffect } from 'react'
import styled from 'styled-components';

//***********************************
// タスクカラムの表示
//***********************************
const Task = (props) => {

    // タスクID
    const id = props.task.id;

    // 実施フラグ
    const [checked, setChecked] = useState( () => {
        if (props.task.done_flg === 0) {
            return false
        } else {
            return true;
        }
    });
    const changeChecked = (e) => {
        setChecked(e.target.checked);
    }

    // タスクタイトル
    const [title, setTitle] = useState(props.task.title);
    const changeTitle = (e) => {
        setTitle(e.target.value);
    }

    // タスク期限
    const [time_limit, setTime_limit] = useState(props.task.time_limit);
    const changeTime_limit = (e) => {
        setTime_limit(e.target.value);
    }

    //------------------------
    // タスクの更新 & 表示更新
    //------------------------
    useEffect(
        () => {
            const done_flg = checked ? 1 : 0;
            const task = {id:id, done_flg:done_flg, title:title, time_limit:time_limit};
            props.modFunc(task);
            },
            [checked, title, time_limit]
    );


    // スタイル設定
    const Input = styled.input`
    margin: 0 8px 0 0;
    `

    const titleStyle = (checked) => ({
        textDecorationLine: checked ? "line-through" : "none"
    });

    return(
      <td>
          <Input type="checkbox"name="done_flg" checked={checked} onChange={changeChecked}/>
          <Input type="hidden" name="id" value={id} />
          <Input type="text" name="title" value={title} onChange={changeTitle} style={titleStyle(checked)} />
          <Input type={checked ? "hidden" : "date"} name="time_limit" value={time_limit} onChange={changeTime_limit}/>
      </td>
    );
  

}

export default Task