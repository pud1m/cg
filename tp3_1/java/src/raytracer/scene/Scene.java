package raytracer.scene;

import raytracer.scene.pygments.Pygment;
import raytracer.scene.objects.Object;
import java.util.ArrayList;

public class Scene {

    public Camera camera;
    public ArrayList<Light> lights;
    public ArrayList<Pygment> pygments;
    public ArrayList<Material> materials;
    public ArrayList<Object> objects;

    public Scene() {
        camera = new Camera();
    }

    public String debugInfo() {
        StringBuilder info = new StringBuilder();
        info.append("Informacoes sobre a cena:\n");
        info.append("\tCamera:\n\t\teye: ").append(camera.eye.debugInfo());
        info.append("\n\t\ttarget: ").append(camera.target.debugInfo());
        info.append("\n\t\tup: ").append(camera.up.debugInfo());
        info.append("\n\t\tfovY: ").append(camera.getFovy());
        info.append("\n");

        info.append("\n\tLuzes: ").append(lights.size()).append("\n");
        for (Light l : lights) {
            info.append("\t\tposition: ").append(l.position.debugInfo()).append("\n");
            info.append("\t\tcolor: ").append(l.color.debugInfo()).append("\n");
            info.append("\t\tatenuacoes: ").append(String.format("%f, %f, %f",
                    l.constantAttenuation, l.linearAttenuation,
                    l.quadraticAttenuation)).append("\n");
        }

        info.append("\n\tPigmentos: ").append(pygments.size()).append("\n");
        for (Pygment p : pygments) {
            info.append("\t\ttipo: ").append(p.getPygmentName()).append("\n");
        }

        info.append("\n\tMateriais: ").append(materials.size()).append("\n");
        for (Material m : materials) {
            info.append("\t\tambiente: ").append(m.ambientCoefficient).append("\n");
            info.append("\t\tdifuso: ").append(m.diffuseCoefficient).append("\n");
            info.append("\t\tespecular: ").append(m.specularCoefficient).append("\n");
            info.append("\t\texpoente espec.: ").append(m.specularExponent).append("\n");
            info.append("\t\tindice reflex.: ").append(m.reflectionCoefficient).append("\n");
            info.append("\t\tindice refrac.: ").append(m.transmissionCoefficient).append("\n");
            info.append("\t\tsnell: ").append(m.snellCoefficient).append("\n");
        }

        info.append("\n\tObjetos: ").append(objects.size()).append("\n");
        for (Object o : objects) {
            info.append("\t\ttipo: ").append(o.getGeometryName()).append("\n");
            info.append("\t\tposicao: ").append(o.getCenter().debugInfo()).append("\n");
            info.append("\t\tpigmento: ").append(o.pygment.getPygmentName()).append("\n");
        }

        return info.toString();
    }
}
