import React from 'react'
import Botaoroxo from './Botaoroxo'
import InputRoxo from './InputRoxo'
import Titulo from './Titulo'
import logoBosch from '../Imgs/logoBosch.png'

function CardNovaSenha() { //CARD PARA TELA DE NOVA SENHA
    return (
        <div className={'bg-white relative  mt-20 w-9/12 h-full sm:w-4/6 sm:h-4/6 sm:mt-2 xl:h-5/6 2xl:w-7/12 3xl:w-6/12 pb-8   '}>
            <img className={'sm:w-36 xl:w-56'} src={logoBosch} alt="" />
            <div className={'flex flex-col items-center'}>
                <div className={'flex mt-10 mb-8'}>
                    <Titulo h1='NOVA SENHA'></Titulo>
                </div>
                <div className={'flex flex-col gap-5 items-center sm:gap-11 '}>
                    <InputRoxo type='password' label='Digite a nova senha'> </InputRoxo>
                    <InputRoxo type='password' label='Confirme a nova senha'> </InputRoxo>
                    <Botaoroxo txt='ENTRAR'></Botaoroxo>
                </div>
            </div>
        </div>
    )
}

export default CardNovaSenha
