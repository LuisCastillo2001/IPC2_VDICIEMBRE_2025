package com.ejemploipc_2.controller;
import com.ejemploipc_2.model.Usuario;
import com.ejemploipc_2.service.UsuarioService;
import com.ejemploipc_2.service.UsuarioServiceImpl;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.LinkedList;

@RestController
@RequestMapping("/usuarios")
public class UsuarioController {

    private final UsuarioService usuarioService;

    public UsuarioController(UsuarioService usuarioService){
        this.usuarioService = usuarioService;
    }

    @GetMapping
    public ResponseEntity<?> listarUsuarios(){
        return ResponseEntity.ok(usuarioService.obtenerUsuarios());
    }

    @GetMapping("/{id}")
    public ResponseEntity<?> obtenerUsuarioPorId(@PathVariable Long id){
        Usuario u = usuarioService.obtenerUsuarioPorId(id);
        if (u == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(u);
    }

    @PostMapping
    public ResponseEntity<?> crearUsuario(@RequestBody Usuario usuario){
        return ResponseEntity.status(201).body(usuarioService.crearUsuario(usuario));
    }


    @PostMapping("/batch")
    public ResponseEntity<?> crearUsuarios(@RequestBody LinkedList<Usuario> usuarios){
        return ResponseEntity.status(201).body(usuarioService.crearUsuarios(usuarios));
    }

    @PutMapping("/{id}")
    public ResponseEntity<?> actualizarUsuario(
            @PathVariable Long id,
            @RequestBody Usuario usuario
    ) {
        Usuario actualizado = usuarioService.actualizarUsuario(id, usuario);
        if (actualizado == null){
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(actualizado);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<?> eliminarUsuario(@PathVariable Long id){
        boolean eliminado = usuarioService.eliminarUsuario(id);
        if (!eliminado){
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.noContent().build();
    }
}





