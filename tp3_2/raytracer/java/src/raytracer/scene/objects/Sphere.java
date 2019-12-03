package raytracer.scene.objects;

import raytracer.Ray;
import raytracer.RayResponse;
import raytracer.math.Constants;
import raytracer.math.Vector3;

/**
 * Uma esfera, que tem uma posição do seu centro e um raio.
 *
 */
public class Sphere extends Object {

    private final Vector3 center;
    private final double radius;

    public Sphere(Vector3 center, double radius) {
        this.center = center;
        this.radius = radius;
    }

    /**
     * * Retorna um objeto do tipo RayResponse com informações sobre uma possível
     * interseção do raio com este objeto.
     *
     * O objeto response deve preencher os seguintes valores: -
     * response.intersected, true/false indicando se houve interseção ou não -
     * response.intersectionT, o valor t do raio da primeira interseção, caso haja
     * mais que 1 interseção - response.intersectionPoint, contendo o ponto (x,y,z)
     * de interseção - ray.intersectionNormal, contendo o vetor normal do objeto no
     * ponto de interseção. A normal deve ser *normalizada* (norma = 1)
     *
     *
     * @param ray o raio sendo lançado.
     * @return objeto com a resposta da colisão.
     */
    @Override
    public RayResponse intersectsWith(Ray ray) {
        Vector3 u = ray.u.normalized();
        Vector3 P0 = ray.P;
        Vector3 C = center;
        Vector3 p = C.diff(P0);
        double r = radius;

        // coeficientes e cálculo da equação de segundo grau que representa
        // a possibilidade de interseção do raio com a esfera
        double a = 1;
        double b = (-2) * u.dot(p);
        double c = p.dot(p) - Math.pow(r, 2);
        double delta = Math.pow(b, 2) - 4 * a * c;
        double root1, root2;

        double t = Double.MAX_VALUE;
        boolean hitFromInside = false;

        RayResponse response = new RayResponse();

        // estuda o delta para saber quantas interseções houve
        if (delta < -Constants.TINY) {
            return response;
        } else if (delta > Constants.TINY) {
            // duas interseções
            root1 = (-b - Math.sqrt(delta)) / (2 * a);
            root2 = (-b + Math.sqrt(delta)) / (2 * a);
            if (root1 > Constants.TINY) {
                t = root1;
            } else if (root2 > Constants.TINY) {
                t = root2;
                hitFromInside = true;
            } else {
                return response;
            }
        } else {
            // uma interseção
            root1 = -b / (2 * a);
            if (root1 > Constants.TINY) {
                t = root1;
            } else {
                return response;
            }
        }

        // agora que temos t, podemos calcular P (ponto de interseção) e então
        // o vetor normal
        Vector3 P = P0.add(u.mult(t));
        Vector3 n = P.diff(C).normalized();

        // preenche a resposta
        response.intersected = true;
        response.t = t;
        response.Q = P;
        response.normal = !hitFromInside ? n : n.mult(-1);

        return response;
    }

    @Override
    public Vector3 getCenter() {
        return center;
    }

    @Override
    public String getGeometryName() {
        return "sphere";
    }
}
