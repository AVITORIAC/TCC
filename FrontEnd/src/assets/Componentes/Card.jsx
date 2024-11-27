import React from 'react'
import { IoIosArrowForward } from "react-icons/io";
import { Link, useNavigate } from 'react-router-dom'

function Card({ azul1, azul2, azul3, verde1, verde2, verde3, verde4, h1, h2, p }) {
    //CARDS COLORIDOS 
    
    const cores = `
    ${azul1 ? 'bg-cardA1' : ''}
    ${azul2 ? 'bg-cardA2' : ''}
    ${azul3 ? 'bg-cardA3' : ''}
    ${verde1 ? 'bg-cardV1' : ''}
    ${verde2 ? 'bg-cardV2' : ''}
    ${verde3 ? 'bg-cardV3' : ''}
    ${verde4 ? 'bg-cardV4' : ''}`;


    return (
        <div className={`h-60 w-96 flex items-center${cores}`}>
            <div>
                <h1 className={` text-lg text-white font-semibold mt-2 ml-5`}>{h1}</h1>
                <h2 className={` text-xl text-white font-semibold mt-5 ml-5`}>{h2}</h2>
                <p className={` text-base text-white mt-3 ml-5`}>{p}</p>
            </div>
            <IoIosArrowForward className={`fill-white size-9 mr-4`}></IoIosArrowForward>
        </div>
    )
}

export default Card
