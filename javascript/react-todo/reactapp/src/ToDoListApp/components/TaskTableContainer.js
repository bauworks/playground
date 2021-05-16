import styled from "styled-components";

const P_Container = styled.div`
  padding: 0 0 20px 0;
`
const C_Container = styled.div`
  padding: 0 0 0 20px;
`

export const TaskTableContainer = ({ children, title }) => {
  return (
    <P_Container>
      <h3>■ { title }</h3>
      <C_Container>
        { children }
      </C_Container>
    </P_Container>
  )
}

