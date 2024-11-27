import React from 'react'

function Botao(props) { //BOTAO COM BORDA AZUL
  return (
    <div>
      <button onClick={props.onClick} className={`h-12 w-32 border-2 border-fonte text-fonte`}>{props.txt}</button>
    </div>
  )
}

export default Botao
