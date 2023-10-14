// import logo from '../logo.svg';
import YouTubePlayer from "../YouTubePlayer";
import { Link } from 'react-router-dom';

const presetPoints = [
  { start: 10, end: 20 },
  { start: 30, end: 40 },
  // Add more preset points as needed
];


const Home = () => { 

    return (
      <div className="App">
      <header>
          <div className='App-header'>
            <YouTubePlayer videoId='a8Rwz6zBJSE' presetPoints={presetPoints} />
            Welcome!
            <Link to="/play">
            <button>
              Go to Play Page!
            </button>
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