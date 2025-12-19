public class Persona {

    // Atributos encapsulados

    private String nombre;
    private int edad;
    private double altura;
    private boolean activo;
    

    // Constructor
    public Persona(String nombre, int edad, double altura, boolean activo){
        this.nombre = nombre;
        this.edad = edad;
        this.altura = altura;
        this.activo = activo;
    }


    // Getter y setter

    public String getNombre(){
        return nombre;
    }

    public void setNombre(String nombre){
        this.nombre = nombre;
    }

    public int getEdad(){
        return edad;
    }

    public void setEdad(int edad){
        this.edad = edad;
    }

    public double getAltura(){
        return altura;
    }

    public void setAltura(double altura){
        this.altura = altura;
    }

    public boolean isActivo(){
        return activo;
    }


    public void saludar(){
        System.out.println("Hola, mi nombre es " + nombre);
    }

    public boolean esMayorDeEdad(){
        return edad >= 18;
    }

}