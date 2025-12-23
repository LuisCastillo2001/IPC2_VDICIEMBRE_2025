const API_URL = 'http://localhost:8080/usuarios'

// Funcion para obtener todos los usuarios

export const obtenerUsuarios = async () =>{
    try{
        const response = await fetch(API_URL)
        if (!response.ok){
            throw new Error("Error al obtener usuarios")
        }

        const data = await response.json()

        /* const data =
        
        [
    {
        "id": 1,
        "nombre": "Luis",
        "correo": "luis@gmail.com"
    },
    {
        "id": 2,
        "nombre": "Jessica",
        "correo": "jessi@mail.com"
    },
    {
        "id": 3,
        "nombre": "Juan",
        "correo": "juan@mail.com"
    }
]

        */

        return data
    } catch(error){
        console.error("Error al obtener usuarios", error)
        throw error
    }
}


// Funcion para crear un nuevo usuario (POST)

export const crearUsuario = async (usuario) => {
    try{
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
           
            body : JSON.stringify(usuario)
        })

        if (!response.ok){
            throw new Error("Error al crear el usuario")
        }

        const data = await response.json()
        return data
    } catch (error){
        console.error("Error al crearUsuario", error)
        throw error
    }

}

