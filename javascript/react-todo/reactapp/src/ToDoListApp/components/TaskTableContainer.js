import styled from "styled-components";


//***********************************
// タスクテーブルのレイアウトコンテナ コンポーネント
//***********************************
export const TaskTableContainer = ({ children, title }) => {
  //-------------------------------
  // JSX
  //-------------------------------  
  return (
    <Container1>
      <h3>■ { title }</h3>
      <Container2>
        { children }
      </Container2>
    </Container1>
  )
}

//***********************************
// スタイル設定（継承）
//***********************************
const Container1 = styled.div`
  padding: 0 0 20px 0;
`
const Container2 = styled.div`
  padding: 0 0 0 20px;
`
