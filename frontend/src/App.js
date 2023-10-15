import {BrowserRouter, Route, Routes} from "react-router-dom";


import './App.css';
import Home from "./pages/Home";
import Play from "./pages/Play";

function App() {
  return (

    <div className="gradient-background"> 
      <div className="gradient-background">
        <BrowserRouter>
        {/* <Nav/> */}
        
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