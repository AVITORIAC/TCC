import React, { useState } from "react";
import Filtro from '../../Componentes/Filtro'
import Botao from '../../Componentes/Botao'
import { Link } from 'react-router-dom'
import Chart from "../../Componentes/Chart";

function Rendimento_Feedback() { // FUNÇÕES DA TELA DE RENDIMENTO DO(S) APRENDIZ(S) NO ACESSO DO INSTRUTOR
    let tipo = ['Auto Avaliação', 'Avaliação']
    let criterios = ['Profissionalismo', 'ingles', 'Conhecimento teorioco']

    const [tipos, setTipos] = useState('')
    const [criterio, setCriterio] = useState('')

    const finalizar = (e) => {
        console.log('tipos:', tipos)
        console.log('criterio:', criterio)

    }
    return (
        <div className={`w-full justify-center sm:w-full sm:p-6 lg:h-full  `}>
            <h1 className={`text-2xl font-bold font-roboto `}>RENDIMENTO</h1>
            <p className={`text-base font-semibold font-roboto pt-4`}>Utilize os filtros para comparar a evolução do aprendiz de acordo com o critério.</p>
            <div className={'flex  xl:justify-center '}>
                <div className={'flex flex-row justify-between mt-8 sm:flex-col sm:gap-4 lg:flex-row lg:justify-evenly 2xl:w-9/12 xl:justify-evenly'}>
                    <Filtro id='tipoCriterio' label='Selecione o tipo de criterio' optionList={tipo} value={tipos} onChange={(e) => (setTipos(e.target.value))}></Filtro>
                    <Filtro id='criterio' label='Selecione o critério' optionList={criterios} value={criterio} onChange={(e) => (setCriterio(e.target.value))}></Filtro>
                    <div className={'flex  items-end'}>
                        <Link><Botao txt='FINALIZAR' onClick={finalizar}></Botao></Link>
                    </div>
                </div>
            </div>

            <div className={'flex justify-center mt-14'}>
                <Chart></Chart>
            </div>
        </div>
    )
}

export default Rendimento_Feedback
