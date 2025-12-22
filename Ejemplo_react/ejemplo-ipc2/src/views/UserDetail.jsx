import { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { obtenerUsuarioPorId } from '../services/userService'

// Vista de detalle de un usuario
// Consume la API para obtener los datos del usuario específico
export default function UserDetail() {
  const { id } = useParams()
  const navigate = useNavigate()
  
  // Estado para almacenar el usuario
  const [user, setUser] = useState(null)
  // Estado para manejar la carga de datos
  const [loading, setLoading] = useState(true)
  // Estado para manejar errores
  const [error, setError] = useState(null)

  // useEffect para cargar el usuario al montar el componente
  useEffect(() => {
    cargarUsuario()
  }, [id])

  // Función para obtener el usuario del backend
  const cargarUsuario = async () => {
    try {
      setLoading(true)
      setError(null)
      // Hacer petición GET al backend para obtener el usuario por ID
      const data = await obtenerUsuarioPorId(id)
      setUser(data)
    } catch (err) {
      setError('No se pudo cargar el usuario')
      console.error('Error al cargar usuario:', err)
    } finally {
      setLoading(false)
    }
  }

  // Mostrar mensaje de carga
  if (loading) {
    return (
      <section>
        <h2 className="title">Detalle del Usuario</h2>
        <p style={{ textAlign: 'center', color: '#667eea', fontSize: '1.1rem' }}>
          Cargando información...
        </p>
      </section>
    )
  }

  // Mostrar mensaje de error
  if (error || !user) {
    return (
      <section>
        <h2 className="title">Detalle del Usuario</h2>
        <div className="error" style={{ textAlign: 'center' }}>
          <p>{error || 'Usuario no encontrado'}</p>
          <button onClick={() => navigate('/usuarios')} className="btn secondary" style={{ marginTop: '1rem' }}>
            Volver a la lista
          </button>
        </div>
      </section>
    )
  }

  // Mostrar detalles del usuario
  return (
    <section>
      <h2 className="title">Detalle del Usuario</h2>
      <div className="user-card">
        <h3>{user.nombre}</h3>
        <p><strong>Correo:</strong> {user.correo}</p>
        <p><strong>ID:</strong> {user.id}</p>
        
        <div className="form-actions" style={{ marginTop: '2rem' }}>
          <button onClick={() => navigate('/usuarios')} className="btn secondary">
            Volver
          </button>
        </div>
      </div>
    </section>
  )
}
