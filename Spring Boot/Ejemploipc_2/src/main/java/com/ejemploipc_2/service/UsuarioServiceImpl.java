package com.ejemploipc_2.service;
import com.ejemploipc_2.model.Usuario;
import org.springframework.stereotype.Service;
import org.w3c.dom.*;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import java.io.File;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

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

    @Override
    public List<Usuario> leerUsuariosDesdeXml(InputStream inputStream) {
        usuarios.clear();
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();

            Document doc = builder.parse(inputStream);
            doc.getDocumentElement().normalize();

            NodeList listaUsuarios = doc.getElementsByTagName("usuario");

            for (int i = 0; i < listaUsuarios.getLength(); i++) {
                Element usuarioElem = (Element) listaUsuarios.item(i);

                // Long id = Long.parseLong(usuarioElem.getAttribute("id"));
                String nombre = usuarioElem.getElementsByTagName("nombre").item(0).getTextContent();
                String correo = usuarioElem.getElementsByTagName("correo").item(0).getTextContent();

                List<String> roles = new LinkedList<>();
                NodeList rolesList = usuarioElem.getElementsByTagName("rol");
                for (int j = 0; j < rolesList.getLength(); j++) {
                    roles.add(rolesList.item(j).getTextContent());
                }

                List<String> pasatiempos = new LinkedList<>();
                NodeList pasatiemposList = usuarioElem.getElementsByTagName("pasatiempo");
                for (int j = 0; j < pasatiemposList.getLength(); j++) {
                    pasatiempos.add(pasatiemposList.item(j).getTextContent());
                }
                Long id = contadorId++;
                

                Usuario usuario = new Usuario(id, nombre, correo, roles, pasatiempos);
                usuarios.add(usuario);

            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return usuarios;
    }
}
