/**********************
 * VARIABLES
 **********************/
let nombre = "Carlos";
const edad = 21;

/**********************
 * TIPOS DE DATOS
 **********************/
let activo = true;
let precio = 150.75;
let usuario = {
    nombre: "Ana",
    rol: "Estudiante"
};

/**********************
 * ESTRUCTURAS DE CONTROL
 **********************/
if (edad >= 18) {
    console.log("Es mayor de edad");
} else {
    console.log("Es menor de edad");
}

/**********************
 * BUCLES
 **********************/
for (let i = 1; i <= 3; i++) {
    console.log("Iteración:", i);
}

/**********************
 * FUNCIONES
 **********************/
function saludar(persona) {
    return "Hola " + persona;
}

/**********************
 * FUNCIONES FLECHA
 **********************/
const despedir = persona => "Adiós " + persona;

/**********************
 * ARREGLOS
 **********************/
let numeros = [10, 20, 30, 40];

/**********************
 * MÉTODOS DE ARREGLOS
 **********************/
let dobles = numeros.map(n => n * 2);
let mayores = numeros.filter(n => n > 20);
let suma = numeros.reduce((total, n) => total + n, 0);
let encontrados = numeros.find(n => n === 30);

console.log("Encontrado:", encontrados);

console.log(dobles, mayores, suma);

/**********************
 * OBJETOS
 **********************/
let producto = {
    nombre: "Laptop",
    precio: 8000,
    disponible: true
};

/**********************
 * MAP
 **********************/
let roles = new Map();
roles.set("admin", "Luis");
roles.set("editor", "María");

console.log(roles.get("admin"));

/**********************
 * DOM - SELECCIÓN DE ELEMENTOS
 **********************/
const titulo = document.getElementById("titulo");
const descripcion = document.getElementById("descripcion");
const btnCambiar = document.getElementById("btnCambiar");
const btnAgregar = document.getElementById("btnAgregar");
const lista = document.getElementById("lista");
const btnRenderUsuarios = document.getElementById("btnRenderUsuarios");
const btnLimpiar = document.getElementById("btnLimpiar");
const btnToggle = document.getElementById("btnToggle");
const nuevoTexto = document.getElementById("nuevoTexto");
const root = document.getElementById("root");
const btnContador = document.getElementById("btnContador");
const lblContador = document.getElementById("lblContador");

// querySelector / querySelectorAll (formas modernas de seleccionar)
const primerBoton = document.querySelector("button");
const todosLosBotones = document.querySelectorAll("button");
console.log("Primer botón:", primerBoton?.id);
console.log("Total de botones:", todosLosBotones.length);

/**********************
 * EVENTOS Y MANIPULACIÓN DEL DOM
 **********************/
btnCambiar.addEventListener("click", () => {
    titulo.textContent = "JavaScript en Acción";
    descripcion.textContent = "El DOM ha sido modificado usando JavaScript";
});

btnAgregar.addEventListener("click", () => {
    const li = document.createElement("li");
    li.textContent = "Elemento agregado desde JavaScript";
    lista.appendChild(li);
});

// Toggle de clases (classList)
btnToggle.addEventListener("click", () => {
    titulo.classList.toggle("destacado");
});

// Agregar elemento con texto desde input


// Render con map: pintar una lista desde un arreglo
const renderLista = (items) => {

    lista.innerHTML = items
        .map((text, idx) => `<li data-idx="${idx}">${idx + 1}. ${text} <button data-action="remove">x</button></li>`) 
        .join("");
};

btnRenderUsuarios.addEventListener("click", () => {
    const usuariosBasicos = ["Ana", "Luis", "María", "Diego"];
    renderLista(usuariosBasicos);
});

btnLimpiar.addEventListener("click", () => {
    lista.innerHTML = "";
});

// Delegación de eventos: manejar clicks en items hijos desde el padre
lista.addEventListener("click", (e) => {
    const t = e.target;
    if (t.matches("button[data-action='remove']")) {
        t.closest("li")?.remove();
    }
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
    console.log(data.map(Card));
    render(root, ...data.map(Card));
};

mostrarCatalogo();

// Un mini estado: contador simple
let count = 0;
btnContador.addEventListener("click", () => {
    count += 1;
    lblContador.textContent = String(count);
});

/**********************
 * CONSUMO DE API
 **********************/
fetch("https://jsonplaceholder.typicode.com/users")
    .then(res => res.json())
    .then(data => {
        console.log("Usuarios desde API:", data.slice(0, 3));
    });

/**********************
 * EXTRA: FLECHAS Y MAP RÁPIDO (para práctica)
 **********************/
// Flecha con retorno implícito
const cuadrado = n => n * n;

// Flecha con parámetros por defecto
const saludar2 = (nombre = "Mundo") => `Hola, ${nombre}`;

// Flecha que retorna objeto (paréntesis)
const crearUsuario = (nombre, rol = "Estudiante") => ({ nombre, rol });

console.log(cuadrado(4), saludar2(), crearUsuario("Sofi"));

// Map (estructura clave-valor) - iteración
for (const [clave, valor] of roles) {
    console.log(`Rol: ${clave} -> ${valor}`);
}
