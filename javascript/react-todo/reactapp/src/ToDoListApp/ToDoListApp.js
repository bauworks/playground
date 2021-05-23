import React, { useState, useEffect } from 'react'
import styled from 'styled-components';
import TaskInput from './TaskInput';
import TaskTable from './TaskTable';
import { Button } from './components/Button';
import { TaskTableContainer } from './components/TaskTableContainer';

//***********************************
// ToDoList APPコンポーネント
//***********************************
const ToDoListApp = () => {

    //-------------------------------
    // プロパティ
    //-------------------------------
    const [loading, setLoading] = useState(true);

    // 全てのタスク    
    const [taskAll, setTaskAll] = useState([]);

    /*** タスクの追加 ***/
    const addTask = (task) => {
        // テーブルを更新してタスクリストに追加
        fetch('http://localhost:8080/api/add', {
            method: 'POST',
            mode: 'cors',
            headers: new Headers({
                'Content-Type': 'application/json; charset=utf-8'
            }),
            body: JSON.stringify(task)
        })
        .then(res => res.json())
        .then(json => {
            // タスクリストに追加
            const copied = taskAll.map((orgTask) => {
                return orgTask;
            });
            copied.push({id:json.id, done_flg:json.done_flg, title:json.title, time_limit:json.time_limit});
            setTaskAll(copied);
        });
    }

    /*** タスクの更新 ***/
    const modTask = (task) => {
        // テーブルを更新してIDが一致するタスクを差し替え
        fetch('http://localhost:8080/api/update', {
            method: 'POST',
            mode: 'cors',
            headers: new Headers({
                'Content-Type': 'application/json; charset=utf-8'
            }),
            body: JSON.stringify(task)
        })
        .then(res => res.json())
        .then(json => {
            // IDが一致するタスクを差し替え
            const modified = taskAll.map((orgTask) => {
                if (task.id === orgTask.id) {
                    return task;
                } else {
                    return orgTask;
                }
            });
            setTaskAll(modified);
        });
    }

    /*** タスクの削除 ***/
    // [完了済みを削除]クリック時の処理
    const removeFinishedTask = () => {
        // テーブルを更新して未完了のタスクのみ抽出
        fetch('http://localhost:8080/api/delete')
        .then(res => {
            // 未完了のタスクのみ抽出して差し替え
            const unfinished = taskAll.filter((task) => {
                return task.done_flg === 0
            });
            setTaskAll(unfinished);
        });
    }
  
    //-------------------------------
    // 副作用
    //-------------------------------
    // 初回実行
    /*** 初期値をDBから取得 ***/
    useEffect(() => {

        const fetchData = async () => {
            const URL = 'http://localhost:8080/api/selectall';
            const res = await fetch(URL)
            const data = await res.json();
            // ↓一行で書くとこうなる
            // await (await fetch(URL)).json();
            setTaskAll(data);
        }

        setTimeout(() => {
            fetchData();
            setLoading(false);
        }, 1000);
    }, []);



    //-------------------------------
    // JSX
    //-------------------------------
    return(
        <div>
            <h1>ToDoList</h1>
            <TaskTableContainer title="新しいタスクを追加">
                <TaskInput addFunc={addTask} />
            </TaskTableContainer>

            <TaskTableContainer title="マイタスク">
                <TaskTable taskAll={taskAll} done_flg="0" modFunc={modTask} loading={loading}/>
            </TaskTableContainer>

            <TaskTableContainer title="完了済み">
                <TaskTable taskAll={taskAll} done_flg="1" modFunc={modTask} loading={loading} />
                <ButtonDel type="button" onClick={removeFinishedTask} mgtop="10px">完了済みを削除</ButtonDel>
            </TaskTableContainer>

        </div>
    );
}

export default ToDoListApp


//***********************************
// スタイル設定
//***********************************
// スタイル定義(カスタム継承＆引数の例)
const ButtonDel = styled(Button)`
    margin: ${props => props.mgtop} 0 0 0;
`
