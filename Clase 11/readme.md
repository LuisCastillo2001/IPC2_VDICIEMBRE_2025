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
