import React from 'react'
import Task from './Task';

//***********************************
// タスクテーブルコンポーネント
//***********************************
const TaskTable = (props) => {

    // 表示タスクの絞り込み
    const taskSelected = props.taskAll.filter((task) => {
      return task.done_flg === Number(props.done_flg)
    });

    // TRタグの配列を生成
    const taskRows = taskSelected.map((task) =>
      <tr key={task.id}>
        <Task task={task} modFunc={props.modFunc}/>
      </tr>
    );

    //-------------------------------
    // JSX
    //-------------------------------
    return(
        <table border='0' cellSpacing='0'>
        <thead>
        </thead>
        <tbody>
            {taskRows}
        </tbody> 
        </table>    
    );
}

export default TaskTable