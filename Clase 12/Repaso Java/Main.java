import java.util.LinkedList;

public class Main {

    // ======================
    // MÉTODO PROPIO (función)
    // ======================
    public static void imprimirTitulo(String texto) {
        System.out.println("\n=== " + texto + " ===");
    }

    public static int sumar(int x, int y) {
        return x + y;
    }

    public static void main(String[] args) {

        // ======================
        // TIPOS DE DATOS BÁSICOS
        // ======================
        imprimirTitulo("Tipos de datos");

        int edad = 25;                 // entero
        double altura = 1.75;          // decimal
        boolean activo = true;         // booleano
        char genero = 'M';             // carácter
        String nombre = "Luis";        // String (objeto)

        System.out.println("Edad: " + edad);
        System.out.println("Altura: " + altura);
        System.out.println("Activo: " + activo);
        System.out.println("Genero: " + genero);
        System.out.println("Nombre: " + nombre);

        // ======================
        // OPERADORES
        // ======================
        imprimirTitulo("Operadores");

        int a = 10;
        int b = 3;

        System.out.println("Suma: " + sumar(a, b)); // uso de método
        System.out.println("Resta: " + (a - b));
        System.out.println("Multiplicación: " + (a * b));
        System.out.println("División: " + (a / b)); // división entera
        System.out.println("Módulo: " + (a % b));

        // ======================
        // CONDICIONALES
        // ======================
        imprimirTitulo("Condicionales");

        if (edad >= 18) {
            System.out.println("Es mayor de edad");
        } else {
            System.out.println("Es menor de edad");
        }

        // ======================
        // LINKEDLIST
        // ======================
        imprimirTitulo("LinkedList y objetos");

        LinkedList<Persona> personas = new LinkedList<>();

        personas.add(new Persona("Luis", 22, 1.72, true));
        personas.add(new Persona("Ana", 17, 1.60, true));
        personas.add(new Persona("Carlos", 30, 1.80, false));

        // ======================
        // FOR-EACH
        // ======================
        imprimirTitulo("For-each");

        for (Persona p : personas) {
            p.saludar();

            if (p.esMayorDeEdad()) {
                System.out.println("Es mayor de edad");
            } else {
                System.out.println("Es menor de edad");
            }
        }

        // ======================
        // FOR NORMAL
        // ======================
        imprimirTitulo("For normal");

        for (int i = 0; i < personas.size(); i++) {
            System.out.println("Persona " + i + ": " + personas.get(i).getNombre());
        }

        // ======================
        // WHILE
        // ======================
        imprimirTitulo("While");

        int contador = 0;
        while (contador < personas.size()) {
            System.out.println("Edad de " + personas.get(contador).getNombre()
                    + ": " + personas.get(contador).getEdad());
            contador++;
        }

        // ======================
        // SETTERS / GETTERS
        // ======================
        imprimirTitulo("Setters y Getters");

        Persona p1 = personas.getFirst();
        p1.setEdad(p1.getEdad() + 1);
        System.out.println(p1.getNombre() + " ahora tiene " + p1.getEdad() + " años");

        // ======================
        // REMOVE
        // ======================
        imprimirTitulo("Remove");

        personas.removeLast();
        System.out.println("Personas restantes: " + personas.size());

        // ======================
        // BOOLEAN
        // ======================
        imprimirTitulo("Boolean");

        boolean estaActivo = personas.get(0).isActivo();
        System.out.println("¿Está activo? " + estaActivo);

        imprimirTitulo("Fin del repaso");
    }
}
