import { Link } from 'react-router-dom';
import {useState, useEffect, useRef} from 'react';
import raw from '../data/suerte.txt';

const Play = () => { 

    const [allLyrics, setAllLyrics] = useState("");
    const [lyric, setLyric] = useState("Letras en Español");
    const [lyricE, setLyricE] = useState("Lyrics in English");
    // const counter = useRef(0);
    const [counter, setCounter] = useState(0);

    useEffect(() => {
        fetch(raw)
            .then(r => r.text())
            .then(text => {
                console.log('text decoded:', text);
                setAllLyrics(text);
                // changeLyric();
                // console.log("Lyrics: ", allLyrics);
        });
    }, [])

    async function changeLyric() {
        incrementCounter();
        setLyric(allLyrics.split('\n')[counter] + "\n" + allLyrics.split('\n')[counter + 1]);
        incrementCounter();
    }

    const incrementCounter = () => {
        setCounter(counter + 1);
        console.log(counter);
    }

    return (
    <div className="App">
        <button style={{width: 125}}>
            Home Page
        </button>
      <header className="App-header">
        
        <div className="center">
            Play The Song!
            <Link to="/">
                
            </Link>
        </div>
            <div className="lyric">{lyric}</div>
            <div className="lyric">--------------------</div>
            <div className="lyric">{lyricE}</div>
            <div className= "right">
                <button className= "button-36" onClick={changeLyric}>Next Lyric</button>
                {/* <button class="button-36" role="button">Button 36</button> */}
            </div>
      </header>
    </div>
    )
}

export default Play;