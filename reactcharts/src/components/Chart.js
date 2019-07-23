import React,{Component} from 'react';
import{Bar,Pie} from 'react-chartjs-2';

class Chart extends Component{

  constructor(props){
    super(props);
    this.state={
      chartData:props.chartData
    }
  }

static defaultProps ={
  displayTitle:true,
  displayLegend:false,
  legendPosition:'right'
}

  render(){
    return(
      <div className="chart">
        <Bar
          data={this.state.chartData}
          options={{
              title:{
                display:this.props.displayTitle,
                text:'NBA Finals Outcome Simulations (%)',
                fontSize:40
              },
              scales: {
                  yAxes: [{
                      ticks: {
                          beginAtZero: true
                      }
                  }]
              },
              legend: {
                position:this.props.legendPosition
              }
          }}
        />

        <Pie
          data={this.state.chartData}
          options={{
              title:{
                display:this.props.displayTitle,
                text:'Number of Games to Win (%)',
                fontSize:40
              },
              legend: {
                display:this.props.displayLegend,
              }
          }}
        />

      </div>
    )
  }
}

export default Chart;
