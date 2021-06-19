import React, { useState, useEffect } from 'react'
import styled from 'styled-components';
import { Button } from './components/Button';

//***********************************
// タスクコンポーネント
//***********************************
export const Task = React.memo((props) => {
// console.log("Render     " + props.task.title)
    //-------------------------------
    // プロパティ
    //-------------------------------
    // タスクID
    const id = props.task.id;

    // 実施フラグ
    const [checked, setChecked] = useState( () => {
        return props.task.done_flg === 0 ? false : true;
    });

    // タスクタイトル、更新フラグ
    const [title, setTitle] = useState(props.task.title);
    const [title_edited, setTitle_edited] = useState(false);

    // タスク期限、更新フラグ
    const [time_limit, setTime_limit] = useState(props.task.time_limit);
    const [time_limit_edited, setTime_limit_edited] = useState(false);


    //-------------------------------
    // インナー関数
    //-------------------------------
    // タスクの更新 & 表示更新
    const changeTask = () => {
        const done_flg = checked ? 1 : 0;
        const task = {id:id, done_flg:done_flg, title:title, time_limit:time_limit};
        props.modFunc(task);
        setTitle_edited(false);
        setTime_limit_edited(false);
    };


    //-------------------------------
    // 副作用
    //-------------------------------
    // チェックボックスの操作時に実行
    useEffect(
        () => {
            changeTask();
        },
        // eslint-disable-next-line react-hooks/exhaustive-deps
        [checked]
    );


    //------------------------
    // スタイル設定
    //------------------------
    // タイトル（マイタスク）
    const titleInputStyle = () => ({
        display: checked ? "none" : "",
        background: title_edited ? "#ffffcc" : "#ffffff",
    });
    // タイトル（完了済）
    const titleSpanStyle = () => ({
        display: checked ? "" : "none",
        textDecorationLine: checked ? "line-through" : "none",
    });
    // 期限
    const timeLimitStyle = () => ({
        background: time_limit_edited ? "#ffffcc" : "#ffffff",
    });
//    // 更新ボタン（継承パターンを使ってみたためコメントアウト）
//    const buttonStyle = (checked) => ({
//        display: checked ? "none" : "",
//    });

    return(
        <td>
            <Input type="hidden" name="id" value={id} />

            {/*チェックボックス*/}
            <Input type="checkbox"name="done_flg" checked={checked} onChange={(e) => setChecked(e.target.checked)}/>

            {/*タイトル*/}
            <Input type="text" name="title" value={title} 
                onChange={(e) => {setTitle(e.target.value);setTitle_edited(true)}} style={titleInputStyle()} />
            <span style={titleSpanStyle()} >{title}</span>

            {/*期限*/}
            <Input type={checked ? "hidden" : "date"} name="time_limit" value={time_limit}
                onChange={(e) => {setTime_limit(e.target.value);setTime_limit_edited(true)}} style={timeLimitStyle()}/>

            {/*更新ボタン*/}
            <ButtonMod type="button" onClick={() => changeTask()} isChecked={checked} >更新</ButtonMod>
        </td>
    );
  

});


//***********************************
// スタイル設定（継承）
// （この形式で定義する場合は関数外でないとワーニングが出る）
//***********************************
// (入力のたびにフォーカスが外れるのを回避するためにクラス外に移動)
// inputタグ全般
const Input = styled.input`
  margin: 0 8px 0 0;
`
// 更新ボタン
const ButtonMod = styled(Button)`
    display: ${props => props.isChecked ? "none" : ""};
`