import React, {useEffect, useRef, useState, Fragment} from "react";
import "./App.css";
import { Input, Button, Container, Row } from "reactstrap";
import ml5 from "ml5"
import P5 from "p5"
import useInterval from '@use-it/interval';
// import P5Wrapper from 'react-p5-wrapper';
let classifier;
let modelURL = 'https://teachablemachine.withgoogle.com/models/RmpzfNMxd/';

function App() {
  const audioRef = useRef();
  const [start, setStart] = useState(false);
  const [result, setResult] = useState([]);
  const [loaded, setLoaded] = useState(false);
  const serverUrl = "http://localhost:5000";

  useEffect(() => {
    classifier = ml5.soundClassifier(modelURL+'model.json', () => {
      navigator.mediaDevices
        .getUserMedia({ video: false, audio: true })
        .then((stream) => {
          audioRef.current.srcObject = stream;
          audioRef.current.play();
          setLoaded(true);
        });
    });
  }, []);

  useInterval(() => {
    if (classifier && start) {
      classifier.classify(audioRef.current, (error, results) => {
        if (error) {
          console.error(error);
          return;
        }
        setResult(results);
        // POST HERE
        let urlToFetch = serverUrl + "/update/" + 1 + "/" + results[0].label + "/" + results[0].confidence;
        fetch(urlToFetch, { method: "POST", }).then((response) => {
          return response.json().then((object) => {
            // setState({
            //   entries: Object.entries(object),
            // });
          });
        });
        // console.log("update running");
        console.log(results[0].label)
      });
    }
  }, 500);

  const toggle = () => {
    setStart(!start);
    setResult([]);
  }

  return (
    <div className="container">
      <div className="upper">
        <div className="capture">
          <video
            ref={audioRef}
            style={{ transform: "scale(-1, 1)" }}
            width="300"
            height="150"
          />
          {loaded && (
            <button onClick={() => toggle()}>
              {start ? "Stop" : "Start"}
            </button>
          )}
        </div>
        {result.length > 0 && (
          <div>
            <ul>
               <span>
                 {Object.values(result[0])}
                 <br></br>
                 {Object.values(result[1])}
                 <br></br>
                 {Object.values(result[2])}
               </span>
         </ul>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;