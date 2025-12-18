package com.ejemploipc2.service;

import com.ejemploipc2.model.Usuario;
import java.util.List;

public interface UsuarioService {

    List<Usuario> obtenerUsuarios();

    Usuario obtenerUsuarioPorId(Long id);

    Usuario crearUsuario(Usuario usuario);

    Usuario actualizarUsuario(Long id, Usuario usuario);

    boolean eliminarUsuario(Long id);
}
