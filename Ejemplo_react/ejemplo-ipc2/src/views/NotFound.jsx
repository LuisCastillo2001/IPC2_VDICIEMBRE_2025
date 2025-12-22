import { Link } from 'react-router-dom'

// Vista para rutas inválidas.
export default function NotFound() {
  return (
    <section>
      <h2 className="title">Página no encontrada</h2>
      <p className="empty">La ruta que intentaste visitar no existe.</p>
      <Link className="btn" to="/">Ir al inicio</Link>
    </section>
  )
}
