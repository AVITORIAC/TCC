import React from 'react'
import fundo from '../../Imgs/Fundo.jpg'
import CardNovaSenha from '../../Componentes/CardNovaSenha'

function NovaSenha() { //TELA PARA REDEFINIR NOVA SENHA 
    return (
        <div className={'flex items-center sm:h-screen md:h-screen lg:h-screen xl:h-screen 2xl:h-screen justify-center'}>
            <img src={fundo} className={'w-full sm:h-screen md:h-screen lg:h-screen xl:h-screen 2xl:h-screen flex absolute'} alt="" />
            <CardNovaSenha/>
        </div>
    )
}

export default NovaSenha
