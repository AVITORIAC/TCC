import React, { useState } from 'react'
import Botaoroxo from './Botaoroxo'
import InputRoxo from './InputRoxo'
import Titulo from './Titulo'
import logoBosch from '../Imgs/logoBosch.png'
import { Link } from 'react-router-dom'

function CardCadastro_Gestor() { //CARD PARA CADASTRO DO GESTOR

    const [nome, setNome] = useState('')
    const [email, setEmail] = useState('')
    const [edv, setEdv] = useState('')
    const [senha, setSenha] = useState('')
    const [confirmar, setConfirmar] = useState('')

    const cadastrar = (e) => {
        console.log('nome:', nome)
        console.log('email:', email)
        console.log('senha:', senha)
        console.log('confirmar:', confirmar)
    }

    return (
        <div className={'bg-white relative mt-20 w-9/12 h-full xl:h-5/6 2xl:w-7/12 3xl:w-6/12 pb-8 sm:w-3/6 sm:h-fit sm:mt-5 md:w-4/6 '}>
            <img className={'sm:w-32 xl:w-56'} src={logoBosch} alt="" />
            <div className={'flex justify-center mt-7 mb-8 sm:mt-1 sm:mb-1 2xl:mb-8 2xl:mt-10'}>
                <Titulo h1='CADASTRO'></Titulo>
            </div>
            <div className={'flex justify-evenly items-center sm:flex-col md:flex-row lg:flex-row 2xl:p-3'}>
                <div className={'flex flex-col gap-8 sm:gap-3 sm:w-min sm:text-xs lg:text-lg 2xl:gap-6'}>
                    <InputRoxo label='Nome completo' value={nome} onChange={(e) => { setNome(e.target.value) }}> </InputRoxo>
                    <InputRoxo label='Email' value={email} onChange={(e) => { setEmail(e.target.value) }}> </InputRoxo>
                    <InputRoxo label='EDV' value={edv} onChange={(e) => { setEdv(e.target.value) }}> </InputRoxo>
                </div>
                <div className={'flex flex-col gap-8 sm:p-3 sm:gap-3 sm:text-xs lg:text-lg 2xl:gap-6'}>
                    <InputRoxo type='password' label='Senha ' value={senha} onChange={(e) => { setSenha(e.target.value) }}> </InputRoxo>
                    <InputRoxo type='password' label='Confirma senha' value={confirmar} onChange={(e) => { setConfirmar(e.target.value) }}> </InputRoxo>
                </div>
            </div>
            <div className={'flex justify-center mt-10 sm:mt-2 md:mt-7'}>
                <Botaoroxo onClick={cadastrar} txt='CRIAR'></Botaoroxo>
            </div>
 
        </div> 
    )
}

export default CardCadastro_Gestor
