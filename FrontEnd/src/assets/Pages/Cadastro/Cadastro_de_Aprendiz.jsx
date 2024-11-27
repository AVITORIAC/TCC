import React from 'react'
import fundo from '../../Imgs/Fundo.jpg'
import CardCadastro_Aprendiz from '../../Componentes/CardCadastro_Aprendiz'

function Cadastro_de_Aprendiz() { //TELA DE CADASTRO DO APRENDIZ 
    return (
        <div className={'flex items-center sm:h-screen justify-center'}>
            <img src={fundo} className={'w-full sm:h-screen flex absolute'} alt="" />
           <CardCadastro_Aprendiz/>
        </div>
    )
}

export default Cadastro_de_Aprendiz
