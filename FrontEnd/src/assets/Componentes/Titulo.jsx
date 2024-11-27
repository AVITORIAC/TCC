import React from 'react'

function Titulo({h1}) { //TITULOS
  return (
    <div>
      <h1 className={'text-black font-bold text-2xl sm:text-xl 2xl:text-2xl'}>{h1}</h1>
    </div>
  )
}

export default Titulo
