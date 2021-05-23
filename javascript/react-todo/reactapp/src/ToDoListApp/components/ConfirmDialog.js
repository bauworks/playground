import styled from 'styled-components';
import { ModalBase } from "./ModalBase";
import { Button } from "./Button";

//***********************************
// 確認ダイアログコンポーネント
//***********************************
export const ConfirmDialog = ({ message, confirm, cancel }) => {
  return (
    <ModalBase>
      <Container>
        <div>{message}</div>
        <ButtonWrapper>
          <Button1 onClick={confirm}>OK</Button1>
          <Button1 onClick={cancel}>Cancel</Button1>
        </ButtonWrapper>
      </Container>
    </ModalBase>
  )
}

//***********************************
// スタイル設定（継承）
//***********************************
const Container = styled.div`
  width: 240px;
  border-radius: 10px;
  padding: 24px 36px;
  color: black;
  background-color: white;
`

const ButtonWrapper = styled.div`
  display: flex;
  justify-content: space-around;
  margin-top: 24px;
`

const Button1 = styled(Button)`
  padding: 16px 32px;
`
