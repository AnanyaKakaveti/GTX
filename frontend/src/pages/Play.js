import { Link } from 'react-router-dom';

const Play = () => { 

    return (
    <div className="App">
      <header className="App-header">
          Play The Song!
          <Link to="/">
            <button>
              Go to Home Page!
            </button>
          </Link>
      </header>
    </div>
    )
}

export default Play;