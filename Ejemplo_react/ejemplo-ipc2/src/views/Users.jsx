import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
// Importar el servicio para consumir la API
import { obtenerUsuarios } from '../services/userService'

// Vista que muestra la lista de usuarios
// Consume la API directamente para obtener los datos
export default function Users() {
  // Estado para almacenar los usuarios
  const [users, setUsers] = useState([])
  // Estado para manejar la carga de datos
  const [loading, setLoading] = useState(true)
  // Estado para manejar errores
  const [error, setError] = useState(null)

  // useEffect para cargar usuarios al montar el componente
  useEffect(() => {
    cargarUsuarios()
  }, [])

  // Función para obtener usuarios del backend
  const cargarUsuarios = async () => {
    try {
      setLoading(true)
      setError(null)
      // Hacer petición GET al backend
      const data = await obtenerUsuarios()
      setUsers(data)
    } catch (err) {
      setError('No se pudieron cargar los usuarios')
      console.error('Error al cargar usuarios:', err)
    } finally {
      setLoading(false)
    }
  }

  // Mostrar mensaje de carga
  if (loading) {
    return (
      <section>
        <h2 className="title">Lista de Usuarios</h2>
        <p style={{ textAlign: 'center', color: '#667eea', fontSize: '1.1rem' }}>
          Cargando usuarios...
        </p>
      </section>
    )
  }

  // Mostrar mensaje de error
  if (error) {
    return (
      <section>
        <h2 className="title">Lista de Usuarios</h2>
        <div className="error" style={{ textAlign: 'center' }}>
          <p>{error}</p>
          <button onClick={cargarUsuarios} className="btn primary" style={{ marginTop: '1rem' }}>
            Reintentar
          </button>
        </div>
      </section>
    )
  }

  // Mostrar lista de usuarios
  return (
    <section>
      <h2 className="title">Lista de Usuarios</h2>
      {users.length === 0 ? (
        <p style={{ textAlign: 'center', color: '#718096' }}>
          No hay usuarios registrados
        </p>
      ) : (
        <div className="user-list">
          {users.map((user) => (
            <div key={user.id} className="user-card">
              <h3>{user.nombre}</h3>
              <p>{user.correo}</p>
              
              <Link to={`/usuarios/${user.id}`} className="btn primary">
                Ver Detalles
              </Link>
            </div>
          ))}
        </div>
      )}
    </section>
  )
}
