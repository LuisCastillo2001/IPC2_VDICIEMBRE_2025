package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @GetMapping("/hola")
    public String hola() {
        return "Hola Spring Boot ";
    }

    @GetMapping("/prueba")
    public String prueba() {
        return "Hola desde prueba";
    }
}


# Aplicacion de ejemplo con React y Vite

Instalar nodejs
npm create vite@latest 

Seleccionar React
Seleccionar JavaScript
cd clase_11_react
npm install
npm run dev

Abrir en el navegador http://localhost:5173/