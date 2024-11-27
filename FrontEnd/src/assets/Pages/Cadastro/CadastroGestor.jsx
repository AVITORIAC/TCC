import React from 'react'
import fundo from '../../Imgs/Fundo.jpg'
import CardCadastro_Gestor from '../../Componentes/CardCadastro_Gestor'


function CadastroGestor() { //TELA DE CADASTRO DO GESTOR E INSTRUTOR
    return (
        <div className={'flex items-center h-full sm:h-screen justify-center'}>
            <img src={fundo} className={'w-full sm:h-screen flex absolute'} alt="" />
            <CardCadastro_Gestor/>
        </div>
    )
}

export default CadastroGestor
