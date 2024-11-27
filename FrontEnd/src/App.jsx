import { BrowserRouter, Routes, Route, useLocation } from 'react-router-dom'
import './App.css'
import Header from './assets/Componentes/Header'
import Footer from './assets/Componentes/Footer'
import HomeAdmin from './assets/Pages/Admin/HomeAdmin'
import HomeIns from './assets/Pages/Instrutor/HomeIns'
import Cadastro_turma from './assets/Pages/Admin/Cadastro_turma'
import Editar_turma from './assets/Pages/Admin/Editar_turma'
import Cadastro_aprendiz from './assets/Pages/Admin/Cadastro_aprendiz'
import Criterios from './assets/Pages/Admin/Criterios'
import Editar_criterio from './assets/Pages/Admin/Editar_criterio'
import Avaliacao from './assets/Pages/Instrutor/Avaliacao'
import Feedback from './assets/Pages/Instrutor/Feedback'
import Avaliacao_feedback from './assets/Pages/Instrutor/Avaliacao_feedback'
import Observacoes from './assets/Pages/Instrutor/Observacoes'
import Auto_avaliacao from './assets/Pages/Aprendiz/Auto_avaliacao'
import Home_aprendiz from './assets/Pages/Aprendiz/Home_aprendiz'
import Cadastro from './assets/Pages/Cadastro/Cadastro'
import Login from './assets/Pages/Cadastro/Login'
import RecuperarSenha from './assets/Pages/Cadastro/RecuperarSenha'
import NovaSenha from './assets/Pages/Cadastro/NovaSenha'
import Cadastro_de_Aprendiz from './assets/Pages/Cadastro/Cadastro_de_Aprendiz'
import CadastroGestor from './assets/Pages/Cadastro/CadastroGestor'
import RendimentoAprendiz from './assets/Pages/Aprendiz/RendimentoAprendiz'
import RendimentoGestor from './assets/Pages/Gestor/RendimentoGestor'
import Home from './assets/Pages/Cadastro/Home'
import Email from './assets/Pages/Admin/Email'
import Upload from './assets/Pages/Admin/Upload'
import Rendimento_instrutor from './assets/Pages/Instrutor/Rendimento_instrutor'
import Rendimento_Feedback from './assets/Pages/Instrutor/Rendimento_Feedback'
import RecuperarEdv from './assets/Pages/Cadastro/RecuperarEdv'

function App(){
  return(
    <BrowserRouter>
      <AppContent></AppContent>
    </BrowserRouter>
  )
}

function AppContent() {
  const location = useLocation();

  const isInstrutor = () => {
    return (
      location.pathname === '/HomeIns' ||
      location.pathname === '/Avaliacao' ||
      location.pathname === '/Avaliacao_feedback' ||
      location.pathname === '/Feedback' ||
      location.pathname === '/Rendimento_instrutor' ||
      location.pathname === '/Rendimento_Feedback' ||
      location.pathname === '/Observacoes'
    );
  };

  const isAprendiz = () => {
    return (
      location.pathname === '/Auto_avaliacao' ||
      location.pathname === '/Home_aprendiz' ||
      location.pathname === '/RendimentoAprendiz'
    );
  };

  const isAdmin = () => {
    return (
      location.pathname === '/HomeAdmin' ||
      location.pathname === '/Cadastro_aprendiz' ||
      location.pathname === '/Cadastro_turma' ||
      location.pathname === '/Criterios' ||
      location.pathname === '/Editar_criterio' ||
      location.pathname === '/Editar_turma' ||
      location.pathname === '/Email' ||
      location.pathname === '/Upload'
    );
  };

  const isGestor = () => {
    return (
      location.pathname === '/RendimentoGestor'
    );
  };

  const isHome = () => {
    return (
      location.pathname === '/' ||
      location.pathname === '/Home'
    );
  };

  return (
    <div className={'h-full '}>
      <Header instrutor={isInstrutor()} aprendiz={isAprendiz()} gestor={isGestor()} admin={isAdmin()} home={isHome()} />

        <Routes>
          <Route path='/' element={<Home/>}></Route>

          <Route path='/Home' element={<Home/>}></Route>
          <Route path='/Cadastro' element={<Cadastro/>}></Route>
          <Route path='/Cadastro_de_Aprendiz' element={<Cadastro_de_Aprendiz/>}></Route>
          <Route path='/CadastroGestor' element={<CadastroGestor/>}></Route>
          <Route path='/Login' element={<Login/>}></Route>
          <Route path='/RecuperarEdv' element={<RecuperarEdv/>}></Route>
          <Route path='/RecuperarSenha' element={<RecuperarSenha/>}></Route>
          <Route path='/NovaSenha' element={<NovaSenha/>}></Route>

          <Route path='/HomeAdmin' element={<HomeAdmin/>}></Route>
          <Route path='/Cadastro_aprendiz' element={<Cadastro_aprendiz/>}></Route>
          <Route path='/Cadastro_turma' element={<Cadastro_turma/>}></Route>
          <Route path='/Criterios' element={<Criterios/>}></Route>
          <Route path='/Editar_criterio' element={<Editar_criterio/>}></Route>
          <Route path='/Editar_turma' element={<Editar_turma/>}></Route>
          <Route path='/Email' element={<Email/>} ></Route>
          <Route path='/Upload' element={<Upload/>} ></Route>

          <Route path='/Auto_avaliacao' element={<Auto_avaliacao/>}></Route>
          <Route path='/Home_aprendiz' element={<Home_aprendiz/>}></Route>
          <Route path='/RendimentoAprendiz' element={<RendimentoAprendiz/>}></Route>

          <Route path='/RendimentoGestor' element={<RendimentoGestor/>}></Route>

          <Route path='/HomeIns' element={<HomeIns/>}></Route>
          <Route path='/Avaliacao' element={<Avaliacao/>}></Route>
          <Route path='/Avaliacao_feedback' element={<Avaliacao_feedback/>}></Route>
          <Route path='/Feedback' element={<Feedback/>}></Route>
          <Route path='/Rendimento_instrutor' element={<Rendimento_instrutor/>}></Route>
          <Route path='/Rendimento_Feedback' element={<Rendimento_Feedback/>}></Route>


          <Route path='/Observacoes' element={<Observacoes/>}></Route>
        </Routes>     

      <Footer ciano={isInstrutor()} verde={isGestor()} azul={isAdmin()} azul_aprendiz={isAprendiz()} home={isHome()}/>
    </div>
  )
}

export default App
