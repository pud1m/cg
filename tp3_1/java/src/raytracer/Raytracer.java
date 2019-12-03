package raytracer;

import raytracer.math.Vector3;
import raytracer.scene.Camera;
import raytracer.scene.Light;
import raytracer.scene.Material;
import raytracer.scene.objects.Object;
import raytracer.scene.pygments.Pygment;
import raytracer.scene.Scene;

public class Raytracer {

    /**
     * *
     * Cria um raio que vai da posição da câmera e passa pelo pixel indicado por
     * (column, row).
     *
     * @param camera A câmera com as configurações de eye, target e up.
     * @param row A coordenada y do pixel por onde o raio deve passar.
     * @param column A coordenada x do pixel por onde o raio deve passar.
     * @param height O número de linhas totais da imagem.
     * @param width O número de colunas totais da image.
     * @return Um raio que sai da origem da câmera e passa pelo pixel (column,
     * row).
     */
    private Ray generateInitialRay(Camera camera, double row, double column,
            int height, int width) {

        double aspectRatio = ((double) width) / height;
        double heightInCameraSpace = 2 * Math.tan(camera.getFovy() / 2);
        double widthInCameraSpace = heightInCameraSpace * aspectRatio;

        double ur = heightInCameraSpace * (((double) row) / height) - heightInCameraSpace / 2;
        double uc = widthInCameraSpace * (((double) column) / width) - widthInCameraSpace / 2;
        
        Vector3 gridPoint = new Vector3(camera.eye);
        gridPoint = gridPoint.add(camera.cameraBaseX.mult(uc));
        gridPoint = gridPoint.add(camera.cameraBaseY.mult(ur));
        gridPoint = gridPoint.diff(camera.cameraBaseZ);

        Vector3 direction = new Vector3(gridPoint.diff(camera.eye));

        return new Ray(camera.eye, direction.normalized());
    }

    /**
     * *
     * Lança um raio para a cena (camera) que passa por um certo pixel da cena.
     * Retorna a cor desse pixel.
     *
     * @param scene A cena onde o raio será lançado.
     * @param ray O raio a ser lançado.
     * @return A cor com que o pixel (acertado pelo raio) deve ser colorido.
     */
    private Vector3 castRay(Scene scene, Ray ray) {
        // Para todos os objetos da cena, verifica se o raio o acerta e pega aquele
        // que foi atingido primeiro (menor "t")
        RayResponse closestIntersection = new RayResponse();
        Object closestObjectHit = null;
        for (Object obj : scene.objects) {
            RayResponse response = obj.intersectsWith(ray);
            if (response.intersected) {
                if (response.t < closestIntersection.t) {
                    closestIntersection = response;
                    closestObjectHit = obj;
                }
            }
        }

        // Verifica se um objeto foi atingido. Se tiver sido, colore o pixel
        if (closestObjectHit != null) {
            // material e pigmento deste objeto
            Material material= closestObjectHit.material;
            Pygment pygment = closestObjectHit.pygment;
            Vector3 colorAtPoint = pygment.getColorAt(closestIntersection.Q);
            
            // Esta é a variável contendo a COR RESULTANTE do pixel,
            // que deve ser devidamente calculada e retornada ao final
            // deste método (castRay)
            Vector3 shadingColor = colorAtPoint;
            
            // ------------------------------------------------------------------
            // Aqui começamos a implementar a equaçăo de Phong (e armazenar o
            // resultado parcial em shadingColor)
            // Sugiro seguir as anotaçőes do prof. David Mount (p. 83)
            // ---
            // Exercício 1: Coloque a componente ambiente na cor resultante
            // luz ambiente: coefAmbienteDaLuz*corDoPigmento

            
            // Um objeto foi atingido
            // Verificamos se as fontes de luz estão iluminando este objeto
            for (Light light : scene.lights) {
                // Para verificar,
                // ---
                // Exercício 2: crie um raio do ponto de interseção com o
                // objeto até a fonte de luz (basta instanciar devidamente
                // um Ray, ~4 linhas)


                



                // Verificamos se o raio atinge algum objeto ANTES da fonte de luz
                // Se for o caso, esta fonte de luz não contribui para a luz do objeto
                boolean hitsAnotherObjectBeforeLight = false;

                // ---
                // Exercício 3: Percorra os objetos da cena verificando se
                // houve interseção com eles, antes da interseção com a fonte luminosa
                // Salve essa informação na variável hitsAnotherObjectBeforeLight (~10 linhas)

                







                if (!hitsAnotherObjectBeforeLight) {
                    // ---
                    // Exercício 4: Devemos terminar de calcular a equaçăo
                    // de Phong (atenuação, componente difusa e componente
                    // especular) e somar o resultado na cor resultante
                    // (na variável shadingColor, ~15 linhas)

                    








                }
            }

            // [Extra] Exercício 5: se o material for reflexivo, lançar raio de reflexão
            // chamando castRay recursivamente




            
            // [Extra] Exercício 5: se o material for transparente, lançar raio de refração
            // chamando castRay recursivamente





            
            // trunca a cor: faz r, g e b ficarem entre 0 e 1, caso tenha excedido
            shadingColor.truncate();
            
            return shadingColor;
	}

        
	// nada foi atingido. Retorna uma cor padrão (de fundo)
	return new Vector3(0, 0, 0);
        
    }
    /**
     * *
     * MÉTODO que renderiza uma cena, gerando uma matriz de cores.
     *
     * @param scene um objeto do tipo Scene contendo a descrição da cena (ver
     * Scene.java)
     * @param height altura da imagem que estamos gerando (e.g., 600px)
     * @param width largura da imagem que estamos gerando (e.g., 800px)
     * @return uma matriz de cores (representadas em Vector3 - r,g,b)
     */
    public Vector3[][] renderScene(Scene scene, int height, int width) {
        Vector3[][] pixels = new Vector3[height][width];

        // Para cada pixel, lança um raio
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                // cria um raio primário
                Ray ray = generateInitialRay(scene.camera, i, j, height, width);

                // lança o raio e recebe a cor
                Vector3 color = castRay(scene, ray);

                // salva a cor na matriz de cores
                pixels[i][j] = color;
            }
        }
        
        return pixels;
    }
}
