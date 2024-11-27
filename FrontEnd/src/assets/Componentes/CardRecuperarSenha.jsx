import React, { useState } from 'react'
import Botaoroxo from './Botaoroxo'
import InputRoxo from './InputRoxo'
import Titulo from './Titulo'
import logoBosch from '../Imgs/logoBosch.png'


function CardRecuperarSenha() { //CARD PARA TELA DO CODIGO DE RECUPERAÇÃO DE SENHA 
    const [codigo, setCodigo] = useState('')
    const recuperar = (e) => {
        console.log('codigo:' , codigo)
    }
    return (
        <div className={'bg-white relative mt-20 w-9/12 h-full pb-8 sm:w-4/6 sm:h-fit sm:mt-2 md:w-5/6 md:mt-2 md:h-fit xl:h-5/6 2xl:w-7/12 3xl:w-6/12 '}>
            <img className={'sm:w-32 xl:w-56'} src={logoBosch} alt="" />
            <div className={'flex flex-col items-center justify-center h-4/6 xl:gap-8'}>
                <div className={'flex mt-10 mb-3'}>
                    <Titulo h1='RECUPERAR SENHA'></Titulo>
                </div>
                <div className={'flex flex-col gap-5 mt-5 items-center sm:text-center xl:gap-10 '}>
                    <h2 className={'font-semibold sm:text-xs md:text-xl'}>Digite abaixo o código enviado no seu email: allana123@gmail.com <br/> para recuperar sua senha. Caso o código não esteja na sua caixa de entrada, verifique o spam.</h2>
                    <InputRoxo value={codigo} onChange={(e) => {setCodigo (e.target.value)}}> </InputRoxo>
 
                    <Botaoroxo txt='VERIFICAR' onClick={recuperar}></Botaoroxo>
                </div>
            </div>
        </div>
    )
}




export default CardRecuperarSenha
