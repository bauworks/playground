import React, { useState, useEffect, useCallback } from 'react'
import styled from 'styled-components';
import { TaskInput } from './TaskInput';
import { TaskTable } from './TaskTable';
import { Button } from './components/Button';
import { TaskTableContainer } from './components/TaskTableContainer';

//***********************************
// ToDoList APPコンポーネント
//***********************************
export const ToDoListApp = () => {
console.log("Render ■ ToDoListApp")

    //-------------------------------
    // プロパティ
    //-------------------------------
    const [loading, setLoading] = useState(true);

    // 全てのタスク    
    const [taskAll, setTaskAll] = useState([]);

    // 仕掛中タスク、完了済タスク
    const [taskRun, setTaskRun] = useState([]);
    const [taskFin, setTaskFin] = useState([]);

    /*** タスクの追加 ***/
    const addTask = useCallback((task) => {
console.log("useCallback addTask")

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
            // const copied = taskAll.map((orgTask) => {
            //     return orgTask;
            // });
            // copied.push({id:json.id, done_flg:json.done_flg, title:json.title, time_limit:json.time_limit});
            // setTaskAll(copied);
            taskAll.push({id:json.id, done_flg:json.done_flg, title:json.title, time_limit:json.time_limit});
            setTaskAll(taskAll);

            // 仕掛中タスク
            const taskRunNew = taskAll.filter((task) => {return task.done_flg === 0});
            setTaskRun(taskRunNew);

        });
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [taskRun]);

    /*** タスクの更新 ***/
    const modTask = useCallback((task) => {
console.log("useCallback modTask")
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
            // const modified = taskAll.map((orgTask) => {
            //     if (task.id === orgTask.id) {
            //         return task;
            //     } else {
            //         return orgTask;
            //     }
            // });
            // setTaskAll(modified);
            
            // 同じIDのタスクを差し替える
            const modified = taskAll.map((orgTask) => {
                if (task.id === orgTask.id) {
                    return task;
                } else {
                    return orgTask;
                }
            });
            // taskAllの中身をmodifiedの中身で入れ替える
            taskAll.length = 0;
            modified.forEach((task) => {taskAll.push(task);});
            setTaskAll(taskAll);

            // 仕掛中タスク
            const taskRunNew = taskAll.filter((task) => {return task.done_flg === 0});
            setTaskRun(taskRunNew);

            // 完了タスク
            const taskFinNew = taskAll.filter((task) => {return task.done_flg === 1});
            setTaskFin(taskFinNew);
        });
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [taskRun, taskFin]);

    /*** タスクの削除 ***/
    // [完了済みを削除]クリック時の処理
    const removeFinishedTask =useCallback(() => {
console.log("useCallback removeFinishedTask")
        // テーブルを更新して未完了のタスクのみ抽出
        fetch('http://localhost:8080/api/delete')
        .then(res => {
            // 未完了のタスクのみ抽出
            const unfinished = taskAll.filter((task) => {
                return task.done_flg === 0
            });
            // taskAllの中身をunfinishedの中身で入れ替える
            taskAll.length = 0;
            unfinished.forEach((task) => {taskAll.push(task);});
            setTaskAll(taskAll);

            // 完了タスク
            const taskFinNew = taskAll.filter((task) => {return task.done_flg === 1});
            setTaskFin(taskFinNew);

        });
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [taskFin]);
  
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

            // 全タスク
            setTaskAll(data);

            // 仕掛中タスク
            const taskRunNew = data.filter((task) => {return task.done_flg === 0});
            setTaskRun(taskRunNew);

            // 完了タスク
            const taskFinNew = data.filter((task) => {return task.done_flg === 1});
            setTaskFin(taskFinNew);

            setLoading(false);
        }

        setTimeout(() => {
            fetchData();
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
                <TaskTable taskAll={taskRun} done_flg="0" modFunc={modTask} loading={loading}/>
            </TaskTableContainer>

            <TaskTableContainer title="完了済み">
                <TaskTable taskAll={taskFin} done_flg="1" modFunc={modTask} loading={loading} />
                <ButtonDel type="button" onClick={removeFinishedTask} mgtop="10px">完了済みを削除</ButtonDel>
            </TaskTableContainer>

        </div>
    );
}


//***********************************
// スタイル設定
//***********************************
// スタイル定義(カスタム継承＆引数の例)
const ButtonDel = styled(Button)`
    margin: ${props => props.mgtop} 0 0 0;
`
