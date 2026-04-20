# Projeto A3 - Modelagem de Retrato Falado e Reconhecimento Facial

## Descrição do Projeto
Este projeto tem como objetivo integrar técnicas de Computação Gráfica, Processamento de Imagens e Visão Computacional para simular aplicações utilizadas em investigações forenses. O sistema desenvolvido gera um retrato falado digital a partir de elementos faciais e submete a imagem gerada a algoritmos de reconhecimento para encontrar possíveis suspeitos em uma base de dados.

Projeto desenvolvido para a UC de Computação Gráfica e Realidade Virtual do curso de Ciência da Computação (Una Uberlândia).

## Status do Projeto: Etapa 3 Concluída
O sistema já realiza a composição de imagens e o pré-processamento exigido para visão computacional.

### Funcionalidades Implementadas
1. **Modelagem Gráfica (Etapa 1 & 2):** Composição de rostos usando camadas transparentes (PNG).
2. **Fusão e Exportação:** Alinhamento de componentes e salvamento do `retrato_falado_suspeito.png`.
3. **Pré-processamento (Etapa 3):** Conversão para escala de cinza, normalização de tamanho e detecção facial utilizando Haar Cascade.

## Tecnologias Utilizadas
* Linguagem: Python
* Bibliotecas: OpenCV, Pillow, NumPy, Matplotlib
* Base de Dados: AT&T Face Database (Kaggle)

## Estrutura do Repositório
* `/assets`: Biblioteca de componentes faciais.
* `/dataset`: Banco de dados simulado da polícia (pastas `s1` a `s40`).
* `/src`: Códigos-fonte.
* `retrato_falado_suspeito_processado.png`: Imagem da face isolada e normalizada, pronta para a rede de reconhecimento.

## Próximos Passos (Em andamento)
* Extração de características utilizando Eigenfaces ou LBPH.
* Comparação da imagem pré-processada com o banco de dados.
* Exibição do ranking de similaridade (Top 5).