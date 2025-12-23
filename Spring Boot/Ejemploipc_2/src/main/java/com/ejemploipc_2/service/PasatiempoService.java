package com.ejemploipc_2.service;

import com.ejemploipc_2.model.Pasatiempo;
import java.util.LinkedList;

public interface PasatiempoService {
    LinkedList<Pasatiempo> listar();
    Pasatiempo crear(Pasatiempo pasatiempo);
}
