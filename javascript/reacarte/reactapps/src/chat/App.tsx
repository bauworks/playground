import React, * as react from "react";
import "./App.css";
import SocketMessage from "./SocketMessage";

const App: react.FC = () => {
  return (
    <div className="Chat">
      <header className="Chat-header">
          <SocketMessage />
      </header>
    </div>
  );
};

export default App;
