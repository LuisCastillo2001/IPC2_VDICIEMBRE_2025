package com.ejemploipc_2.model;

import java.util.LinkedList;
import java.util.List;

public class Usuario {

    private Long id;
    private String nombre;
    private String correo;
    private List<String> roles;
    private List<String> pasatiempos;


    public Usuario() {
        this.roles = new LinkedList<>();
        this.pasatiempos = new LinkedList<>();
    }

    public Usuario(Long id, String nombre, String correo) {
        this.id = id;
        this.nombre = nombre;
        this.correo = correo;
        this.roles = new LinkedList<>();
        this.pasatiempos = new LinkedList<>();
    }

    public Usuario(Long id, String nombre, String correo, List<String> roles, List<String> pasatiempos) {
        this.id = id;
        this.nombre = nombre;
        this.correo = correo;
        this.roles = roles;
        this.pasatiempos = pasatiempos;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }

    public String getCorreo() { return correo; }
    public void setCorreo(String correo) { this.correo = correo; }

    public List<String> getRoles() { return roles; }
    public void setRoles(List<String> roles) { this.roles = roles; }

    public List<String> getPasatiempos() { return pasatiempos; }
    public void setPasatiempos(List<String> pasatiempos) { this.pasatiempos = pasatiempos; }


}
