import React from 'react'
import Botaoroxo from './Botaoroxo'
import Titulo from './Titulo'
import logoBosch from '../Imgs/logoBosch.png'
import { useNavigate } from 'react-router-dom'
import { useStore } from '../store'

    
function CardCadastro() { //CARD PARA TELA DE ESCOLHA DO CARGO PARA CADASTRO
    let navigate = useNavigate()
    const {setCargoCadastro} = useStore()

    return (
        <div className={'bg-white relative mt-20 w-7/12 h-screenP sm:h-5/6 xl:h-4/6 2xl:w-5/12'}>
            <img src={logoBosch} alt="Logo da Bosch"/>
            <div className={'flex flex-col items-center'}>
                <div className={'flex mt-10 mb-14'}>
                    <Titulo h1='SELECIONE SEU CARGO'></Titulo>
                </div>
                <div className={'flex flex-col gap-4 items-center'}>
                    <Botaoroxo txt='APRENDIZ' onClick={() => {
                        navigate('/Cadastro_de_Aprendiz')
                        setCargoCadastro('aprendiz')
                        }}></Botaoroxo>
                    <Botaoroxo txt='INSTRUTOR' onClick={() => {
                        navigate('/CadastroGestor')
                        setCargoCadastro('instrutor')
                        }}></Botaoroxo>
                    <Botaoroxo txt='GESTOR' onClick={() => {
                        navigate('/CadastroGestor')
                        setCargoCadastro('gestor')
                        }}></Botaoroxo>
                </div>
            </div>
        </div>
    )
}

export default CardCadastro