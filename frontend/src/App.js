import {BrowserRouter, Route, Routes, Link} from "react-router-dom";


import './App.css';
import Home from "./pages/Home";
import Play from "./pages/Play";
import Navbar from "./Navbar";


function App() {
  const presetPoints = [
    { start: 10, end: 20 },
    { start: 30, end: 40 },
    // Add more preset points as needed
  ];

  return (

    <div className="gradient-background"> 
      <div className="gradient-background">
        <BrowserRouter>
        <Navbar/>
          <Routes>
              <Route path="/" element={<Home/>} />
              <Route path="/play" element={<Play/>} />
              {/* <Route path="/feed" element={<Feed name = "name" song="song"/>} /> */}

          </Routes>
        
          {/* <Footer/> */}
        
        </BrowserRouter>
        </div>
      </div>   
  );
}

export default App;