import { useState } from 'react'
// React Router para definir rutas de la aplicación
import { Routes, Route } from 'react-router-dom'
import './App.css'

// Componentes y vistas (se crean en archivos separados)
import NavBar from './components/NavBar'
import Home from './views/Home'
import Users from './views/Users'
import UserDetail from './views/UserDetail'
import AddUser from './views/AddUser'




function App() {
  return (
    <div className="app-container">
      {/* Menú de navegación visible en toda la app */}
      <NavBar />

      <main className="content">
        {/* Definición de rutas: SPA sin recargar la página */}
        <Routes>
          <Route path="/" element={<Home />} />
          {/* Lista y detalle de usuarios - cada vista maneja su propia data */}
          <Route path="/usuarios" element={<Users />} />
          <Route path="/usuarios/:id" element={<UserDetail />} />
          {/* Formulario para agregar un nuevo usuario */}
          <Route path="/agregar" element={<AddUser />} />
         
        </Routes>
      </main>
    </div>
  )
}

export default App
