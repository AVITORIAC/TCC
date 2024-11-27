import React from 'react'

function InputRoxo(props) { // INPUT COM BORDA ROXA
    return (
        <div>
            <label className="block text-base font-medium leading-6 mb-2 text-gray-900">{props.label}</label>
            <input value={props.value} onChange={props.onChange} type={props.type} className="block font-roboto w-80 sm:w-52 xl:w-80 xl:h-10 py-1.5 pl-2 ring-1  ring-roxo placeholder:text-black md:text-sm" placeholder="Insira um texto"/>
        </div>
    )
}

export default InputRoxo
