import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
// Estilos globales
import './index.css'
// Enrutador para navegación sin recarga
import { BrowserRouter } from 'react-router-dom'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    {/* BrowserRouter provee navegación SPA (Single Page Application) */}
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
)
