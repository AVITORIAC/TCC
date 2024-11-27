import React from 'react'

function Filtro(props) { // INPUT DE FILTRO COM BORDA AZUL 
    
    return (
        <div>
            <label for="filtro" className="block text-base font-roboto font-medium mb-2 text-gray-900">{props.label}</label>
            <select value={props.value} onChange={props.onChange} class="block w-80  py-1.5 pl-2 font-roboto text-black ring-1 " >
                {props.optionList.map((val) => (
                    <>
                        <option value={val}>{val}</option>
                    </>
                ))}
            </select>
        </div>
    )
}

export default Filtro


