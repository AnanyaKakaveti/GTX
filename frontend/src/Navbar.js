import { Link } from 'react-router-dom';
import React, {} from 'react';
import './App.css';


const Navbar = () => { 

    return (
        <div className="App">
            <Link to="/">
                <button className='homeButton'>
                    Home Page
                </button>
            </Link>
        </div>

    )
}
export default Navbar;