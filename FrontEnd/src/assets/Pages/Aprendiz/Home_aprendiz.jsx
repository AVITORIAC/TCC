import React from 'react'
import img1 from '../../Imgs/img1.png'
import img2 from '../../Imgs/img2.png'
import Botao from '../../Componentes/Botao'
import { Link } from 'react-router-dom'
import { useStore } from '../../store'


function Home_aprendiz() { //FUNÇÃO DA TELA INICIAL DO ACESSO DE APRENDIZ

    const {curso} = useStore() // recebendo a variável global do curso

    switch (curso) {

        case 'Técnico em Administração':
            return (
                <div className={'ml-7 h-full flex flex-col justify-around'}>
                    <div className={'flex max-w-[100rem]'}>
                        <img src={img1} alt="" />
                        <div className={'ml-6'}>
                            <h1 className={'font-roboto font-bold text-fonte text-2xl sm:text-xl'}>Preencher avaliação da área</h1>
                            <p className={'font-roboto sm:text-sm md:text-base'}>A avaliação é feita ao final dos semestres pelos aprendizes.
                                Esse é o momento em que você avalia sua jornada na área durante 6 meses de acordo com os critérios no formulário. Para isso, basta clicar no botão abaixo:</p>
                            <div className={'flex justify-end mr-10 mt-10'}>
                                <Link to='/Auto_avaliacao' ><Botao txt='PREENCHER'></Botao></Link>
                            </div>
                        </div>
                    </div>
                    <div className={'flex max-w-[100rem]'}>
                        <img src={img2} alt="" />
                        <div className={'ml-6'}>
                            <h1 className={'font-roboto font-bold text-fonte text-2xl sm:text-xl'}>Acompanhar rendimento</h1>
                            <p className={'font-roboto sm:text-sm md:text-base'}>O rendimento é medido de acordo com as suas notas em feedbacks anteriores completos. Os feedbacks completos são aqueles em que o instrutor aprensentou e discutiu suas notas. Dessa forma, clique no botão abaixo para visualizar seu rendimento:</p>
                            <div className={'flex justify-end mr-10 mt-10'}>
                                <Link to='/RendimentoAprendiz'><Botao txt='ACOMPANHAR'></Botao></Link>
                            </div>
                        </div>
                    </div>
                </div>
            )


        default:
            return (
                <div className={'ml-7 h-full '}>
                    <div className={'flex mt-7'}>
                        <img src={img1} alt="" />
                        <div className={'ml-6'}>
                            <h1 className={'font-roboto font-bold text-fonte text-2xl sm:text-xl'}>Preencher auto avaliação</h1>
                            <p className={'font-roboto sm:text-sm md:text-base'}>A auto avaliação é feita aos finais dos semestres pelos aprendizes. Esse é o momento em que você avalia sua jornada durantes 6 meses de acordo com os critérios no formulário. Para isso, basta clicar no botão abaixo:</p>
                            <div className={'flex justify-end mr-10 mt-10'}>
                                <Link to='/Auto_avaliacao' ><Botao txt='PREENCHER'></Botao></Link>
                            </div>
                        </div>
                    </div>
                    <div className={'flex mt-7'}>
                        <img src={img2} alt="" />
                        <div className={'ml-6'}>
                            <h1 className={'font-roboto font-bold text-fonte text-2xl sm:text-xl'}>Acompanhar rendimento</h1>
                            <p className={'font-roboto sm:text-sm md:text-base'}>O rendimento é medido de acordo com as suas notas em feedbacks anteriores completos. Os feedbacks completos são aqueles em que o instrutor aprensentou e discutiu suas notas. Dessa forma, clique no botão abaixo para visualizar seu rendimento:</p>
                            <div className={'flex justify-end mr-10 mt-10'}>
                                <Link to='/RendimentoAprendiz' ><Botao txt='ACOMPANHAR'></Botao></Link>
                            </div>
                        </div>
                    </div>
                </div>
            )
    }
}

export default Home_aprendiz