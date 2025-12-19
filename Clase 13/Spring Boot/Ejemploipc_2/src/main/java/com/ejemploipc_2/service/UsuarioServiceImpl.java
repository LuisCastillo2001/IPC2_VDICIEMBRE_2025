package com.ejemploipc_2.service;
import com.ejemploipc_2.model.Usuario;
import org.springframework.stereotype.Service;


import java.util.ArrayList;
import java.util.LinkedList;

// objeto Spring
// Spring tendrá ese servicio por si alguien lo quiere usar
@Service
public class UsuarioServiceImpl implements  UsuarioService {
    private final LinkedList<Usuario> usuarios = new LinkedList<>();
    private Long contadorId= 1L;

    public UsuarioServiceImpl(){

    }


    @Override

    public LinkedList<Usuario> obtenerUsuarios(){
        return usuarios;
    }

    @Override
    public Usuario obtenerUsuarioPorId(Long id){
        for (Usuario u : usuarios){
            if (u.getId().equals(id)){
                return u;
            }
        }
        return null;
    }

    @Override

    public Usuario crearUsuario(Usuario usuario){
        usuario.setId(contadorId++);
        usuarios.add(usuario);
        return usuario;
    }


    @Override

    public Usuario actualizarUsuario(Long id, Usuario usuarioActualizado){

        Usuario usuarioExistente = obtenerUsuarioPorId(id);

        if (usuarioExistente == null){
            return null;
        }

        usuarioExistente.setNombre(usuarioActualizado.getNombre());
        usuarioExistente.setCorreo(usuarioActualizado.getCorreo());

        return usuarioExistente;
    }


    @Override
    public boolean eliminarUsuario(Long id){

        for (int i = 0; i < usuarios.size(); i++){
            if (usuarios.get(i).getId().equals(id)){
                usuarios.remove(i);
                return true;
            }
        }
        return false;

    }

    @Override
    public LinkedList<Usuario> crearUsuarios(LinkedList<Usuario> nuevosUsuarios) {
        for (Usuario u : nuevosUsuarios) {
            u.setId(contadorId++);
            usuarios.add(u);
        }
        return nuevosUsuarios;
    }


}
