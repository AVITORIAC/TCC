import React from 'react'
import Filtro from '../../Componentes/Filtro'
import Card from '../../Componentes/Card'
import Input from '../../Componentes/Input'
import { Link } from 'react-router-dom'


function Feedback() { //TELA PARA DAR O FEEDBACK COM O APRENDIZ
    let semestre = ['1° Semestre', '2° Semestre', '3° Semestre']
    let turma = ['DS 6', 'DS 7', 'DS 8', 'DS 9', 'DS 10']
    let aprendiz = ['Eduarda Rabelo Oliveira', 'Julia Roberta Veloso Guiraldeli', 'Carlos Eduardo Faustino Barbosa']
    let criterios = ['INGLES', '5S', 'CONHECIMENTO', 'PYTHON', 'JAVA', 'EMPATIA','PYTHON', 'JAVA', 'EMPATIA','PYTHON', 'JAVA', 'EMPATIA', ]



    return (
        <div className={`flex gap-4 mt-10 mx-10 sm:flex-col sm:gap-10 md:justify-between `}>
            <div className={'flex flex-col sm:gap-4 lg:w-3/5 '}>
                <h1 className={`text-2xl font-bold font-roboto`}>FEEDBACK</h1>
                <Filtro id="turma" label='Selecione a turma' optionList={turma} ></Filtro>
                <Filtro id="aprendiz" label='Selecione o aprendiz' optionList={aprendiz} ></Filtro>
                <Filtro id="semestre" label='Selecione o semestre' optionList={semestre} ></Filtro>
                <div className={'bg-cianoclaro flex flex-col h-64 w-full gap-4 pt-2 pb-2 pl-1 pr-1 sm:overflow-y-scroll sm:w-3/4 xl:w-2/4 xl:h-80 '}>
                    {new Array(Math.ceil(criterios.length / 3)).fill(0).map((e, i) => {
                        return (<div key={i}>
                            {criterios.slice(i * 3, i * 3 + 3).map((ea) => { return <Input label={ea} /> })}
                        </div>)
                    })}
                </div>
            </div>

            <div className={`flex flex-col gap-4 xl:flex-row`}>
                <Card verde3 h1='Nota final' h2='3,6' p='Essa nota é calculada com base nos critérios dos instrutores.' />
                <Link to='/Rendimento_Feedback'><Card verde1 h1='Instrutor' h2='Semestres anteriores' p='Acompanhar o desempenho em diferentes semestres' /></Link>
                <Link to='/Avaliacao_feedback'><Card verde2 h1='Aprendiz' h2='Auto avaliação do aprendiz' p='Acompanhar a nota em cada critério do aprendiz' /></Link>

            </div>
        </div>
    ) 
}

export default Feedback
