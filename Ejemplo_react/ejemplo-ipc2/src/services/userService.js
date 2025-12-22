// URL base del backend
const API_URL = 'http://localhost:8080/usuarios'

// Función para obtener todos los usuarios (GET)
export const obtenerUsuarios = async () => {
  try {
    const response = await fetch(API_URL)
    if (!response.ok) {
      throw new Error('Error al obtener usuarios')
    }
    const data = await response.json()
    return data
  } catch (error) {
    console.error('Error en obtenerUsuarios:', error)
    throw error
  }
}

// Función para crear un nuevo usuario (POST)
export const crearUsuario = async (usuario) => {
  try {
    const response = await fetch(API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(usuario)
    })
    if (!response.ok) {
      throw new Error('Error al crear usuario')
    }
    const data = await response.json()
    return data
  } catch (error) {
    console.error('Error en crearUsuario:', error)
    throw error
  }
}

// Función para obtener un usuario por ID (GET)
export const obtenerUsuarioPorId = async (id) => {
  try {
    const response = await fetch(`${API_URL}/${id}`)
    if (!response.ok) {
      throw new Error('Error al obtener usuario')
    }
    const data = await response.json()
    return data
  } catch (error) {
    console.error('Error en obtenerUsuarioPorId:', error)
    throw error
  }
}

/* 
  EJEMPLO: Cómo hacer petición GET directamente desde un componente JSX
  
  import { useState, useEffect } from 'react'
  
  function MiComponente() {
    const [usuarios, setUsuarios] = useState([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)
    
    useEffect(() => {
      // Función para hacer el GET
      const obtenerDatos = async () => {
        try {
          setLoading(true)
          // Hacer la petición GET
          const response = await fetch('http://localhost:8080/usuarios')
          
          // Verificar si la respuesta fue exitosa
          if (!response.ok) {
            throw new Error('Error al obtener datos')
          }
          
          // Convertir la respuesta a JSON
          const data = await response.json()
          
          // Actualizar el estado con los datos
          setUsuarios(data)
          setError(null)
        } catch (err) {
          console.error('Error:', err)
          setError(err.message)
        } finally {
          setLoading(false)
        }
      }
      
      // Llamar la función
      obtenerDatos()
    }, []) // Array vacío = solo se ejecuta al montar el componente
    
    // Renderizar según el estado
    if (loading) return <p>Cargando...</p>
    if (error) return <p>Error: {error}</p>
    
    return (
      <div>
        {usuarios.map(usuario => (
          <div key={usuario.id}>
            <h3>{usuario.nombre}</h3>
            <p>{usuario.correo}</p>
          </div>
        ))}
      </div>
    )
  }
  
  // EJEMPLO 2: GET con botón (no automático)
  function OtroComponente() {
    const [datos, setDatos] = useState(null)
    
    const handleClick = async () => {
      try {
        const response = await fetch('http://localhost:8080/usuarios')
        const data = await response.json()
        setDatos(data)
      } catch (err) {
        console.error('Error:', err)
      }
    }
    
    return (
      <div>
        <button onClick={handleClick}>Cargar Usuarios</button>
        {datos && <pre>{JSON.stringify(datos, null, 2)}</pre>}
      </div>
    )
  }
*/
