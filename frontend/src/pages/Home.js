// import logo from '../logo.svg';
import { Link } from 'react-router-dom';
import React, {useState} from 'react';


const Home = () => { 
    const [espanol, setEspanol] = useState(false)
    const [espanolpop, setEspanolpop] = useState(false)
    return (
      <div className="App">
      <header>
          <div className='App-header'>
            <div className='first-line'>Learning language through music</div>
            <div className="center">Welcome to Cantar! <br></br></div>
            <div className='selection'>Select your language:</div>
            {/* Select your language: */}
            {/* <Link to="/play"> */}
            <div className = 'button-line'>
              <button onClick={()=>setEspanol(true)} class="button-27" role="button">Spanish</button>
              <span></span>
              <button class="button-27" role="button">German</button>
              <span></span>
              <button class="button-27" role="button">French</button>
            </div>
          {/* </Link> */}
          <div className='selection'>Select your genre:</div>
          <div className = 'button-line'>
              <button onClick={()=>setEspanolpop(true)} class="button-27" role="button">Pop</button>
              <span></span>
              <button class="button-27" role="button">Rap</button>
              <span></span>
              <button class="button-27" role="button">Hip Hop</button>
            </div>
            <div className='selection'>Select your song:</div>
            <Link to="/play">
            <div className = 'button-line'>
              
              {espanol&&espanolpop?<button class="button-27" role="button">Suerte - Shakira</button>:null}
              <span></span>
              {espanol&&espanolpop?<button class="button-27" role="button">Un Preview - Bad Bunny</button>:null}
              <span></span>
              {espanol&&espanolpop?<button class="button-27" role="button">Holanda - Jhayco</button>:null}
              
            </div>
            </Link>
          </div>
      </header>
     
    </div>

    )
}
export default Home;


{/* <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <Link to="/play">
          <button>
            Click me!
          </button>
        </Link>
      </header>
    </div> */}