import React, { useState } from "react";
import axios from "axios";
import "./App.css"; // Assuming you will create a separate CSS file for styling

const HumorApp = () => {
  const [text, setText] = useState("");
  const [theme, setTheme] = useState("");
  const [joke, setJoke] = useState("");
  const [isHumor, setIsHumor] = useState(null);

  const detectHumor = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:5000/detect-humor", {
        text,
      });
      setIsHumor(response.data.is_humor);
    } catch (error) {
      console.error("Error detecting humor:", error);
    }
  };

  const generateJoke = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:5000/generate-joke", {
        theme,
      });
      setJoke(response.data.joke);
    } catch (error) {
      console.error("Error generating joke:", error);
    }
  };

  return (
    <div className="app-container">
      <h1>😂 Humor Detector & Joke Generator 🤣</h1>

      {/* Humor Detection */}
      <div className="section">
        <h2>Detect Humor</h2>
        <input
          type="text"
          className="input-field"
          placeholder="Enter text"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        <button className="button" onClick={detectHumor}>
          Check
        </button>
        {isHumor !== null && (
          <p className={isHumor ? "funny" : "not-funny"}>
            {isHumor ? "😂 It's funny!" : "😐 Not funny."}
          </p>
        )}
      </div>

      {/* Joke Generation */}
      <div className="section">
        <h2>Generate Joke</h2>
        <input
          type="text"
          className="input-field"
          placeholder="Enter joke theme"
          value={theme}
          onChange={(e) => setTheme(e.target.value)}
        />
        <button className="button" onClick={generateJoke}>
          Generate
        </button>
        {joke && <p className="generated-joke">🤣 {joke}</p>}
      </div>
    </div>
  );
};

export default HumorApp;
