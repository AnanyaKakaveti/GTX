// import logo from '../logo.svg';
import { Link } from 'react-router-dom';

const Home = () => { 

    return (
      <div className="App">
      <header>
          <div className='App-header'>
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