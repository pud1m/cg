package raytracer;

import raytracer.math.Vector3;

public class RayResponse {

    // Indica se houve interseção com algum objeto
    public boolean intersected;
    // O valor de "t" do raio para quando houve interseção.
    // Se tiver acontecido duas interseções (raio entrou e saiu), 
    // guardar o menor valor.
    public double t;
    // O ponto (x,y,z) da superfície do objeto onde houve a interseção 
    // no valor de "t" igual a "intersectionT"
    public Vector3 Q;
    // O vetor normal do objeto atingido, calculado no 
    // ponto de interseção ("intersectionPoint")
    public Vector3 normal;

    public RayResponse() {
        this.intersected = false;
        this.t = Double.MAX_VALUE;
    }
}
