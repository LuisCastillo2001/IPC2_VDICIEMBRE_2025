package com.ejemploipc2.service;

import com.ejemploipc2.model.Usuario;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class UsuarioServiceImpl implements UsuarioService {

    private final List<Usuario> usuarios = new ArrayList<>();
    private Long contadorId = 1L;

    public UsuarioServiceImpl() {
        usuarios.add(new Usuario(contadorId++, "Juan Pérez", "juan@mail.com"));
        usuarios.add(new Usuario(contadorId++, "María López", "maria@mail.com"));
    }

    @Override
    public List<Usuario> obtenerUsuarios() {
        return usuarios;
    }


    @Override
    public Usuario obtenerUsuarioPorId(Long id) {
        for (Usuario u : usuarios) {
            if (u.getId().equals(id)) {
                return u;
            }
        }
        return null;
    }


    @Override
    public Usuario crearUsuario(Usuario usuario) {
        usuario.setId(contadorId++);
        usuarios.add(usuario);
        return usuario;
    }


    @Override
    public Usuario actualizarUsuario(Long id, Usuario usuarioActualizado) {

        Usuario usuarioExistente = obtenerUsuarioPorId(id);

        if (usuarioExistente == null) {
            return null;
        }

        usuarioExistente.setNombre(usuarioActualizado.getNombre());
        usuarioExistente.setCorreo(usuarioActualizado.getCorreo());

        return usuarioExistente;
    }


    @Override
    public boolean eliminarUsuario(Long id) {
        return usuarios.removeIf(u -> u.getId().equals(id));
    }
}
