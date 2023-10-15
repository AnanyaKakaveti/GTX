import { Link } from 'react-router-dom';
import {useState, useEffect, useRef} from 'react';
import raw from '../data/suerte.txt';
import axios from 'axios';

const Play = () => { 

    const [allLyrics, setAllLyrics] = useState("");
    const [lyric, setLyric] = useState("Letras en Español");
    const [lyricE, setLyricE] = useState("Lyrics in English");
    // const counter = useRef(0);
    const [counter, setCounter] = useState(0);
    const [response, setResponse] = useState([]);
    const [grade, setGrade] = useState("Record yourself to see your grade!");

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
        setGrade("Record yourself to see your grade!");
        incrementCounter();
        setLyric(allLyrics.split('\n')[counter] + "\n" + allLyrics.split('\n')[counter + 1]);
        incrementCounter();
        console.log(response);
    }

    const incrementCounter = () => {
        setCounter(counter + 1);
        console.log(counter);
    }

    const submit = () => {
        var url = 'http://127.0.0.1:5000/api/get_user_input/' + lyric;
        console.log("submitting ", url);  
        axios.get(url)
            .then((res) => {
                setResponse(res.data.message);
                console.log(response);
                messageGrade();  
            })
            .catch((error) => {
                console.error(error); 
            });
          
    };

    const messageGrade = () => {
        // console.log(response);
        if (response == 100) {
            setGrade("Amazing! You sang it perfectly!");
        }
        else if (response >= 75 && response < 100) {
            setGrade("Great job! You did pretty good!");
        }
        else if (response >= 40 && response < 75) {
            setGrade("Nice going! Keep practicing to get better!");
        }
        else if (response < 40) {
            setGrade("Your pronunciation could be better!");
        }
        else {
            setGrade("didn't work");
        }
    }

    


    return (
    <div className="App">
        <Link to="/">
        <button style={{width: 125}}>
            Home Page
        </button>
        </Link>
        <button style={{width: 125}} onClick={submit}>
            Make post request
        </button>
      <header className="App-header">
        
        <div className="center">
            Play The Song!
        </div>
            <div className="lyric">
                <div>{lyric}</div>
                <div>--------------------</div>
                <div>{lyricE}</div>
            </div>
            <div className="grade">{grade}</div>
            {/* <button className="lyric" onClick={messageGrade}>Submit</button> */}
            <div className= "right">
                <button className= "button-36" onClick={changeLyric}>Next Lyric</button>
                {/* <button class="button-36" role="button">Button 36</button> */}
            </div>
      </header>
    </div>
    )
}

export default Play;