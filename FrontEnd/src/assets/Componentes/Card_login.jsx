import React, {useEffect, useState} from 'react'
import Botaoroxo from './Botaoroxo'
import InputRoxo from './InputRoxo'
import Titulo from './Titulo'
import logoBosch from '../Imgs/logoBosch.png'
import { Link, useNavigate } from 'react-router-dom'
import axios from 'axios'
import { useStore } from '../store' // variaveis globais, acessar em todas as páginas


function Card_login() { //CARD PARA TELA DE LOGIN 
    // armazenando os dados de login do usuário
    const [edv, setEdv] = useState()
    const [senha, setSenha] = useState("")
    let navigate = useNavigate()
    const {setId, setToken, setCargo, setCurso, url} = useStore() // puxando as variáveis globais

    const fazer_login = async(e) => { // async -> função assincrona
        try{
            // post: url e json
            const response = await axios.post(`${url}/login/`, {
                edv: edv,
                password: senha
            })
            // guardando as informações do usuário logado
            setToken(response.data.token)   
            setId(response.data.id)
            setCargo(response.data.cargo)
            setCurso(response.data.curso)
            
            switch(response.data.cargo) {
                case 'instrutor':
                    return navigate('/HomeIns')
                case 'aprendiz':
                    return navigate('/Home_aprendiz')
                case 'gestor':
                    return navigate('/RendimentoGestor')
                case 'administrador':
                    return navigate('/HomeAdmin')
                default:
                    return navigate('/Login')
            }
        }
        // tratamento de erros
        catch (error){
            console.error(error)
            alert("Informações incorretas!") // avisar do usuário
        }
    }

    return (
        <div className={'bg-white relative mt-20 w-9/12 h-full xl:h-5/6 2xl:w-7/12 3xl:w-6/12 pb-8 sm:w-4/6 sm:h-fit sm:mt-2 md:w-5/6 md:mt-2 md:h-fit'}>
            <img className={'sm:w-32 xl:w-56'} src={logoBosch} alt="" />
            <div className={'flex flex-col items-center'}>
                <div className={'flex mt-10 mb-8'}>
                    <Titulo h1='LOGIN'></Titulo>
                </div>
                <div className={'flex flex-col gap-5 items-center'}>

                    <InputRoxo label='EDV' value={edv} onChange={(e) => {setEdv(e.target.value)}}> </InputRoxo>
                    <InputRoxo type='password' label='Senha' value={senha} onChange={(e) => {setSenha(e.target.value)}}> </InputRoxo>

                    <Botaoroxo txt='ENTRAR' onClick={fazer_login}></Botaoroxo>
                </div>
            </div>
            <div className={'flex gap-2 justify-center mt-10'}>
                <p> Esqueceu a senha?</p>
                <Link to='/RecuperarEdv'><p className={'underline decoration-solid '}> Recuperar</p></Link>
            </div>
            <div className={'flex gap-2 justify-center mt-3 sm:'}>
                <p> Ainda não possui uma conta? </p>
                <Link to='/Cadastro'> <p className={'underline decoration-solid '}> Cadastre-se </p></Link>
            </div>
        </div>
    )
}

export default Card_login
