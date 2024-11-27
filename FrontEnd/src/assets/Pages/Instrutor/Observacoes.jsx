import React, { useState } from 'react'
import Filtro from '../../Componentes/Filtro'
import Botao from '../../Componentes/Botao'
import { BsEmojiFrown } from "react-icons/bs";
import { BsEmojiSmile } from "react-icons/bs";

function Observacoes() { //TELA PARA ADICIONAR ANOTAÇÕES SOBRE OS APRENDIZES

  let aprendiz = ['Eduarda Rabelo Oliveira', 'Julia Roberta Veloso Guiraldeli', 'Carlos Eduardo Faustino Barbosa']
  let semestre = ['1° Semestre', '2° Semestre', '3° Semestre']
  let turma = ['DS 6', 'DS 7', 'DS 8', 'DS 9', 'DS 10']

  const [turma1, setTurma1] = useState('')
  const [aluno, setAluno] = useState('')
  const [semes, setSemes] = useState('')
  const [comentario, setComentario] = useState('')
  const [positivo, setPositivo] = useState('')
  const [negativo, setNegativo] = useState('')

  const finalizar = (e) => {
    console.log('turma:', turma1)
    console.log('Aprendiz:', aluno)
    console.log('semestre:', semes)
    console.log('Comentario:', comentario)
  }
  const positivoteste = (e) => {
    console.log('positivo')
  }
  const negativoteste = (e) => {
    console.log('negativo')
  }

  return (
    <div className={`flex flex-col h-full gap-3 mt-6 mx-10 sm:flex-col sm:gap-6 sm:h-fit`}>
      <h1 className={`text-2xl font-bold font-roboto`}>NOTAS</h1>
      <p className={`text-base font-semibold font-roboto`}>Adicione uma observação sobre o aprendiz apontado durante a aula. Por fim, classifique a observação como negativa ou positiva. </p>
      <Filtro id="turma" label='Selecione a turma' optionList={turma} value={turma1} onChange={(e) => (setTurma1(e.target.value))}></Filtro>
      <Filtro id="aprendiz" label='Selecione o aprendiz' optionList={aprendiz} value={aluno} onChange={(e) => (setAluno(e.target.value))}></Filtro>
      <Filtro id="semestre" label='Selecione o semestre' optionList={semestre} value={semes} onChange={(e) => (setSemes(e.target.value))}></Filtro>
 
      <label className=" text-base font-medium font-roboto leading-6 text-gray-900">Descreva a observação</label>
      <textarea className=" flex w-80 h-24 text-black ring-1 placeholder:text-black p-2" placeholder="Insira um texto" value={comentario} onChange={(e) => (setComentario(e.target.value))} ></textarea>
 
      <label className=" text-base font-medium font-roboto text-gray-900">Selecione como é essa nota</label>
      <div className={'flex gap-10'}>
        <div className={'flex gap-3 flex-col items-center'}>
          <BsEmojiSmile className={'fill-green-600 size-10'}></BsEmojiSmile>
          <p className={'flex '}>Ponto positivo</p>
        </div>
        <div className={'flex gap-3 flex-col items-center'}>
          <BsEmojiFrown className={'fill-red-600 size-10'}></BsEmojiFrown>
          <p>Ponto a melhorar</p>
        </div>
 
      </div>
      <div className={'flex justify-end'}>
        <Botao txt='FINALIZAR' onClick={finalizar}></Botao>
      </div>
    </div>
  )
}

export default Observacoes

