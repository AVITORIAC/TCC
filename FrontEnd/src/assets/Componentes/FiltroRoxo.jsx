import React from 'react'

function FiltroRoxo(props) { //INPUT DE FILTRO COM BORDA ROXA 
    return (
        <div>
            <label className="block text-base font-medium leading-6 mb-2 text-gray-900">{props.label}</label>
            <select value={props.value} onChange={props.onChange} className="block font-roboto w-80 sm:w-52 xl:w-80 xl:h-10 py-1.5 pl-2 placeholder:text-black ring-1  ring-roxo sm:text-sm">
                <option value="turma">Selecionar</option>
                {props.optionList.map((option) => (
                    <option key={option.id} className='md:text-sm'>{option.nome}</option>
                ))}
            </select>
        </div>
    )
}

export default FiltroRoxo