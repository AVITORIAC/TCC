import React from 'react'
import fundo from '../../Imgs/Fundo.jpg'
import Card_login from '../../Componentes/Card_login'



function Login() { //TELA DE LOGIN
    return (
        <div className={'flex items-center sm:h-screen md:h-screen lg:h-screen xl:h-screen 2xl:h-screen justify-center'}>
            <img src={fundo} className={'w-full sm:h-screen md:h-screen lg:h-screen xl:h-screen 2xl:h-screen flex absolute'} alt="" />
            <Card_login></Card_login>
        </div>
    )
}

export default Login


