import {useState, useEffect} from 'react'

import {Link} from 'react-router-dom'


import { obtenerUsuarios } from '../services/userService' 


export default function Users(){

    // users = []
    

    const [users, setUsers] = useState([])

    const [loading, setLoading] = useState(true)

    const [error, setError] = useState(null)


    useEffect(() => {
        cargarUsuarios()
    }, [])

    const cargarUsuarios = async () =>{
        try{
            setLoading(true)
            setError(null)

            // Hacer el get al backend
            const data = await obtenerUsuarios()

            
            setUsers(data)
            
            
        } catch (err ){
            setError('No se pudieron cargar los usuarios')
            console.error('Error al cargar los usuarios', err)
        } finally{
            setLoading(false)
        }
    }

    console.log("Usuarios cargados")
    console.log(users)

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

  return (
    <section>
        <h2 className='tittle'>Lista de Usuarios</h2>
        {users.length === 0 ? (
            <p> No hay usuarios registrados</p>
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
        )
    
    }
    </section>
  )


}