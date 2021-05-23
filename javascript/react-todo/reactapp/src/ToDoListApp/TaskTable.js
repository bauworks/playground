import React from 'react'
import Task from './Task';
import styled from 'styled-components';

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
    // ロード中
    const Loading = (
      <LoadDiv>ロード中...</LoadDiv>
    );

    // タスクテーブル
    const LoadedTable = (
      <table border='0' cellSpacing='0'>
        <thead>
        </thead>
        <tbody>
            {taskRows}
        </tbody> 
      </table>
    );

    return props.loading ? Loading : LoadedTable;
    
}

export default TaskTable


//***********************************
// スタイル設定（継承）
//***********************************
const LoadDiv = styled.div`
  /*
   * height: 30px;
   * padding: 10px;
   */
  color: ${() => "#666"};
  background-color: ${() => "#FFF"};
`