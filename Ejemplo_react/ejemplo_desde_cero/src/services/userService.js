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


export const obtenerUsuarioPorId = async(id) =>{
    try{
        const response = await fetch(`${API_URL}/${id}`)
        if (!response.ok){
            throw new Error('Error al obtener el usuario')
        }
        const data = await response.json()
        return data

    }catch (error){
        console.error('Error al obtener usuario por id', error)
        throw error
    }
}

export const EliminarUsuarioPorid = async(id) =>{
    try{
        const response = await fetch(`${API_URL}/${id}`,{
            method: 'DELETE',
        })
        if (!response.ok){
            throw new Error('Error al eliminar el usuario')
        }
        const data = await response.json()
        return data
    }catch (error){
        console.error('Error al eliminar usuario por id', error)
        throw error
    }
}


export const cargarUsuariosDesdeXml = async (file) => {
    const formData = new FormData();
    formData.append('file', file);

    try{
        const response = await fetch(`${API_URL}/leer-xml`,{
            method: 'POST',
            body: formData
    });
    if (!response.ok){
        throw new Error('Error al cargar archivo desde el xml');

    }

    const data = await response.json()
    return data;
    }catch(error){
        console.error("Error al cargar usuarios desde el xml", error);
        throw error;
    }
}
