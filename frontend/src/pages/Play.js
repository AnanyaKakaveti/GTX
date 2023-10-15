import { Link } from 'react-router-dom';
import {useState, useEffect, useRef} from 'react';
import raw from '../data/suerteSpanish.txt';
import raw2 from '../data/suerteEnglish.txt';
import axios from 'axios';
import YouTubePlayer from "../YouTubePlayer";

const presetPoints = [
    { start: 10, end: 20 },
    { start: 30, end: 40 },
    // Add more preset points as needed
  ];

const Play = () => { 

    const [allLyrics, setAllLyrics] = useState("");
    const [allLyricsE, setAllLyricsE] = useState("");
    const [lyric, setLyric] = useState("Letras en Español");
    const [lyricE, setLyricE] = useState("Lyrics in English");
    // const counter = useRef(0);
    const [counter, setCounter] = useState(0);
    const [response, setResponse] = useState([]);
    const [grade, setGrade] = useState("Record yourself to see how you did!");
    const [continueDisabled, setContinueDisabled] = useState(false);
    const [start, setStart] = useState(true);

    useEffect(() => {
        fetch(raw)
            .then(r => r.text())
            .then(text => {
                console.log('text decoded:', text);
                setAllLyrics(text);
                // changeLyric();
                // console.log("Lyrics: ", allLyrics);
        });
        fetch(raw2)
            .then(r => r.text())
            .then(text => {
                console.log('text decoded:', text);
                setAllLyricsE(text);
                // changeLyric();
                // console.log("Lyrics: ", allLyrics);
        });
    }, [])

    useEffect (() => {
        messageGrade();
    }, [response]);

    async function changeLyric() {
        setContinueDisabled(true);
        setStart(false);
        setGrade("Record yourself to see how you did!");
        incrementCounter();
        setLyric(allLyrics.split('\n')[counter] + "\n" + allLyrics.split('\n')[counter + 1]);
        setLyricE(allLyricsE.split('\n')[counter] + "\n" + allLyricsE.split('\n')[counter + 1]);
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
            setGrade("Your pronunciation was a bit off. Try again!");
        }
        else {
            setGrade("didn't work");
        }

        if (response >= 40) {
            setContinueDisabled(true);
        }
    }


    return (
    <div className="App">
        
        
      <header className="App-header">
        
        <div className="center">
            Play The Song!
            <YouTubePlayer videoId='a8Rwz6zBJSE' presetPoints={presetPoints} /> 
        </div>
            

            <div className="lyric">
                <div>{lyric}</div>
                <div>--------------------</div>
                <div>{lyricE}</div>
            </div>
            <div className="recordHolder">
                <div className="record" id="recButton"></div>
                <button className="recordButton" onClick={submit}>Record</button>
            </div>
            
            <div className="grade">{grade}</div>
            {/* <button className="lyric" onClick={messageGrade}>Submit</button> */}
            <div className= "right">
                <button disabled={continueDisabled} className= "button-27" onClick={changeLyric}>{start ? "Start Singing" : "Next Lyric"}</button>
                {/* <button class="button-36" role="button">Button 36</button> */}
            </div>
      </header>
    </div>
    )
}

export default Play;