// Vista de Inicio: explica brevemente qué hace el sistema.
export default function Home() {
  return (
    <section>
      <h1 className="title">Mini App de Gestión de Usuarios</h1>
      <p className="lead">
        Este ejemplo muestra lo básico de React y React Router:
      </p>
      <ul className="features">
        <li>Navegación entre páginas sin recargar (SPA)</li>
        <li>Estado en memoria para una lista de usuarios</li>
        <li>Props para pasar datos entre componentes</li>
        <li>Eventos y formularios controlados</li>
        <li>Rutas con parámetros para ver el detalle</li>
        <li>Renderizado condicional y listas con claves únicas</li>
      </ul>
      <p>
        Usa el menú superior para visitar la lista de usuarios o agregar uno
        nuevo. No hay backend: los datos viven en memoria mientras la app está
        abierta.
      </p>
    </section>
  )
}
