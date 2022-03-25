import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import "./App.css";
import Navbar from "./components/Navbar/Navbar";
import Header from "./components/Header/Header";
import Bot from "./components/Bot/Bot";
import Features from "./components/Feature/Features";
import Footer from './components/Footer/Footer'

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Header />
        <Bot />
        <Features />
        <Footer/>
      </div>
    </Router>
  );
}

export default App;
