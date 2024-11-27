import React, { useState } from 'react'
import Input from '../../Componentes/Input'
import Botao from '../../Componentes/Botao'

function Upload() {
    const [email, setEmail] = useState('')

    const enviar = (e) => {
        console.log('email:', email)
    }

    return (
        <div className={`flex flex-col h-full gap-4 mt-10 mx-10`}>
            <h1 className={`text-2xl font-bold`}>NOTAS DO SENAI</h1>
            <h2 className={`text-lg font-bold`}>Selecione o arquivo</h2>
            <p className={`text-base`}>Selecione o arquivo .xlsx que contém as notas dos aprendizes do SENAI.</p>
            <Input label='Faça o upload do arquivo' type='file' value={email} onChange={(e) => { setEmail(e.target.value) }}></Input>
           
            <div className={'flex justify-end'}><Botao txt='ENVIAR' onClick={enviar}></Botao></div>
        </div>
    )
}

export default Upload
