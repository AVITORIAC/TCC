import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';
import { Line} from 'react-chartjs-2';
import React from 'react';
 
 
ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);
 
const labels = ["inglês", "Profissionalismo", "Provas", "Empatia","inglês", "Conecimento Tecnico", "Organização"]
 
const options = {};
 
export const data = {
    labels,
    datasets: [
        {
            label: "1 - semestre",
            data: [4, 1, 3, 1, 2, 3, 1, 4],
            backgroundColor: "#2196F3",
            borderColor: "#2196F3",
        },
        {
            label: "2 - semestre",
            data: [1, 3, 3,5 , 3, 2, 3, 1, 3, 3],
            backgroundColor: "#F44236",
            borderColor: "#F44236",
        },
        {
            label: "3 - semestre",
            data: [ 2, 3, 4, 3, 1, 4, 5, 2],
            backgroundColor: "#FFCA29",
            borderColor: "#FFCA29",
        },
    ],
}
 
 
const Chart = () => {
 
    return (
        <div style={{width: 1000, height:450}}>
           <Line options={options} data={data} />
        </div>
    )
}
 
export default Chart





