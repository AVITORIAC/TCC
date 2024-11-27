import React from 'react'
import fundo from '../../Imgs/Fundo.jpg'
import CardEdv from '../../Componentes/CardEdv'

function RecuperarEdv(){
    return (
        <div className={'flex items-center sm:h-screen md:h-screen lg:h-screen xl:h-screen 2xl:h-screen justify-center'}>
            <img src={fundo} className={'w-full sm:h-screen md:h-screen lg:h-screen xl:h-screen 2xl:h-screen flex absolute'} alt="" />
            <CardEdv></CardEdv>
        </div>
    )
}

export default RecuperarEdv