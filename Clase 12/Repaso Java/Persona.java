public class Persona {

    // ======================
    // ATRIBUTOS (encapsulados)
    // ======================
    private String nombre;
    private int edad;
    private double altura;
    private boolean activo;

    // ======================
    // CONSTRUCTOR
    // ======================
    public Persona(String nombre, int edad, double altura, boolean activo) {
        this.nombre = nombre;
        this.edad = edad;
        this.altura = altura;
        this.activo = activo;
    }

    // ======================
    // GETTERS y SETTERS
    // ======================
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        if (edad >= 0) {
            this.edad = edad;
        }
    }

    public double getAltura() {
        return altura;
    }

    public boolean isActivo() {
        return activo;
    }

    // ======================
    // MÉTODOS
    // ======================
    public void saludar() {
        System.out.println("Hola, soy " + nombre);
    }

    public boolean esMayorDeEdad() {
        return edad >= 18;
    }
}
