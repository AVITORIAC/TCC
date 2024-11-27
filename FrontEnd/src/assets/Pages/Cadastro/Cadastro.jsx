import React from 'react'
import fundo from '../../Imgs/Fundo.jpg'
import CardCadastro from '../../Componentes/CardCadastro'


function Cadastro() { //TELA DE ESCOLHA DO CARGO PARA CADASTRO
    return (
      <div className={'flex items-center sm:h-screen md:h-screen lg:h-screen xl:h-screen 2xl:h-screen justify-center '}>
        <img src={fundo} className={'w-full sm:h-screen md:h-screen lg:h-screen xl:h-screen 2xl:h-screen flex absolute'} alt="" />
        <CardCadastro></CardCadastro>
      </div>
    )
  }


  export default Cadastro
