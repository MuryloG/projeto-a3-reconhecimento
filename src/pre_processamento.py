import cv2
import os

def pre_processar_imagem(caminho_imagem, tamanho_padrao=(200, 200)):
    # Carrega a imagem gerada
    img = cv2.imread(caminho_imagem)
    if img is None:
        print(f"Erro: Não foi possível carregar a imagem em {caminho_imagem}")
        return None

    # Conversão para escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Carrega o classificador Haar Cascade do OpenCV
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Tenta detectar a face
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:
        print("Aviso: Nenhuma face detectada.")
        print("O Haar Cascade foi treinado para rostos reais e pode não reconhecer mocks geométricos.")
        # Fallback: normaliza o tamanho da imagem inteira caso não ache um rosto
        face_recortada = cv2.resize(gray, tamanho_padrao)
    else:
        # Pega as coordenadas da primeira face detectada (x, y, largura, altura)
        (x, y, w, h) = faces[0]
        # Recorta a região do rosto e normaliza o tamanho
        face_recortada = gray[y:y+h, x:x+w]
        face_recortada = cv2.resize(face_recortada, tamanho_padrao)
        print("Face detectada e recortada com sucesso!")

    # Salva o resultado
    caminho_saida = caminho_imagem.replace('.png', '_processado.png')
    cv2.imwrite(caminho_saida, face_recortada)
    print(f"Imagem pré-processada salva em: {caminho_saida}")
    
    return face_recortada

if __name__ == "__main__":
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_retrato = os.path.join(diretorio_atual, '..', 'retrato_falado_suspeito.png')
    
    pre_processar_imagem(caminho_retrato)