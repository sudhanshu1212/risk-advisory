import { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, Title, Tooltip, LineElement, Legend, CategoryScale, LinearScale, PointElement, Filler } from 'chart.js';
import { json } from 'react-router-dom';
ChartJS.register(
    Title, Tooltip, LineElement, Legend,
    CategoryScale, LinearScale, PointElement, Filler
)

function App() {
    const [values, setvalue] = useState("10282")
    const [data, setData] = useState(
        {
            labels: [],
            datasets: [
                {
                    
                    label: "Date / Price",
                    data: [],
                    backgroundColor: 'yellow',
                    borderColor: 'green',
                    tension: 0.4,
                    fill: true,
                    pointStyle: 'rect',
                    pointBorderColor: 'blue',
                    pointBackgroundColor: '#fff',
                    showLine: true
                }
            ]
        }
    )
    const ShowGraph = () => {
        console.log("showgraph",values)
        
            const y = [];
            const x = [];
            fetch('http://localhost:8000/returns/')
                .then(response => response.json())
                .then(json => {
                    console.log("json", json)
                    json.map((item, index) => {
                        if (item.equity_id == values) {
                            // console.log("hiihihihihihihih",values)
                            y.push(item.open)
                            x.push(item.date)
                        }
                        
                        

                    })
                    setData(
                        {
                            labels: x,
                            datasets: [
                                {
                                    label: "Date / Price",
                                    data: y,
                                    backgroundColor: 'yellow',
                                    borderColor: 'green',
                                    tension: 0.4,
                                    fill: true,
                                    pointStyle: 'rect',
                                    pointBorderColor: 'blue',
                                    pointBackgroundColor: '#fff',
                                    showLine: true
                                }
                            ]
                        }
                    )
                }
                )
            console.log("arr", y)


    }

    return (
        
        <div className="App" style={{ alignContent:'center',margin:"20px"}}>
            <h1>Click button to see graph</h1>
            <input
                type="text"
                className="form-control form-control-lg"
                placeholder="Enter ID"
                name="values"
                value={values}
                onChange={(e) => setvalue(e.target.value)}

            />
            <button onClick={ShowGraph}>click to see for specifc data</button>
            <Line data={data}>Hello</Line>
        
            
            
        </div>
    );
}

export default App;