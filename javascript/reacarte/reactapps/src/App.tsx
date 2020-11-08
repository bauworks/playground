import React from 'react';
import { BrowserRouter, Route, Link } from 'react-router-dom';
import Origin from './origin/App';
import AddSub from './addsub/App';
import Chat from './chat/App';
import Tutorial from './tutorial/index';
import EffectCC from './hooks/EffectCC';
import EffectFC from './hooks/EffectFC';
import StateContext from './statecontext/App';
import MaterialUI from './materialui/App';


const Menu = () => {
    return (
      <div>
        <Link to="/origin">
          <button>Origin</button>
        </Link>
        <Link to="/addsub">
          <button>AddSub</button>
        </Link>
        <Link to="/chat">
          <button>Chat (WebSocket)</button>
        </Link>
        <Link to="/tutorial">
          <button>Tutorial TypeScript</button>
        </Link>
        <Link to="/hookscc">
          <button>Hooks Class</button>
        </Link>
        <Link to="/hooksfc">
          <button>Hooks Function</button>
        </Link>
        <Link to="/statecontext">
          <button>Hooks State/Context</button>
        </Link>
        <Link to="/materialui">
          <button>Material UI</button>
        </Link>
      </div>
    );
};
  
const App = () => {
  return (
    <div>
      <BrowserRouter>
        <div>
          <Route path="/" component={Menu} />
          <Route path="/origin"  component={Origin} />
          <Route path="/addsub"  component={AddSub} />
          <Route path="/chat"  component={Chat} />
          <Route path="/tutorial"  component={Tutorial} />
          <Route path="/hookscc"  component={EffectCC} />
          <Route path="/hooksfc"  component={EffectFC} />
          <Route path="/statecontext"  component={StateContext} />
          <Route path="/materialui"  component={MaterialUI} />
        </div>
      </BrowserRouter>
    </div>
  );
};

export default App;
