import React, { useState } from 'react'
import Input from '../../Componentes/Input'
import Filtro from '../../Componentes/Filtro'
import Botao from '../../Componentes/Botao'

function Editar_criterio() { // TELA PARA EDITAR OS CRITERIOS

    let curso = ['Digital Solutions', 'Mecatrônica', 'Manufatura Digital']
    let semestre = ['1° Semestre', '2° Semestre', '3° Semestre', 'Todos']

    const [curso2, setCurso2] = useState('')
    const [criterio, setCriterio] = useState('')
    const [descricao, setDescricao] = useState('')
    const [semestre2, setSemestre2] = useState('')

    const editar = (e) => {
        console.log('curso:', curso2)
        console.log('criterio:', criterio)
        console.log('descricao:', descricao)
        console.log('semestre:', semestre2)
    }

    return (
        <div className={`flex flex-col h-full gap-4 mt-10 mx-10`}>
            <h1 className={`text-2xl font-bold font-roboto`}>EDITAR CRITÉRIO </h1>
            <p className={`text-base font-roboto font-semibold`}>Preencha as informações abaixo para editar o critério:</p>
            <Filtro label='Selecione o curso que possui esse critério.' value={curso2} onChange={(e) => { setCurso2(e.target.value) }} optionList={curso}></Filtro>
            <Input label='Nome do critério' value={criterio} onChange={(e) => { setCriterio(e.target.value) }}></Input>
            <Input label='Descrição do critério: ajuda o aprendiz ou instrutor a saber mais informações.' value={descricao} onChange={(e) => { setDescricao(e.target.value) }}> </Input>
            <Filtro label='Selecione o(os) semestre(s) que esse critério deve aparecer.' value={semestre2} onChange={(e) => { setSemestre2(e.target.value) }} optionList={semestre} ></Filtro>
            <div className={'flex justify-end'}><Botao txt='SALVAR' onClick={editar}></Botao></div>
        </div>
    )
}

export default Editar_criterio