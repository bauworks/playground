import React, { VFC } from 'react';
import {
  LocalState,
  mutateLocalState,
  useLocalSelector,
  useLocalStateCreate,
} from '@react-libraries/use-local-state';

interface LocalStateType {
  tall: number;
  weight: number;
}
interface ChildProps {
  state: LocalState<LocalStateType>;
}

export const Tall: VFC<ChildProps> = ({ state }) => {
  console.log('Tall');
  const tall = useLocalSelector(state, (v) => v.tall);
  return (
    <div>
      Tall:
      <input
        value={tall}
        onChange={(e) => {
          mutateLocalState(state, (v) => ({ ...v, tall: Number(e.target.value) }));
        }}
      />
    </div>
  );
};
export const Weight: VFC<ChildProps> = ({ state }) => {
  console.log('Weight');
  const weight = useLocalSelector(state, (v) => v.weight);
  return (
    <div style={{ display: 'flex' }}>
      Weight:
      <input
        value={weight}
        onChange={(e) => {
          mutateLocalState(state, (v) => ({ ...v, weight: Number(e.target.value) }));
        }}
      />
    </div>
  );
};

export const Bmi: VFC<ChildProps> = ({ state }) => {
  console.log('Bmi');
  const { tall, weight } = useLocalSelector(state, (v) => v);
  return (
    <div>
      {isNaN(Number(tall)) || isNaN(Number(weight))
        ? 'Error'
        : `BMI:${Math.floor((Number(weight) / Math.pow(Number(tall) / 100, 2)) * 100) / 100}`}
    </div>
  );
};

const App = () => {
  const state = useLocalStateCreate<LocalStateType>(() => ({ tall: 170, weight: 60 }));
  console.log('Parent');
  return (
    <>
      <Bmi state={state} />
      <br></br>
      <Tall state={state} />
      <br></br>
      <Weight state={state} />
    </>
  );
};

export default App;