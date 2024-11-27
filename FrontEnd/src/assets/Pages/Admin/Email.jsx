import React, { useState }from 'react'
import Input from '../../Componentes/Input'
import Botao from '../../Componentes/Botao'

function Email() {
  const [email, setEmail] = useState('')
  const [senha, setSenha] = useState('')

  const editar = (e) => {
    console.log('email:', email)
    console.log('senha:', senha)
  }

  return (
    <div className={`flex flex-col h-full gap-4 mt-10 mx-10`}>
      <h1 className={`text-2xl font-bold`}>E-MAIL</h1>
      <h2 className={`text-lg font-bold`}>Editar e-mail</h2>
      <p className={`text-base`}>Preencha as informações para editar o usuário que envia o e-mail de recuperação de senha.</p>
      <Input label='Insira o e-mail' value={email} onChange={(e) => { setEmail(e.target.value) }}></Input>
      <Input label='Insira a senha' value={senha} onChange={(e) => { setSenha(e.target.value) }}> </Input>
      <div className={'flex justify-end'}><Botao txt='EDITAR' onClick={editar}></Botao></div>
    </div>
  )
}

export default Email
