import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { crearUsuario } from '../services/userService'

export default function AddUser() {
  const [nombre, setNombre] = useState('')
  const [correo, setCorreo] = useState('')
  const [error, setError] = useState('')
  const navigate = useNavigate()

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')

    if (!nombre || !correo) {
      setError('Por favor completa todos los campos.')
      return
    }

    const nuevoUsuario = {
      nombre: nombre,
      correo: correo
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
