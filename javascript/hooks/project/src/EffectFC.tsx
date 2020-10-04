import React, { useState, useEffect } from 'react'

const EffectFC:React.FC = () => {

  const [count1, setCount1] = useState<number>(0)
  const handleClick1 = () => {
    setCount1(count1 + 1 )
  }

  const [count2, setCount2] = useState<number>(0)
  const handleClick2 = () => {
    setCount2(count2 + 1 )
  }

  useEffect(
    () => {
      document.title =`useEffect（C1:${count1}) (C2:${count2}）`
    },
    [count1]
  );


  return(
    <div>
      <h1>関数コンポーネント</h1>
      <p>[1] {count1} 回クリックしました</p>
      <p>[2] {count2} 回クリックしました</p>
      <button onClick={handleClick1}>C1</button>
      <button onClick={handleClick2}>C2</button>
    </div>
  );
}

export default EffectFC