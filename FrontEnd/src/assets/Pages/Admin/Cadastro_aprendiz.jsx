import React from 'react'
import { Link } from 'react-router-dom'

function Cadastro_aprendiz() { //FUNÇÃO DA TELA DE ACEITAR OS CADASTROS

    
    const aceitar = () => {
        console.log('Solicitação aceita')
    }
    const recusar = () => {
        console.log('Solicitação recusada')
    }

    return (
        <div className={`flex flex-col h-fit md:h-fit lg:full gap-6 mt-10 mx-10`}>
            <h1 className={`text-2xl font-bold font-roboto`}>GERENCIAR APRENDIZES</h1>
            <h2 className={`text-lg font-bold font-roboto`}>Novos cadastros</h2>
            <p className={`text-lg font-semibold font-roboto `}>Analise as informações e aceite ou recuse os novos aprendizes na plataforma através dos botões. </p>
            <table class="table-auto border-separate border-spacing-y-1.5 border-spacing-x-1.5 ">
                <thead>
                    <tr className=''>
                        <th className={' text-left '}>Nome</th>
                        <th className={' text-left '}>Turma</th>
                        <th className={' text-left '}>Edv</th>
                        <th className={' text-left '}>ACEITAR</th>
                        <th className={' text-left '}>RECUSAR</th>
                    </tr>
                </thead>
                <tbody >
                    <tr className=''>
                        <td className={'bg-barraedit font-semibold '}>Eduarda Rabelo Oliveira</td>
                        <td className={'bg-barraedit font-semibold'}>Digital solutions 6</td>
                        <td className={'bg-barraedit font-semibold'}>12345678</td>
                        <td className={''}><button onClick={aceitar} className={'bg-green-400 w-24'}>ACEITAR</button></td>
                        <td className=''><button onClick={recusar} className={'bg-red-400 w-24'}>RECUSAR</button></td>
                    </tr>
                    <tr>
                        <td className={'bg-barraedit font-semibold'}>Carlos Eduardo Faustino Barbosa</td>
                        <td className={'bg-barraedit font-semibold'}>Digital solutions 6</td>
                        <td className={'bg-barraedit font-semibold'}>12345678</td>
                        <td className={''}><button className={'bg-green-400 w-24'}>ACEITAR</button></td>
                        <td ><button className={'bg-red-400 w-24'}>RECUSAR</button></td>
                    </tr>
                    <tr>
                        <td className={'bg-barraedit font-semibold'}>Carlos Eduardo Faustino Barbosa</td>
                        <td className={'bg-barraedit font-semibold'}>Digital solutions 6</td>
                        <td className={'bg-barraedit font-semibold'}>12345678</td>
                        <td className={''}><button className={'bg-green-400 w-24'}>ACEITAR</button></td>
                        <td ><button className={'bg-red-400 w-24 '}>RECUSAR</button></td>
                    </tr>
                    <tr>
                        <td className={'bg-barraedit font-semibold'}>Carlos Eduardo Faustino Barbosa</td>
                        <td className={'bg-barraedit font-semibold'}>Digital solutions 6</td>
                        <td className={'bg-barraedit font-semibold'}>12345678</td>
                        <td className={''}><button className={'bg-green-400 w-24'}>ACEITAR</button></td>
                        <td ><button className={'bg-red-400 w-24 '}>RECUSAR</button></td>
                    </tr>
                    <tr>
                        <td className={'bg-barraedit font-semibold'}>Carlos Eduardo Faustino Barbosa</td>
                        <td className={'bg-barraedit font-semibold'}>Digital solutions 6</td>
                        <td className={'bg-barraedit font-semibold'}>12345678</td>
                        <td className={''}><button className={'bg-green-400 w-24'}>ACEITAR</button></td>
                        <td ><button className={'bg-red-400 w-24 '}>RECUSAR</button></td>
                    </tr>
                    <tr>
                        <td className={'bg-barraedit font-semibold'}>Carlos Eduardo Faustino Barbosa</td>
                        <td className={'bg-barraedit font-semibold'}>Digital solutions 6</td>
                        <td className={'bg-barraedit font-semibold'}>12345678</td>
                        <td className={''}><button className={'bg-green-400 w-24'}>ACEITAR</button></td>
                        <td ><button className={'bg-red-400 w-24 '}>RECUSAR</button></td>
                    </tr>
                    <tr>
                        <td className={'bg-barraedit font-semibold'}>Carlos Eduardo Faustino Barbosa</td>
                        <td className={'bg-barraedit font-semibold'}>Digital solutions 6</td>
                        <td className={'bg-barraedit font-semibold'}>12345678</td>
                        <td className={''}><button className={'bg-green-400 w-24'}>ACEITAR</button></td>
                        <td ><button className={'bg-red-400 w-24 '}>RECUSAR</button></td>
                    </tr>
                    <tr>
                        <td className={'bg-barraedit font-semibold'}>Carlos Eduardo Faustino Barbosa</td>
                        <td className={'bg-barraedit font-semibold'}>Digital solutions 6</td>
                        <td className={'bg-barraedit font-semibold'}>12345678</td>
                        <td className={''}><button className={'bg-green-400 w-24'}>ACEITAR</button></td>
                        <td ><button className={'bg-red-400 w-24 '}>RECUSAR</button></td>
                    </tr>
                    <tr>
                        <td className={'bg-barraedit font-semibold'}>Carlos Eduardo Faustino Barbosa</td>
                        <td className={'bg-barraedit font-semibold'}>Digital solutions 6</td>
                        <td className={'bg-barraedit font-semibold'}>12345678</td>
                        <td className={''}><button className={'bg-green-400 w-24'}>ACEITAR</button></td>
                        <td ><button className={'bg-red-400 w-24 '}>RECUSAR</button></td>
                    </tr>
                    <tr>
                        <td className={'bg-barraedit font-semibold'}>Carlos Eduardo Faustino Barbosa</td>
                        <td className={'bg-barraedit font-semibold'}>Digital solutions 6</td>
                        <td className={'bg-barraedit font-semibold'}>12345678</td>
                        <td className={''}><button className={'bg-green-400 w-24'}>ACEITAR</button></td>
                        <td ><button className={'bg-red-400 w-24 '}>RECUSAR</button></td>
                    </tr>
                    <tr>
                        <td className={'bg-barraedit font-semibold'}>Carlos Eduardo Faustino Barbosa</td>
                        <td className={'bg-barraedit font-semibold'}>Digital solutions 6</td>
                        <td className={'bg-barraedit font-semibold'}>12345678</td>
                        <td className={''}><button className={'bg-green-400 w-24'}>ACEITAR</button></td>
                        <td ><button className={'bg-red-400 w-24 '}>RECUSAR</button></td>
                    </tr>
                    <tr>
                        <td className={'bg-barraedit font-semibold'}>Carlos Eduardo Faustino Barbosa</td>
                        <td className={'bg-barraedit font-semibold'}>Digital solutions 6</td>
                        <td className={'bg-barraedit font-semibold'}>12345678</td>
                        <td className={''}><button className={'bg-green-400 w-24'}>ACEITAR</button></td>
                        <td ><button className={'bg-red-400 w-24 '}>RECUSAR</button></td>
                    </tr>
                    <tr>
                        <td className={'bg-barraedit font-semibold'}>Carlos Eduardo Faustino Barbosa</td>
                        <td className={'bg-barraedit font-semibold'}>Digital solutions 6</td>
                        <td className={'bg-barraedit font-semibold'}>12345678</td>
                        <td className={''}><button className={'bg-green-400 w-24'}>ACEITAR</button></td>
                        <td ><button className={'bg-red-400 w-24 '}>RECUSAR</button></td>
                    </tr>
                    <tr>
                        <td className={'bg-barraedit font-semibold'}>Carlos Eduardo Faustino Barbosa</td>
                        <td className={'bg-barraedit font-semibold'}>Digital solutions 6</td>
                        <td className={'bg-barraedit font-semibold'}>12345678</td>
                        <td className={''}><button className={'bg-green-400 w-24'}>ACEITAR</button></td>
                        <td ><button className={'bg-red-400 w-24 '}>RECUSAR</button></td>
                    </tr>
                    <tr>
                        <td className={'bg-barraedit font-semibold'}>Carlos Eduardo Faustino Barbosa</td>
                        <td className={'bg-barraedit font-semibold'}>Digital solutions 6</td>
                        <td className={'bg-barraedit font-semibold'}>12345678</td>
                        <td className={''}><button className={'bg-green-400 w-24'}>ACEITAR</button></td>
                        <td ><button className={'bg-red-400 w-24 '}>RECUSAR</button></td>
                    </tr>
                    <tr>
                        <td className={'bg-barraedit font-semibold'}>Carlos Eduardo Faustino Barbosa</td>
                        <td className={'bg-barraedit font-semibold'}>Digital solutions 6</td>
                        <td className={'bg-barraedit font-semibold'}>12345678</td>
                        <td className={''}><button className={'bg-green-400 w-24'}>ACEITAR</button></td>
                        <td ><button className={'bg-red-400 w-24 '}>RECUSAR</button></td>
                    </tr>
                    <tr>
                        <td className={'bg-barraedit font-semibold'}>Carlos Eduardo Faustino Barbosa</td>
                        <td className={'bg-barraedit font-semibold'}>Digital solutions 6</td>
                        <td className={'bg-barraedit font-semibold'}>12345678</td>
                        <td className={''}><button className={'bg-green-400 w-24'}>ACEITAR</button></td>
                        <td ><button className={'bg-red-400 w-24 '}>RECUSAR</button></td>
                    </tr>
                    <tr>
                        <td className={'bg-barraedit font-semibold'}>Carlos Eduardo Faustino Barbosa</td>
                        <td className={'bg-barraedit font-semibold'}>Digital solutions 6</td>
                        <td className={'bg-barraedit font-semibold'}>12345678</td>
                        <td className={''}><button className={'bg-green-400 w-24'}>ACEITAR</button></td>
                        <td ><button className={'bg-red-400 w-24 '}>RECUSAR</button></td>
                    </tr>
                    <tr>
                        <td className={'bg-barraedit font-semibold'}>Carlos Eduardo Faustino Barbosa</td>
                        <td className={'bg-barraedit font-semibold'}>Digital solutions 6</td>
                        <td className={'bg-barraedit font-semibold'}>12345678</td>
                        <td className={''}><button className={'bg-green-400 w-24'}>ACEITAR</button></td>
                        <td ><button className={'bg-red-400 w-24 '}>RECUSAR</button></td>
                    </tr>
                    <tr>
                        <td className={'bg-barraedit font-semibold'}>Carlos Eduardo Faustino Barbosa</td>
                        <td className={'bg-barraedit font-semibold'}>Digital solutions 6</td>
                        <td className={'bg-barraedit font-semibold'}>12345678</td>
                        <td className={''}><button className={'bg-green-400 w-24'}>ACEITAR</button></td>
                        <td ><button className={'bg-red-400 w-24 '}>RECUSAR</button></td>
                    </tr>

                </tbody>
            </table>

            {/* <div className={`w-full h-20 bg-barraedit flex gap-36 justify-normal items-center sm:gap-4 sm:pr-2 sm:pl-2 md:gap-10 lg:gap-16 xl:gap-20`}>
                <p className={`text-base font-bold font-roboto sm:text-sm lg:text-base xl:text-xl`}>Eduarda Rabelo Oliveira</p>
                <p className={`text-base font-bold font-roboto sm:text-sm lg:text-base xl:text-xl`}>Digital solutions 6</p>
                <p className={`text-base font-bold font-roboto sm:text-sm lg:text-base xl:text-xl`}>12345678 </p>
               <Link onClick={aceitar}><p className={`text-base font-bold font-roboto sm:text-sm lg:text-base xl:text-xl`}>ACEITAR </p></Link>
               <Link onClick={recusar}><p className={`text-base font-bold font-roboto sm:text-sm lg:text-base xl:text-xl`}>RECUSAR </p></Link>
            </div>
            <div className={`w-full h-20 bg-barraedit flex gap-36 justify-start items-center sm:gap-4 sm:pr-2 sm:pl-2 md:gap-10 lg:gap-16 xl:gap-20`}>
                <p className={`text-base font-bold font-roboto sm:text-sm lg:text-base xl:text-xl`}>Carlos Eduardo Faustino Barbosa </p>
                <p className={`text-base font-bold font-roboto sm:text-sm lg:text-base xl:text-xl`}>Digital solutions 6</p>
                <p className={`text-base font-bold font-roboto sm:text-sm lg:text-base xl:text-xl`}>12345678 </p>
               <Link onClick={aceitar}><p className={`text-base font-bold font-roboto sm:text-sm lg:text-base xl:text-xl`}>ACEITAR </p></Link>
               <Link onClick={recusar}><p className={`text-base font-bold font-roboto sm:text-sm lg:text-base xl:text-xl`}>RECUSAR </p></Link>
            </div>
     */}



        </div>
    )
}

export default Cadastro_aprendiz

