package com.ejemploipc_2.controller;
import com.ejemploipc_2.model.Usuario;
import com.ejemploipc_2.service.UsuarioService;
import com.ejemploipc_2.service.UsuarioServiceImpl;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.HttpStatus;
import org.springframework.web.multipart.MultipartFile;

import java.util.LinkedList;
import java.util.List;
import org.w3c.dom.*;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import java.io.File;

@RestController
@RequestMapping("/usuarios")
public class UsuarioController {

    private final UsuarioService usuarioService;

    public UsuarioController(UsuarioService usuarioService){
        this.usuarioService = usuarioService;
    }

    @GetMapping
    public ResponseEntity<?> listarUsuarios(){
        return ResponseEntity.status(HttpStatus.OK).body(usuarioService.obtenerUsuarios());
    }

    @GetMapping("/{id}")
    public ResponseEntity<?> obtenerUsuarioPorId(@PathVariable Long id){
        Usuario u = usuarioService.obtenerUsuarioPorId(id);
        if (u == null) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
        }
        return ResponseEntity.status(HttpStatus.OK).body(u);
    }

    @PostMapping
    public ResponseEntity<?> crearUsuario(@RequestBody Usuario usuario){
        return ResponseEntity.status(HttpStatus.CREATED).body(usuarioService.crearUsuario(usuario));
    }


    @PostMapping("/batch")
    public ResponseEntity<?> crearUsuarios(@RequestBody LinkedList<Usuario> usuarios){
        return ResponseEntity.status(HttpStatus.CREATED).body(usuarioService.crearUsuarios(usuarios));
    }

    @PutMapping("/{id}")
    public ResponseEntity<?> actualizarUsuario(
            @PathVariable Long id,
            @RequestBody Usuario usuario
    ) {
        Usuario actualizado = usuarioService.actualizarUsuario(id, usuario);
        if (actualizado == null){
            return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
        }
        return ResponseEntity.ok(actualizado);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<?> eliminarUsuario(@PathVariable Long id){
        boolean eliminado = usuarioService.eliminarUsuario(id);
        if (!eliminado){
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.status(HttpStatus.OK).build();
    }

    @PostMapping("/leer-xml")
    public ResponseEntity<?> leerXmlUsuarios( MultipartFile file) {

        try {
            List<Usuario> usuarios = usuarioService.leerUsuariosDesdeXml(file.getInputStream());
            return ResponseEntity.ok(usuarios);
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Error leyendo el archivo XML");
        }
    }
}





