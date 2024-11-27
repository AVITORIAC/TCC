import React, { useState } from "react";
import Filtro from '../../Componentes/Filtro'
import Botao from '../../Componentes/Botao'
import { Link } from 'react-router-dom'
 
 
function Avaliacao_feedback() { //TELA PARA VISUALIZAR A AUTO AVALIAÇÃO DO APRENDIZ
 
  let turma = ['DS 6', 'DS 7', 'DS 8', 'DS 9', 'DS 10']
  let aprendiz = ['Eduarda Rabelo Oliveira', 'Julia Roberta Veloso Guiraldeli', 'Carlos Eduardo Faustino Barbosa']
  let semestre = ['1° Semestre', '2° Semestre', '3° Semestre']
 
  const [turma1, setTurma1] = useState('')
  const [aluno, setAluno] = useState('')
  const [semes, setSemes] = useState('')
 
  const finalizar = (e) => {
    console.log('turma:', turma1)
    console.log('Aprendiz:', aluno)
    console.log('semestre:', semes)
}
  return (
    <div className={`flex flex-col h-full gap-4 mt-10 mx-10`}>
      <h1 className={`text-2xl font-bold`}>AUTO AVALIAÇÃO</h1>
      <Filtro id='turma' label='Selecione a turma' optionList={turma} value={turma1} onChange={(e) => (setTurma1(e.target.value))}></Filtro>
      <Filtro id='aprendiz' label='Selecione o aprendiz' optionList={aprendiz} value={aluno} onChange={(e) => (setAluno(e.target.value))}></Filtro>
      <Filtro id='semestre' label='Selecione o semestre' optionList={semestre} value={semes} onChange={(e) => (setSemes(e.target.value))}></Filtro>
      <div className={'flex justify-end'}>
      <Link><Botao txt='FINALIZAR' onClick={finalizar}></Botao></Link>
      </div>
    </div>
  )
}
 
export default Avaliacao_feedback