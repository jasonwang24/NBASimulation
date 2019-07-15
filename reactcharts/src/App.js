import React,{Component} from 'react';
import logo from './logo.svg';
import title from './title.svg';
import raptors from './raptors.svg';
import warriors from './warriors.svg';
import './App.css';
import Chart from './components/Chart';

class App extends Component {

constructor() {
  super();
  this.state={
    chartData:{}
  }
}

componentWillMount(){
  this.getChartData();
}

getChartData() {
  //ajax calls here
  this.setState({
    chartData:{
      labels:['4 games','5 games','6 games','7 games'],
      datasets:[
        {
          label:'Raptors',
          data:[
            5.1,
            12.8,
            14.4,
            12.6
          ],
          backgroundColor:[
            'rgba(255, 0,0)',
            'rgba(255, 0,0)',
            'rgba(255, 0,0)',
            'rgba(255, 0,0)'
          ]
        },
        {
          label:'Warriors',
          data:[
            7.8,
            14.4,
            21.3,
            11.6
          ],
          backgroundColor:[
            'rgba(255, 223,0)',
            'rgba(255, 223,0)',
            'rgba(255, 223,0)',
            'rgba(255, 223,0)'
          ]
        }
      ],
    }
  });
}

render() {
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
      <Chart chartData={this.state.chartData} legendPosition="bottom"/>
    </div>
  );
}
}

export default App;
