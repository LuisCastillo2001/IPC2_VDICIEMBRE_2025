import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
// Importar el servicio para consumir la API
import { obtenerUsuarios, cargarUsuariosDesdeXml } from '../services/userService'

// Vista que muestra la lista de usuarios
// Consume la API directamente para obtener los datos
export default function Users() {
  // Estado para almacenar los usuarios
  const [users, setUsers] = useState([])
  // Estado para manejar la carga de datos
  const [loading, setLoading] = useState(true)
  // Estado para manejar errores
  const [error, setError] = useState(null)
  // Estado para archivo XML y mensajes
  const [xmlFile, setXmlFile] = useState(null)
  const [xmlError, setXmlError] = useState('')
  const [xmlSuccess, setXmlSuccess] = useState('')

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

  // Función para manejar el envío del archivo XML
  const handleXmlSubmit = async (e) => {
    e.preventDefault()
    setXmlError('')
    setXmlSuccess('')
    if (!xmlFile) {
      setXmlError('Selecciona un archivo XML.')
      return
    }
    try {
      const data = await cargarUsuariosDesdeXml(xmlFile)
      setUsers(data)
      setXmlSuccess('Usuarios cargados correctamente desde XML.')
    } catch (err) {
      setXmlError('Error al cargar usuarios desde XML.')
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

      {/* Formulario para cargar archivo XML */}
      <form onSubmit={handleXmlSubmit} style={{ marginBottom: '1.5rem', textAlign: 'center' }}>
        <input
          type="file"
          accept=".xml"
          onChange={e => setXmlFile(e.target.files[0])}
          style={{ marginRight: '1rem' }}
        />
        <button type="submit" className="btn primary" style={{ width: 'auto' }}>
          Cargar XML
        </button>
      </form>
      {xmlError && <p className="error">{xmlError}</p>}
      {xmlSuccess && <p style={{ color: '#38a169', textAlign: 'center' }}>{xmlSuccess}</p>}

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
              {/* Mostrar roles */}
              {user.roles && user.roles.length > 0 && (
                <div style={{ marginBottom: '0.5rem' }}>
                  <strong>Roles:</strong>{' '}
                  {user.roles.map((rol, idx) => (
                    <span
                      key={idx}
                      style={{
                        display: 'inline-block',
                        background: '#667eea22',
                        color: '#667eea',
                        borderRadius: '8px',
                        padding: '0.2em 0.7em',
                        marginRight: '0.4em',
                        fontSize: '0.95em',
                        fontWeight: 500,
                      }}
                    >
                      {rol}
                    </span>
                  ))}
                </div>
              )}
              {/* Mostrar pasatiempos */}
              {user.pasatiempos && user.pasatiempos.length > 0 && (
                <div style={{ marginBottom: '0.5rem' }}>
                  <strong>Pasatiempos:</strong>{' '}
                  {user.pasatiempos.map((p, idx) => (
                    <span
                      key={idx}
                      style={{
                        display: 'inline-block',
                        background: '#38a16922',
                        color: '#276749',
                        borderRadius: '8px',
                        padding: '0.2em 0.7em',
                        marginRight: '0.4em',
                        fontSize: '0.95em',
                      }}
                    >
                      {p}
                    </span>
                  ))}
                </div>
              )}
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
