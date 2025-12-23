import { NavLink } from 'react-router-dom'

// Menú de navegación principal.
// Usa NavLink para marcar la ruta activa sin recargar la página.
export default function NavBar() {
  return (
    <header className="navbar">
      <nav className="navbar-inner">
        <span className="brand">Gestión de Usuarios</span>
        <ul className="nav-links">
          <li>
            <NavLink
              to="/"
              className={({ isActive }) => (isActive ? 'active' : undefined)}
              end
            >
              Inicio
            </NavLink>
          </li>
          <li>
            <NavLink
              to="/usuarios"
              className={({ isActive }) => (isActive ? 'active' : undefined)}
            >
              Usuarios
            </NavLink>
          </li>
          <li>
            <NavLink
              to="/agregar"
              className={({ isActive }) => (isActive ? 'active' : undefined)}
            >
              Agregar
            </NavLink>
          </li>
        </ul>
      </nav>
    </header>
  )
}
