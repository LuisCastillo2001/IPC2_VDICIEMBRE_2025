package com.ejemploipc_2.service;
import com.ejemploipc_2.model.Usuario;

import java.util.LinkedList;
import java.util.List;
import java.io.InputStream;

public interface UsuarioService {
    LinkedList<Usuario> obtenerUsuarios();
    Usuario obtenerUsuarioPorId(Long id);
    Usuario crearUsuario(Usuario usuario);
    Usuario actualizarUsuario(Long id, Usuario usuario);
    boolean eliminarUsuario(Long id);
    LinkedList<Usuario> crearUsuarios(LinkedList<Usuario> usuarios);
    List<Usuario> leerUsuariosDesdeXml(InputStream inputStream);


}
