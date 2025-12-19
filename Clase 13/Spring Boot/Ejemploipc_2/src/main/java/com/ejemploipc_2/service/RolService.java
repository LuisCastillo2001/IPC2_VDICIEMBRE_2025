package com.ejemploipc_2.service;

import com.ejemploipc_2.model.Rol;
import java.util.LinkedList;

public interface RolService {
    LinkedList<Rol> listar();
    Rol crear(Rol rol);
}
