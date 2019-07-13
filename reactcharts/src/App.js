import React from 'react';
import logo from './logo.svg';
import title from './title.svg';
import raptors from './raptors.svg';
import warriors from './warriors.svg';
import './App.css';
import Chart from './components/Chart';

function App() {
  return (
    <div className="App">
      <header className="Top">
          <img src={title} />
      </header>
      <header className="App-header">
        <img src={raptors} className="App-raptors"/>
        <img src={logo} className="App-logo" alt="logo" />
        <img src={warriors} className="App-warriors"/>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
        </a>
      </header>
      <Chart />
    </div>
  );
}

export default App;
