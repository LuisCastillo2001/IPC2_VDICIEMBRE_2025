import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.*;
import java.io.File;

public class Main {

    public static void main(String[] args) {

        try {
            // 1. Crear el parser DOM
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();

            // 2. Leer el XML
            Document doc = builder.parse(new File("estudiantes.xml"));
            doc.getDocumentElement().normalize();

            // 3. Obtener todos los <estudiante>
            NodeList listaEstudiantes = doc.getElementsByTagName("estudiante");

            for (int i = 0; i < listaEstudiantes.getLength(); i++) {

                Element estudiante = (Element) listaEstudiantes.item(i);

                // 4. Atributo id
                String id = estudiante.getAttribute("id");

                // 5. Etiquetas simples
                String nombre = estudiante
                        .getElementsByTagName("nombre")
                        .item(0)
                        .getTextContent();

                String edad = estudiante
                        .getElementsByTagName("edad")
                        .item(0)
                        .getTextContent();

                System.out.println("ID: " + id);
                System.out.println("Nombre: " + nombre);
                System.out.println("Edad: " + edad);

                // 6. Cursos
                Element cursos = (Element)
                        estudiante.getElementsByTagName("cursos").item(0);

                NodeList listaCursos = cursos.getElementsByTagName("curso");

                for (int j = 0; j < listaCursos.getLength(); j++) {

                    Element curso = (Element) listaCursos.item(j);

                    String codigo = curso.getAttribute("codigo");
                    String nombreCurso = curso.getTextContent();

                    System.out.println("  Curso: " + nombreCurso
                            + " (Código: " + codigo + ")");
                }

                System.out.println("----------------------");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
