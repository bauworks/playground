import React, { useState, useCallback } from "react";
import logo from "./logo.svg";
import "./App.css";

const App: React.FC = () => {
  const [count, setCount] = useState<number>(0);

  const handleIncrement = useCallback(() => {
    setCount((prev) => prev + 1);
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>

        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <div>{count}</div>
        <button onClick={handleIncrement}>Add</button>
      </header>
    </div>
  );
};

export default App;
