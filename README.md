# Segmenta-o

- Lista de Segmentação 
    - Este trabalho consite em implementar um script para aplicação de filtros para detecção de bordas em imagens no domínio espacial, no processo de filtragem usasse um processo de convolução de uma máscara pela imagem. Este processo equivale a percorrer toda a imagem alterando seus valores conforme os pesos da máscara e as intensidades da imagem.
    - Sendo que esta sendo aplicado os seguintes filtros em imagens monocromáticas:

        -h1 = [0, 0, -1, 0, 0],

              [0, -1, -2, -1, 0],

              [-1, -2, 16, -2, -1],

              [0, -1, -2, -1, 0],
              
              [0, 0, -1, 0, 0]


        - h2 = (1/256) * [1, 4, 6, 4, 1],
                         [4, 16, 24, 16, 4],
                         [6, 24, 36, 24, 6],
                         [4, 16, 24, 16, 4],
                         [1, 4, 6, 4, 1]


        - h3 = [-1,  0,  1],
               [-2,  0,  2],
               [-1,  0,  1]


        - h4 = [-1, -2, -1],
              [ 0,  0,  0],
              [ 1,  2,  1]


        - h5 = [-1, -1, -1],
               [-1,  8, -1],
               [-1, -1, -1]


        - h6 = (1/9) * [1, 1, 1],
                       [1, 1, 1],
                       [1, 1, 1],

        - h7 = [-1, -1,  2],
               [-1,  2, -1],
               [ 2, -1, -1]


        - h8 = [ 2, -1, -1],
               [-1,  2, -1],
               [-1, -1,  2]


        - h9 = (1/9) * [1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1],

        - h10 = (1/8) * [-1, -1, -1, -1, -1],
                        [-1,  2,  2,  2, -1],
                        [-1,  2,  8,  2, -1],
                        [-1,  2,  2,  2, -1],
                        [-1, -1, -1, -1, -1]


        - h11 = [-1, -1, 0],
                [-1,  0, 1],
                [ 0,  1, 1]
    
        - Também iremos aplicar o filtro sqr(h3^2 + h4^2)

    - Antes de iniciar, crie duas pastas, uma com o nome \input e outra com o nome \output, o script ira aplicar os filtros em todas as imagens em input e salvar a modificação em output.

    - Para iniciar: python filtros.py