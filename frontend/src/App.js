import './App.css';
import { BrowserRouter, Routes, Route as Switch } from "react-router-dom"
import { Home } from './components/Home';
import { AddCoin } from './components/AddCoin';
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.js";
import { AddTradePair } from './components/AddTradePair';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
            <Routes>
                <Switch path="/" element={<Home />} />
                <Switch path="/add-coin" element={<AddCoin />} />
                <Switch path="/add-trade-pair" element={<AddTradePair />} />
            </Routes>
        </BrowserRouter>
    </div>
  );
}

export default App;
