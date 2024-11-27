import React, { useState } from "react";
import Filtro from '../../Componentes/Filtro'
import Botao from '../../Componentes/Botao'
import { Link } from 'react-router-dom'
import Chart from "../../Componentes/Chart";


function Rendimento_instrutor() { //TELA PARA VISUALIZAR O RENDIMENTO DO APRENDIZ

  let turma = ['DS 6', 'DS 7', 'DS 8', 'DS 9', 'DS 10']
  let aprendiz = ['Eduarda Rabelo Oliveira', 'Julia Roberta Veloso Guiraldeli', 'Carlos Eduardo Faustino Barbosa']
  let tipo = ['Auto Avaliação', 'Avaliação']
  let criterios = ['Profissionalismo', 'ingles', 'Conhecimento teorioco']
  let aprendiz2 = ['Eduarda Rabelo Oliveira', 'Julia Roberta Veloso Guiraldeli', 'Carlos Eduardo Faustino Barbosa']


  const [turmas, setTurmas] = useState('')
  const [aluno, setAluno] = useState('')
  const [tipos, setTipos] = useState('')
  const [criterio, setCriterio] = useState('')
  const [aluno2, setAluno2] = useState('')

  const finalizar = (e) => {
    console.log('turma:', turmas)
    console.log('Aprendiz:', aluno)
    console.log('tipos:', tipos)
    console.log('criterio:', criterio)
    console.log('aluno2:', aluno2)
  }
  return (
    <div className={`w-full justify-center sm:w-full sm:p-6 md:w-full md:p-8 lg:w-full lg:p-10 xl:w-full xl:p-10 `}>
      <h1 className={`text-2xl font-bold font-roboto`}>RENDIMENTO</h1>
      <p className={`text-base font-semibold font-roboto pt-4`}>Utilize os filtros para comparar alunos de acordo com critérios específicos. </p>
      <div className={'flex  flex-row gap-5 p-5 sm:flex-col md:flex-col lg:flex-col xl:flex-row 2xl:justify-items-center lg:justify-evenly'}>
        <Filtro id='turma' label='Selecione a turma' optionList={turma} value={turmas} onChange={(e) => (setTurmas(e.target.value))}></Filtro>
        <Filtro id='aprendiz' label='Selecione o aprendiz' optionList={aprendiz} value={aluno} onChange={(e) => (setAluno(e.target.value))}></Filtro>
        <Filtro id='semestre' label='Selecione o tipo de criterio' optionList={tipo} value={tipos} onChange={(e) => (setTipos(e.target.value))}></Filtro>
      </div>
      <div className={'flex  flex-row gap-5 p-5 sm:flex-col md:flex-col lg:flex-col xl:flex-row 2xl:justify-items-center lg:justify-evenly'}>
        <Filtro id='semestre' label='Selecione outro aprendiz' optionList={aprendiz2} value={aluno2} onChange={(e) => (setAluno2(e.target.value))}></Filtro>
        <Filtro id='semestre' label='Selecione um critério' optionList={criterios} value={criterio} onChange={(e) => (setCriterio(e.target.value))}></Filtro>
        <div className={'flex w-80 justify-end items-end sm:justify-normal'}>
          <Link><Botao txt='FINALIZAR' onClick={finalizar}></Botao></Link>
        </div>
      </div>
 
      <div className={'flex justify-center mt-5 sm:w-full'}>
        <Chart />
      </div>
 
    </div>
  )
}

export default Rendimento_instrutor