package com.ejemploipc_2.service;

import com.ejemploipc_2.model.Rol;
import org.springframework.stereotype.Service;

import java.util.LinkedList;

@Service
public class RolServiceImpl implements RolService {

    private final LinkedList<Rol> roles = new LinkedList<>();
    private Long contadorId = 1L;

    @Override
    public LinkedList<Rol> listar() {
        return roles;
    }

    @Override
    public Rol crear(Rol rol) {
        rol.setId(contadorId++);
        roles.add(rol);
        return rol;
    }
}
