import React, { useState } from 'react'
import Botao from '../../Componentes/Botao'
import Filtro from '../../Componentes/Filtro'
import Input from '../../Componentes/Input'
 
function Editar_turma() { //TELA PARA EDITAR AS TURMAS
 
  let cursos = ['Digital Solutions', 'Mecatrônica', 'Manufatura Digital']
  let instrutor = ['Vanessa Silva', 'Cleber', 'Ianella', 'Leonardo', 'Luca']
 
  const [curso, setCurso] = useState('')
  const [turma, setTurma] = useState('')
  const [padrinhos, setPadrinhos] = useState('')
 
  const visualizar = (e) => {
    console.log('curso:', curso)
    console.log('turma:', turma)
    console.log('padrinho (a):', padrinhos)
  }
 
  return (
    <div className={`flex flex-col h-full gap-4 mt-10 mx-10`}>
      <h1 className={`text-2xl font-bold font-roboto`}>EDITAR TURMA </h1>
      <p className={`text-base font-roboto font-semibold`}>Preencha as informações abaixo para editar a turma:</p>
      <Filtro label='Selecione o curso.' optionList={cursos} value={curso} onChange={(e) => (setCurso (e.target.value))} ></Filtro>
      <Input label='Nome da turma' value={turma} onChange={(e) => (setTurma (e.target.value))}></Input>
      <Filtro label='Selecione o padrinho ou a madrinha.' optionList={instrutor} value={padrinhos} onChange={(e) => (setPadrinhos (e.target.value))}></Filtro>
      <div className={'flex justify-end'}><Botao txt='SALVAR' onClick={visualizar}></Botao></div>
    </div>
  )
}
 
export default Editar_turma