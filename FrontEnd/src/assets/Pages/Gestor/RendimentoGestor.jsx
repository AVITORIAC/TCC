import React, { useState } from "react";
import Chart from '../../Componentes/Chart'
import Filtro from '../../Componentes/Filtro'
import Titulo from '../../Componentes/Titulo'
import { Link } from 'react-router-dom'
import Botao from '../../Componentes/Botao'

function RendimentoGestor() {
    let turma = ['DS 6', 'DS 7', 'DS 8', 'DS 9', 'DS 10']

    const [turma1, setTurma1] = useState('')
    const [turma2, setTurma2] = useState('')

    const visualizar = (e) => {
        console.log('turma:', turma1)
        console.log('turma:', turma2)
    }

    return (
        <div className={'p-5 sm:p-5 '}>
            <Titulo h1='RENDIMENTO'></Titulo>
            <div className={'flex justify-center gap-6 sm:flex-col sm:p-5 md:flex-col lg:flex-row'}>
                <Filtro id="turma" label='Selecione a turma' optionList={turma} value={turma1} onChange={(e) => (setTurma1(e.target.value))}></Filtro>
                <Filtro id="turma2" label='Selecione outra turma' optionList={turma} value={turma2} onChange={(e) => (setTurma2(e.target.value))}></Filtro>
                <div className={'lg:p-7 xl:p-7 2xl:p-7'}>
                    <Link><Botao txt='VISUALIZAR' onClick={visualizar}></Botao></Link>
                </div>
            </div>
            <div className={'flex justify-center mt-16'}>
                <Chart></Chart>
            </div>
        </div>
    )
}

export default RendimentoGestor