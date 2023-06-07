import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import React, { useState, useEffect } from 'react';


function App() {
const [a, setA ] = useState('')
const [b, setB ] = useState('')
  useEffect(()=>{
    axios
      .get('http://20.243.57.42:8000/')
      //.get("http://localhost:8000/")
      //.get('http://api0602:8000/')
      //.get('http://172.18.0.3:8000/')
      //.get("http://0.0.0.0:8000/")
      //.get("http://127.0.0.1:8000/")
      .then((res)=>{setA(res.data)})
  },[])
  //useEffect(()=>{
  //  axios
  //    .get('http://20.243.57.42:8000/')
  //    .get("http://localhost:8000/")
  //    .get('http://api0602:8000/')
  //    .get('http://172.18.0.3:8000/')
  //    .get("http://0.0.0.0:8000/")
  //    .get("http://127.0.0.1:8000/")
  //    .then((res)=>{setB(res.data)})
  //},[])  console.log("a :", b)

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
	<div>t : {a.Hello}</div>
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
      </header>
    </div>
  );
}

export default App;
