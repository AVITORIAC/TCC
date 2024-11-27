import React, { useState } from 'react'
import Input from '../../Componentes/Input'
import Filtro from '../../Componentes/Filtro'
import Botao from '../../Componentes/Botao'
import { HiMagnifyingGlass } from "react-icons/hi2";
import { Link } from 'react-router-dom';
 
function Cadastro_turma() { //TELA PARA CADASTRO DE TURMAS
  let padrinho = ['Vanessa Silva', 'Leonardo Oliveira', 'Cleber Augusto', 'Edmar Ianella']
  let cursos = ['Digital Solutions', 'Mecatrônica', 'Manufatura Digital']
 
  const [curso, setCurso] = useState('')
  const [turma, setTurma] = useState('')
  const [padrinhos, setPadrinhos] = useState('')
  const [pesquisar, setPesquisar] = useState('')
 
  const cadastrar = (e) => {
    console.log('curso:', curso)
    console.log('turma:', turma)
    console.log('padrinho (a):', padrinhos)
    
  }
  const pesquisa = (e)=> {
    console.log('pesquisa:', pesquisar)
  }
 
  return (
    <div className={`flex flex-col sm:h-full gap-4 mx-10 sm:mb-14 mt-5`}>
      <h1 className={`text-2xl font-bold font-roboto `}>Turmas</h1>
      <h2 className={`text-lg font-bold font-roboto`}>Cadastrar turmas</h2>
      <p className={`text-base font-roboto font-semibold`}>Preencha as informações abaixo para adicionar uma nova turma:</p>
      <Filtro label='Selecione o curso' optionList={cursos} value={cursos} onChange={(e) => {setCurso (e.target.value)}}></Filtro>
      <Input label='Nome da turma' value={turma} onChange={(e) => {setTurma (e.target.value)}}></Input>
      <Filtro label='Selecione o padrinho ou a madrinha' optionList={padrinho} value={padrinhos} onChange={(e) => {setPadrinhos (e.target.value)}}></Filtro>
 
      <div className={'flex justify-end'}>
        <Botao txt='CADASTRAR' onClick={cadastrar}></Botao>
      </div>
      <h2 className={`text-lg font-roboto font-bold`}>Editar turma</h2>
      <div className={'flex items-center gap-2'}>
        <Input label='Pesquise pela turma que deseja editar' value={pesquisar} onChange={(e) => {setPesquisar (e.target.value)}}></Input>
        <Link onClick={pesquisa}><HiMagnifyingGlass className={`size-8 fill-blue-400 mt-5`} /></Link>
      </div>
      <div className={`w-full h-20 bg-barraedit flex gap-40 justify-center items-center sm:gap-10  sm:pl-2 sm:pr-2`}>
        <p className={`text-base font-bold font-roboto sm:text-sm lg:text-base xl:text-xl`}>Digital solutions 6</p>
        <p className={`text-lg font-bold font-roboto sm:text-sm lg:text-base xl:text-xl`}>Técnico em Desenvolvimento de Sistemas </p>
        <p className={`text-lg font-bold font-roboto sm:text-sm lg:text-base xl:text-xl`}>Vanessa Silva </p>
        <Link to='/Editar_turma'><p className={`text-lg font-bold font-roboto sm:text-sm lg:text-base xl:text-xl`}>EDITAR </p></Link>
 
      </div>
    </div>
  )
}
 
export default Cadastro_turma
 