package com.ejemploipc_2.controller;

import com.ejemploipc_2.model.Rol;
import com.ejemploipc_2.service.RolService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/roles")
public class RolController {

    private final RolService rolService;

    public RolController(RolService rolService) {
        this.rolService = rolService;
    }

    @GetMapping
    public ResponseEntity<?> listar() {
        return ResponseEntity.ok(rolService.listar());
    }

    @PostMapping
    public ResponseEntity<?> crear(@RequestBody Rol rol) {
        return ResponseEntity.status(201).body(rolService.crear(rol));
    }
}
