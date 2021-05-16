import { useContext } from 'react';
import styled from 'styled-components';
import { ModalBase } from "./components/ModalBase";
import { Button } from "./components/Button";

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

  const ButtonKai = styled(Button)`
    padding: 16px 32px;
  `

export const AddConfirm = ({ confirm, cancel }) => {
  return (
    <ModalBase>
      <Container>
        <div>タスクを追加しますか？</div>
        <ButtonWrapper>
          <ButtonKai onClick={confirm}>OK</ButtonKai>
          <ButtonKai onClick={cancel}>Cancel</ButtonKai>
        </ButtonWrapper>
      </Container>
    </ModalBase>
  )
}
