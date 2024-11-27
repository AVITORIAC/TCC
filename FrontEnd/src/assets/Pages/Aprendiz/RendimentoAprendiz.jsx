import Chart from '../../Componentes/Chart'
import Titulo from '../../Componentes/Titulo'
import Filtro from '../../Componentes/Filtro'
import Botao from '../../Componentes/Botao'
import { Link } from 'react-router-dom'
import React, { useState } from "react";

function RendimentoAprendiz() {
    let semestre = ['1° Semestre', '2° Semestre', '3° Semestre']

    const [semes, setSemes] = useState('')
    const [semes1, setsemes1] = useState('')

    const visualizar = (e) => {
        console.log('semestre:', semes)
        console.log('semestre:', semes1)
    }
    return (
        <div className={'flex-col w-full xl:h-full sm:h-fit p-5 justify-center sm:flex-col md:flex-col lg:flex-col xl:flex-col 2xl:flex-col'}>
            <Titulo h1='RENDIMENTO'></Titulo>
            <h2 className={'font-roboto mt-4'}>Bem-vindo(a) ao seu rendimento, aqui você consegue acompanhar sua evolução entre os semestres de acordo os principais critérios.</h2>
            <div className={' w-full flex flex-row items-end gap-16 mt-5 sm:flex-col sm:gap-8 sm:p-3 md:p-5 lg:p-3 lg:flex-row lg:justify-center xl:p-3  2xl:p-5'}>
                <Filtro id='semestre' label='Selecione o semestre' optionList={semestre} value={semes} onChange={(e) => (setSemes(e.target.value))}></Filtro>
                <Filtro id='semestre' label='selecione outro semestre' optionList={semestre} value={semes1} onChange={(e) => (setsemes1(e.target.value))}></Filtro>
                <Link onClick={visualizar}><Botao txt='VERIFICAR'></Botao></Link>
            </div>
            <div className={' w-full flex justify-center mt-5 '}>
                <Chart></Chart>
            </div>
        </div>
    )
}

export default RendimentoAprendiz