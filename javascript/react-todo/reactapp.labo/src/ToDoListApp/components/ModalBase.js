import ReactDOM from 'react-dom'
import styled from 'styled-components';

// モーダルベースのアンカーを取得
const modalRoot = document.getElementById('modal-root');

//***********************************
// モーダルベースコンポーネント
//***********************************
export const ModalBase = (props) => {
  return ReactDOM.createPortal(
    <Container>
      { props.children }
    </Container>,
    modalRoot
  )
}

//***********************************
// スタイル設定（継承）
//***********************************
const Container = styled.div`
  position: absolute;
  top: 0;
  left: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
  background-color: rgba(0, 0, 0, .5);
`