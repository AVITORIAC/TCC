import React from 'react'
import logo from '../Imgs/logo_rosto.png'
import { MdLogout } from "react-icons/md";
import { IoHome } from "react-icons/io5";
import { FiLogIn } from "react-icons/fi";
import { Link } from 'react-router-dom';


function Header({ gestor, instrutor, home, aprendiz, admin }) { //FUNÇÃO PARA TROCAR COR E ICONES DO HEADER 

  const cores = `
  ${gestor ? 'bg-gestor' : ''}
  ${instrutor ? 'bg-instrutor' : ''}
  ${home ? 'bg-home' : ''}
  ${aprendiz ? 'bg-aprendiz' : ''}
  ${admin ? 'bg-admin' : ''}`

  let acesso = ''
  if (home) {
    acesso = 'home';
  } 
  else if (aprendiz) {
    acesso = 'aprendiz';
  } 
  else if (admin) {
    acesso = 'admin';
  } 
  else if (instrutor) {
    acesso = 'instrutor';
  } 
  else if (gestor) {
    acesso = 'gestor';
  }
  
  switch (acesso) {

    case 'home':
      return (
        <div className={`h-20 p-2 w-full ${cores}`}>
          <img src={logo} className={`w-20 sm:w-16 md:w-20 m-2`} />
          <p className={'text-3xl absolute font-bold inset-x-0 top-4 left-32 h-16 text-white '}>Meinung</p>
          <a href='/Login'><FiLogIn color='white' className={' size-9 absolute top-4 right-4 h-10 w-10'}></FiLogIn></a>
        </div>
      )

    case 'aprendiz':
      return (
        <div className={`h-20 p-2 w-full ${cores}`}>
          <img src={logo} className={`w-20 sm:w-16 md:w-20 m-2`} />
          <p className={'text-3xl absolute font-bold inset-x-0 top-4 left-32 h-16 text-white '}>Meinung</p>
          <a href='/Home_aprendiz'><IoHome className={` fill-white absolute top-4 right-20 h-10 w-10`}></IoHome></a>
          <a href='/Login'><MdLogout className={' fill-white size-9 absolute top-4 right-4 h-10 w-10'}></MdLogout></a>
        </div>
      )

    case 'admin':
      return (
        <div className={`h-20 p-2 w-full ${cores}`}>
          <img src={logo} className={`w-20 sm:w-16 md:w-20 m-2`} />
          <p className={'text-3xl absolute font-bold inset-x-0 top-4 left-32 h-16 text-white'}>Meinung</p>
          <a href='/HomeAdmin'><IoHome className={` fill-white absolute top-4 right-20 h-10 w-10`}></IoHome></a>
          <a href='/Login'><MdLogout className={' fill-white size-9 absolute top-4 right-4 h-10 w-10'}></MdLogout></a>
        </div>
      )

    case 'instrutor':
      return (
        <div className={`h-20 p-2 w-full ${cores}`}>
          <img src={logo} className={`w-20 sm:w-16 md:w-20 m-2`} />
          <p className={'text-3xl absolute font-bold inset-x-0 top-4 left-32 h-16 text-white'}>Meinung</p>
          <a href='/HomeIns'><IoHome className={` fill-white absolute top-4 right-20 h-10 w-10`}></IoHome></a>
          <a href='/Login'><MdLogout className={' fill-white size-9 absolute top-4 right-4 h-10 w-10'}></MdLogout></a>
        </div>
      )

    case 'gestor':
      return (
        <div className={`h-20 p-2 w-full ${cores}`}>
          <img src={logo} className={`w-20 sm:w-16 md:w-20 m-2`} />
          <p className={'text-3xl absolute font-bold inset-x-0 top-4 left-32 h-16 text-white'}>Meinung</p>
          <a href='/Login'><MdLogout className={' fill-white size-9 absolute top-4 right-4 h-10 w-10'}></MdLogout></a>
        </div>
      )

    default:
      return(
        <></>
      )
  }

}


export default Header



