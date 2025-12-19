import java.util.LinkedList;


public class Main {

    public static void imprimirTitulo(String texto){
        System.out.println("\n==="+ texto + "===");
    }

    public static int sumar(int x, int y){
        return x + y;
    }


    public static void main(String[] args){

        imprimirTitulo("Tipos de datos");

        int edad = 25;
        double altura = 1.75;
        boolean activo = true;
        char genero = 'M';
        String nombre = "Luis";


        imprimirTitulo("Operadores");
        int a = 10;
        int b = 3;

        System.out.println(a+b);
        System.out.println(a-b);
        System.out.println(a *b);


        if (edad >= 18){
            System.out.println("Es mayor de edad");
        }else{
            System.out.println("Es menor de edad");
        }


        imprimirTitulo("LinkedList y objetos");


        LinkedList<Persona> personas = new LinkedList<>();

        personas.add(new Persona("Luis", 24, 1.76, activo));
        personas.add(new Persona("Jessica", 24, 1.65, activo));
        personas.add(new Persona("Juan", 16, 1.80, false));

        imprimirTitulo("For each");

        for (Persona p: personas){
            p.saludar();

            if (p.esMayorDeEdad()){
                System.out.println("Es mayor de edad");
            } else{
                System.out.println("Es menor de edad");
            }
        }

        imprimirTitulo("For normal");


        for (int i = 0; i < personas.size(); i++){
            System.out.println(personas.get(i).getNombre());
        }

        imprimirTitulo("While");
        int contador = 0;
        while(contador < personas.size()){
            System.out.println(personas.get(contador).getEdad());
            
            contador++;
        }

        personas.remove();
        for (int i = 0; i < personas.size(); i++){
            System.out.println(personas.get(i).getNombre());
        }
        

        imprimirTitulo("Fin del repaso");


    }
}