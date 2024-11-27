import React, { useEffect, useState } from 'react'
import Botaoroxo from './Botaoroxo'
import InputRoxo from './InputRoxo'
import Titulo from './Titulo'
import logoBosch from '../Imgs/logoBosch.png'
import FiltroRoxo from './FiltroRoxo'
import axios from 'axios'
import { useStore } from '../store'


function CardCadastro_Aprendiz(props) { //CARD PARA CADASTRO DO APRENDIZ
    const {url, cargoCadastro} = useStore() // url da api
    const [nome, setNome] = useState('')
    const [edv, setEdv] = useState('')
    const [email, setEmail] = useState('')
    const [turma, setTurma] = useState('')
    const [turmaId, setTurmaId] = useState(0)
    const [senha, setSenha] = useState('')
    const [confirmarSenha, setConfirmarSenha] = useState('')
    const [listaTurmas, setListaTurmas] = useState([])

    // traz a lista de turmas da api e cria outra lista só com os nomes das turmas
    const listarTurmas = async () => {
        try {
            const response = await axios.get(`${url}/turma`)
            console.log(response.data)
            setListaTurmas(response.data)
        } catch (error) {
            console.log(error)
        }
    }

    // chama a função de listar turmas ao carregar o componente
    useEffect(() => {
        listarTurmas()
    }, [])

    // função que busca o id da turma, que será usado para enviar para a api
    // const obterIdTurma = () => {
    //     for(let i = 0; i < listaTurmas.length; i++){
    //         if(listaTurmas[i].nome == turma){
    //             setTurmaId(listaTurmas[i].id)
    //         }
    //     }
    //     return alert("Turma não encontrada.")
    // }
    
    // função que cadastra um usuário na api
    const cadastrar = async (e) => {
        e.preventDefault()
        try {
            // verifica se todos os campos foram preenchidos
            if (turma == '' || nome == '' || edv == '' || email == '' || senha == '' || confirmarSenha == '') {
                alert('Preencha todos os campos!')
            }
            else {  
                const response_turma = await axios.get(`http://127.0.0.1:8000/api/v1/turma/?turma:${turma}`)
                setTurmaId(response_turma.data[0].id)
                 
                const response = await axios.post(`${url}/usuario/`, {
                    edv: edv,
                    email: email,
                    nome: nome,   
                    cargo: cargoCadastro,
                    idTurma: turmaId,
                    logado: false,
                    password: senha,
                    password_confirm: confirmarSenha
                })
                alert(response.data.mensagem) // retornando a mensagem da api
                console.log(response)
            }
        }
        catch (error) {
            console.error(error)
        }
    }

    return (
        <div className={' bg-white relative mt-20 w-9/12 h-full sm:w-3/6 sm:h-fit sm:mt-2 lg:w-4/6 xl:h-5/6 2xl:w-7/12 3xl:w-6/12 pb-8 '}>
            <img className={'sm:w-32 xl:w-56'} src={logoBosch} alt="" />
            <div className={'flex justify-center mt-7 mb-8 sm:mt-1 sm:mb-1 2xl:mb-8 2xl:mt-10'}>
                <Titulo h1='CADASTRO'></Titulo>
            </div>
            <div className={'flex justify-evenly items-center sm:flex-col sm:text-xs xl:h-3/6 lg:flex-row 2xl:p-3 '}>
                <div className={'flex flex-col gap-8 sm:gap-3 sm:text-xs md:gap-2 lg:text-xl 2xl:gap-6'}>
                    <InputRoxo label='Nome completo' value={nome} onChange={(e) => { setNome(e.target.value) }}> </InputRoxo>
                    <InputRoxo label='EDV' value={edv} onChange={(e) => { setEdv(e.target.value) }}> </InputRoxo>
                    <InputRoxo label='Email' value={email} onChange={(e) => { setEmail(e.target.value) }}> </InputRoxo>
                </div>
                <div className={'flex flex-col gap-8 sm:gap-3 sm:p-2 md:gap-2 sm:text-xs lg:text-lg 2xl:gap-6'}>
                    <FiltroRoxo id="turma" label='Selecione a turma:' value={turma} optionList={listaTurmas} onChange={(e) => {setTurma(e.target.value)
                        console.log(e.target.value)
                        // obterIdTurma
                    }}></FiltroRoxo>
                    <InputRoxo type='password' label='Senha ' value={senha} onChange={(e) => { setSenha(e.target.value) }}> </InputRoxo>
                    <InputRoxo type='password' label='Confirma senha' value={confirmarSenha} onChange={(e) => { setConfirmarSenha(e.target.value) }}> </InputRoxo>
                </div>
 
            </div>
            <div className={'flex justify-center mt-10 sm:mt-1 md:mt-2'}>
                <Botaoroxo txt='CRIAR' onClick={cadastrar}></Botaoroxo>
            </div>
 
        </div>
    )
}

export default CardCadastro_Aprendiz


