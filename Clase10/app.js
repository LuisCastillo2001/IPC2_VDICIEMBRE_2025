// Variables

let nombre = "Carlos";
const edad = 21;

// tipos de datos

let activo = true;
let precio = 150.75;
let usuario = {
    nombre: "Ana",
    rol: "Estudiante"
}

// Estructuras de control

if (edad >= 18){
    console.log("Es mayor de edad")
} else{
    console.log("Es menor de edad")
}


// bucle

for (let i = 1; i <= 3; i++ ){
    console.log("Iteracion", i);
}

contador = 0

while (contador < 5){
    console.log(contador);
    contador++;

}

let k = 6;


console.log("Bucle do while")
do {
    console.log(k);
    k++;
} while (k < 5)


// Funciones

function saludar(persona) {
    return "Hola " + persona
}

console.log(saludar("Luis"))


// Funciones flecha

const despedir = persona => "Adios " + persona;

// arreglos

console.log("--------Arreglos------------")
let numeros = [10, 20, 30, 40]


// Metodos principales de arreglos

console.log("Metodos de arreglos")

let dobles = numeros.map( n => n * 2 )

let mayores = numeros.filter(n => n > 20)

let suma = numeros.reduce((total, n)  => total +  n, 0)
console.log(suma)

let encontrados = numeros.find(n => n > 20);

console.log(encontrados)

let producto = {
    nombre: "Laptop",
    precio: 8000,
    disponible: true
};


// Map

let roles = new Map()

roles.set("admin", "Luis")
roles.set("editor", "Maria")

console.log(roles.get("admin"))

// DOM

/**********************
 * DOM - SELECCIÓN DE ELEMENTOS
 **********************/
const titulo = document.getElementById("titulo"); // <h1 id="titulo">Fundamentos de JavaScript</h1>



const descripcion = document.getElementById("descripcion");
const btnCambiar = document.getElementById("btnCambiar");
const btnAgregar = document.getElementById("btnAgregar"); // <button id="btnAgregar">Agregar elemento</button>
const lista = document.getElementById("lista");
const btnRenderUsuarios = document.getElementById("btnRenderUsuarios");
const btnLimpiar = document.getElementById("btnLimpiar");
const btnToggle = document.getElementById("btnToggle");
const nuevoTexto = document.getElementById("nuevoTexto");
const root = document.getElementById("root"); // <div id="root"></div>
const btnContador = document.getElementById("btnContador");
const lblContador = document.getElementById("lblContador");

// querySelector / querySelectorAll (formas modernas de seleccionar)
const primerBoton = document.querySelector("button");
const todosLosBotones = document.querySelectorAll("button");
console.log("Primer botón:", primerBoton?.id);
console.log("Total de botones:", todosLosBotones);



// Eventos y manipulacion del dom

btnCambiar.addEventListener("click", () =>{
    titulo.textContent = "Javascript en accion";
    descripcion.textContent = "El dom ha sido modificado usando javascript"
});


btnAgregar.addEventListener("click", () =>{
    const li = document.createElement("li");
    li.textContent = "Elemento agregado desde javascript"
    lista.appendChild(li)
})


// Toggle de clases

btnToggle.addEventListener("click", ()=>{  // <button id="btnToggle">Toggle destacado</button>
    titulo.classList.toggle("destacado"); // <h1 id="titulo" class = "destacado">Fundamentos de JavaScript</h1>
})

const renderLista = (items) => {

    lista.innerHTML = items
        .map((text, idx) => `<li data-idx="${idx}">${idx + 1}. ${text} <button data-action="remove">x</button></li>`) 
        .join("----------");
};

btnRenderUsuarios.addEventListener("click", () => {
    const usuariosBasicos = ["Ana", "Luis", "María", "Diego"];
    renderLista(usuariosBasicos);
});


// Mini "mental model" hacia React: funciones puras que crean nodos
const Card = ({ title, subtitle }) => {
    const div = document.createElement("div");
    div.className = "card";
    const h3 = document.createElement("h3");
    h3.textContent = title;
    const small = document.createElement("div");
    small.className = "muted";
    small.textContent = subtitle;
    div.append(h3, small);
    return div;
};

const render = (container, ...children) => {
    container.replaceChildren(...children);
};

const mostrarCatalogo = () => {
    const data = [
        { title: "Curso JS", subtitle: "DOM + ES6" },
        { title: "Intro React", subtitle: "Componentes y estado" },
    ];
    // console.log(data.map(Card));
    render(root, ...data.map(Card)); // <div id="root"></div> ["<div><h3>Curso Javascript</h3> DOM+ES6</div>", <div><h3>Intro react</h3> Componentes y estados</div>]
};


let count = 0;

btnContador.addEventListener("click", () =>{
    count += 1;
    lblContador.textContent = String(count)
})



// Consumo de api

fetch("https://jsonplaceholder.typicode.com/users")
    .then(res => res.json())
    .then(data => {
        console.log("Usuarios desde API:", data.slice(0, 3));
    });

mostrarCatalogo();






