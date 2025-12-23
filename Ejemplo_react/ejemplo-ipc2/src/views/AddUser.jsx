import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { crearUsuario } from '../services/userService'

// Opciones fijas para roles y pasatiempos
const ROLES = ['ADMIN', 'USER', 'INVITADO']
const PASATIEMPOS = ['Futbol', 'Lectura', 'Música', 'Videojuegos', 'Viajar']

export default function AddUser() {
  const [nombre, setNombre] = useState('')
  const [correo, setCorreo] = useState('')
  const [roles, setRoles] = useState([])
  const [pasatiempos, setPasatiempos] = useState([])
  const [error, setError] = useState('')
  const navigate = useNavigate()

  const handleRoleChange = (e) => {
    const value = e.target.value
    setRoles(prev =>
      e.target.checked ? [...prev, value] : prev.filter(r => r !== value)
    )
  }

  const handlePasatiempoChange = (e) => {
    const value = e.target.value
    setPasatiempos(prev =>
      e.target.checked ? [...prev, value] : prev.filter(p => p !== value)
    )
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')

    if (!nombre || !correo) {
      setError('Por favor completa todos los campos.')
      return
    }

    const nuevoUsuario = {
      nombre: nombre,
      correo: correo,
      roles: roles,
      pasatiempos: pasatiempos
    }

    try {
      await crearUsuario(nuevoUsuario)
      navigate('/usuarios')
    } catch (err) {
      setError('Error al crear el usuario.')
      console.error(err)
    }
  }

  return (
    <section>
      <h2 className="title">Agregar Usuario</h2>
      <form className="form" onSubmit={handleSubmit}>
        
        <div className="form-row">
          <label htmlFor="nombre">Nombre</label>
          <input
            id="nombre"
            type="text"
            value={nombre}
            onChange={(e) => setNombre(e.target.value)}
            placeholder="Jessica"
          />
        </div>

        <div className="form-row">
          <label htmlFor="correo">Correo</label>
          <input
            id="correo"
            type="email"
            value={correo}
            onChange={(e) => setCorreo(e.target.value)}
            placeholder="jessi@mail.com"
          />
        </div>

        {/* Checklist de roles */}
        <div className="form-row">
          <label>Roles</label>
          <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
            {ROLES.map((rol) => (
              <label key={rol} style={{
                display: 'flex', alignItems: 'center', gap: '0.4em',
                background: roles.includes(rol) ? '#667eea22' : 'transparent',
                borderRadius: '8px', padding: '0.2em 0.7em'
              }}>
                <input
                  type="checkbox"
                  value={rol}
                  checked={roles.includes(rol)}
                  onChange={handleRoleChange}
                />
                <span style={{ color: '#667eea', fontWeight: 500 }}>{rol}</span>
              </label>
            ))}
          </div>
        </div>

        {/* Checklist de pasatiempos */}
        <div className="form-row">
          <label>Pasatiempos</label>
          <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
            {PASATIEMPOS.map((p) => (
              <label key={p} style={{
                display: 'flex', alignItems: 'center', gap: '0.4em',
                background: pasatiempos.includes(p) ? '#38a16922' : 'transparent',
                borderRadius: '8px', padding: '0.2em 0.7em'
              }}>
                <input
                  type="checkbox"
                  value={p}
                  checked={pasatiempos.includes(p)}
                  onChange={handlePasatiempoChange}
                />
                <span style={{ color: '#276749' }}>{p}</span>
              </label>
            ))}
          </div>
        </div>

        {error && <p className="error">{error}</p>}

        <div className="form-actions">
          <button type="submit" className="btn primary">
            Guardar
          </button>
        </div>
      </form>
    </section>
  )
}
