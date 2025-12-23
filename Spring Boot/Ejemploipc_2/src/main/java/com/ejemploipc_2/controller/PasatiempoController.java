package com.ejemploipc_2.controller;

import com.ejemploipc_2.model.Pasatiempo;
import com.ejemploipc_2.service.PasatiempoService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/pasatiempos")
public class PasatiempoController {

    private final PasatiempoService pasatiempoService;

    public PasatiempoController(PasatiempoService pasatiempoService) {
        this.pasatiempoService = pasatiempoService;
    }

    @GetMapping
    public ResponseEntity<?> listar() {
        return ResponseEntity.ok(pasatiempoService.listar());
    }

    @PostMapping
    public ResponseEntity<?> crear(@RequestBody Pasatiempo pasatiempo) {
        return ResponseEntity.status(201).body(pasatiempoService.crear(pasatiempo));
    }
}
