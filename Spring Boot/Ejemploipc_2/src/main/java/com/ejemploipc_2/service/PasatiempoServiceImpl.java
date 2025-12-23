package com.ejemploipc_2.service;

import com.ejemploipc_2.model.Pasatiempo;
import org.springframework.stereotype.Service;

import java.util.LinkedList;

@Service
public class PasatiempoServiceImpl implements PasatiempoService {

    private final LinkedList<Pasatiempo> pasatiempos = new LinkedList<>();

    private Long contadorId = 1L;

    @Override
    public LinkedList<Pasatiempo> listar() {
        return pasatiempos;
    }

    @Override
    public Pasatiempo crear(Pasatiempo pasatiempo) {
        pasatiempo.setId(contadorId++);
        pasatiempos.add(pasatiempo);
        return pasatiempo;
    }
}
