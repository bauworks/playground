import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import ProductPage from "./pages/ProductPage";
import TopPage from "./pages/TopPage";

const App: React.FC = () => {
  return (
    <Router>
      <Switch>
        <Route path="/materialui/products" component={ProductPage} exact />
        <Route path="/materialui" component={TopPage} exact />
      </Switch>
    </Router>
  );
};

export default App;