import React from 'react'
import animação1 from '../../Imgs/animação1.png'
import animacao2 from '../../Imgs/animacao2.png'
import animacao3 from '../../Imgs/animacao3.png'
import animacao4 from '../../Imgs/animacao4.png'
import front from '../../Imgs/front.png'
import back from '../../Imgs/back.png'
import outros from '../../Imgs/outros.png'
import { GoLightBulb } from "react-icons/go";


function Home() {  //TELA INICIAL DA PLATAFORMA 
    return (
        <div>
            <div className={'flex items-center'}>
                <div className={''}>
                    <h1 className={'p-4 mb-2 ml-10 text-4xl font-semibold bg-gradient-to-r from-gradiente2 to-gradiente1 inline-block text-transparent bg-clip-text'}>Plataforma online de Feedback</h1>
                    <p className={'ml-14 text-base'}>O Meinung tem por objetivo melhorar o processo do feedback
                        entre os aprendizes e instrutores.</p>
                    <p className={'ml-14 text-base'}>Dessa forma, os dados ficam centralizados
                        contribuindo para o funcionamento de maneira mais rápida e fácil para todos os envolvidos.</p>
                </div>
                <div className={'flex justify-end mr-10 mt-5'}>
                    <img src={animação1} alt="" />
                </div>
            </div>
            <div className={'flex justify-center'}>
                <div className={`w-11/12 h-48 flex items-center justify-center bg-home rounded-b-3xl rounded-l-full rounded-r-full mt-20`}>
                    <div className={'flex justify-center items-center p-4'}>
                        <div className={'flex flex-col items-center m-14'}>
                            <div><GoLightBulb fill='white' size={60} /></div>
                            <p className={'text-white mt-2'}>IDEIA</p>
                        </div>

                        <p className={'text-base'}>A ideia para o projeto surgiu em uma reunião com o Henrique Dona, nosso gestor. Além disso, também percebemos que alguns processos do feedback poderiam ser automatizados para ser mais rápido.</p>
                    </div>
                </div>

            </div>
            <div className={'flex justify-center items-center mt-10'}>
                <p className={'text-2xl font-bold bg-gradient-to-r from-gradiente4 to-gradiente3 inline-block text-transparent bg-clip-text'}>NOSSOS SERVIÇOS</p>
            </div>


            <div className={'flex justify-center'}>
                <div className={`w-11/12 h-48  bg-rosa rounded-r-full mt-20`}>
                    <div className={'flex items-center justify-around p-4'}>
                        <div className={''}>
                            <p className={'text-gradiente1 font-semibold'}>Auto Avaliação</p>
                        </div>

                        <div className={''}>
                            <p className={'text-base'}>Através de uma página é possível realizar toda a auto avaliação necessária no semestre.</p>
                        </div>

                        <div className={''}>
                            <img src={animacao2} alt="" className={'w-32'} />
                        </div>
                    </div>
                </div>
            </div>


            <div className={'flex justify-center'}>
                <div className={`w-11/12 h-48  bg-container rounded-l-full mt-20`}>
                    <div className={'flex items-center justify-center mt-4'}>
                        <p className={'text-dashboard font-semibold'}>Rendimento/Dashboard</p>
                    </div>
                    <div className={'flex items-center justify-evenly'}>
                        <div className={''}>
                            <img src={animacao3} alt="" className={'w-32'} />
                        </div>
                        <div className={''}>
                            <p className={'text-base'}>Todas as notas se transformam em dados, para que seja gerado o rendimento dos aprendizes em formato de gráfico.</p>
                        </div>
                    </div>
                </div>
            </div>


            <div className={'flex justify-center'}>
                <div className={`w-11/12 h-48  bg-rosa rounded-r-full mt-20`}>
                    <div className={'flex items-center justify-around p-4'}>
                        <div className={''}>
                            <p className={'text-gradiente1 font-semibold'}>Busca de dados</p>
                        </div>
                        <div className={''}>
                            <p className={'text-base'}>A plataforma recolhe as notas do SENAI de todos os aprendizes.</p>
                        </div>
                        <div className={''}>
                            <img src={animacao4} alt="" className={'w-16'} />
                        </div>
                    </div>
                </div>
            </div>


            <div className={'flex justify-center items-center mt-10'}>
                <p className={'text-2xl font-bold bg-gradient-to-r from-gradiente6 to-gradiente5 inline-block text-transparent bg-clip-text'}>FERRAMENTAS</p>
            </div>

            <div className={'flex justify-center mt-4'}>
                <div className={`w-11/12 h-48  bg-gray-100 flex items-center justify-around `}>
                    <div className={'w-10/12 flex items-center justify-between '}>
                        <div className={'flex flex-col w-32 mt-4 items-center '}>
                            <img src={front} alt="" className={'w-28'} />
                            <p className={'text-blue-800 font-semibold '}>FrontEnd</p>
                        </div>
                        <div className={'flex items-center'}>
                            <p className={'text-base'}>Utilizamos React JS junto com o Vite para a construção da platarfoma e conexão com as APIs.</p>
                        </div>

                    </div>
                </div>
            </div>


            <div className={'flex justify-center mt-4'}>
                <div className={`w-11/12 h-48  bg-gray-100 flex items-center justify-around`}>
                    <div className={'w-10/12 flex justify-between '}>
                        <div className={'flex flex-col mt-4 w-32 items-center '}>
                            <img src={back} alt="" className={'w-28'} />
                            <p className={'text-blue-800 font-semibold'}>BackEnd</p>
                        </div>
                        <div className={'flex items-center w-8/12 '}>
                            <p className={'text-base'}>Utilizamos Django para a construção das APIs e o banco de dados Sqlite <br />para o armazenamento dos dados,
                                que já vem por padrão com o Django; <br /> A extração dos dados do PDF foi realizado através da biblioteca do Python;</p>
                        </div>
                    </div>
                </div>
            </div>


            <div className={'flex justify-center mt-4'}>
                <div className={`w-11/12 h-48  bg-gray-100 flex items-center justify-around`}>
                    <div className={'w-10/12 flex justify-between '}>
                        <div className={'flex flex-col mt-4 w-32 items-center '}>
                            <img src={outros} alt="" className={'w-28'} />
                            <p className={'text-blue-800 font-semibold'}>Outros</p>
                        </div>
                        <div className={'flex items-center w-8/12'}>
                            <p className={'text-base'}>Para os gráficos utilizamos o Charts.js integrado com o banco de dados; <br />
                                Para o protótipo e logo utilizamos o Figma;<br /> Para as apresentações e video pitch utlizamos o Canva;</p>
                        </div>
                    </div>
                </div>
            </div>

            <div className={'flex justify-center'}>
                <div className={'w-11/12 h-14 mt-7 mb-6 flex items-center justify-center bg-gray-800'}>
                    <p className={'text-white'}>Desenvolvido por: Allana Vieira, Carlos Barbosa, Eduarda Oliveira e Julia Guiraldeli</p>
                </div>
            </div>
        </div>
    )
}

export default Home

