import React, { useState } from 'react'
import Filtro from '../../Componentes/Filtro'
import Input from '../../Componentes/Input'
import Botao from '../../Componentes/Botao'
import { HiMagnifyingGlass } from "react-icons/hi2";
import { Link } from 'react-router-dom';

function Criterios() { //TELA PARA CADASTROS DE CRITERIOS

    let curso = ['Digital Solutions', 'Mecatrônica', 'Manufatura Digital']
    let semestre = ['1° Semestre', '2° Semestre', '3° Semestre']

    const [criterio, setCriterio] = useState('')
    const [turma, setTurma] = useState('')
    const [descricao, setDescricao] = useState('')
    const [semes, setSemes] = useState('')
    const [editcriterio, setEditcriterio] = useState('')

    const cadastrar = (e) => {
        console.log('criterio:', criterio)
        console.log('turma:', turma)
        console.log('Descrição:', descricao)
        console.log('Semestre:', semes)
        console.log('Criterio editado:', editcriterio)
    }

    const pesquisar = () => {
        console.log('Pesquisa feita')
    }
    const excluir = () => {

        var nomecriterio = prompt('Digite o nome do critério para excluí-lo')

        if (nomecriterio == null || nomecriterio == "") {
            alert("O uso do prompt foi cancelado!");
        }
        else{
            alert(nomecriterio + " excluído com sucesso!"
            )
        }

    }


    return (
        <div className={`flex flex-col md:h-full lg:h-full justify-around mx-10 gap-3 mt-5`}>
            <h1 className={`text-2xl font-roboto font-bold`}>CRITÉRIO</h1>
            <h2 className={`text-lg font-roboto font-bold`}>Cadastrar critério</h2>
            <p className={`text-base font-roboto font-semibold`}>Preencha as informações abaixo para adicionar um novo critério: </p>
            <Filtro id="curso" label='Selecione o curso que possui esse critério.' optionList={curso} value={turma} onChange={(e) => { setTurma(e.target.value) }}></Filtro>
            <Input label='Nome do critério' value={criterio} onChange={(e) => { setCriterio(e.target.value) }}></Input>
            <Input label='Descrição do critério: ajuda o aprendiz ou instrutor a saber mais informações' value={descricao} onChange={(e) => { setDescricao(e.target.value) }}></Input>
            <Filtro id="semestre" label='Selecione o(os) semestre(s) que esse critério deve aparecer.' optionList={semestre} value={semes} onChange={(e) => { setSemes(e.target.value) }}></Filtro>
            <div className={'flex justify-end'}>
                <Botao txt='CADASTRAR' onClick={cadastrar}></Botao>
            </div>
            <h2 className={`text-lg font-bold font-roboto`}>Editar ou excluir critério</h2>
            <div className={'flex items-center gap-2'}>
                <Input label='Pesquise pelo critério que deseja editar ou excluir' value={editcriterio} onChange={(e) => { setEditcriterio(e.target.value) }}></Input>
                <Link onClick={pesquisar}><HiMagnifyingGlass className={`size-8 fill-blue-400 mt-5`} /></Link>
            </div>
            <div className={`w-full h-20 bg-barraedit flex gap-36 justify-center items-center sm:gap-10  sm:pl-2 sm:pr-2 `}>
                <p className={`text-base font-bold font-roboto sm:text-sm  lg:text-base xl:text-xl`}>Inglês</p>
                <p className={`text-base font-bold font-roboto sm:text-sm lg:text-base xl:text-xl`}>Técnico em Desenvolvimento de Sistemas </p>
                <p className={`text-base font-bold font-roboto sm:text-sm lg:text-base xl:text-xl`}>Vanessa Silva </p>
                <Link to='/Editar_criterio'><p className={`text-base font-bold font-roboto sm:text-sm lg:text-base xl:text-xl`}>EDITAR </p></Link>
                <Link onClick={excluir}><p className={`text-base font-bold font-roboto sm:text-sm lg:text-base xl:text-xl`}>EXCLUIR </p></Link>

            </div>
        </div>
    )
}

export default Criterios
