import React,{Component} from 'react';
import{Bar,Pie} from 'react-chartjs-2';

class Chart extends Component{

  constructor(props){
    super(props);
    this.state={
      chartData:{
        labels:['4','5','6','7'],
        datasets:[
          {
            label:'Raptors',
            data:[
              10,
              20,
              30,
              40
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
              10,
              20,
              30,
              40
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
    }
  }

  render(){
    return(
      <div className="chart">
      <Bar
        data={this.state.chartData}
        options={{
            title:{
              display:true,
              text:'NBA Finals Outcome Simulations',
              position:'top',
              fontSize:25
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }}
      />
      </div>
    )
  }
}

export default Chart;
