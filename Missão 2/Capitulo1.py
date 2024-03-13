import cv2 as cv # importação da biblioteca

file_path = './Images/RAS.png' # caminho da imagem
imagem = cv.imread(file_path) # leitura da imagem com a função imread()

print('Largura em pixels: ', end='')
print(imagem.shape[1]) # largura da imagem

print('Altura em pixels: ', end='')
print(imagem.shape[0]) # altura da imagem

print('Qtde de canais: ', end='')
print(imagem.shape[2])


cv.imshow("Nome da janela", imagem) # mostra a imagem com a função imshow
cv.waitKey(0) # espera pressionar qualquer tecla para fechar a imagem
cv.imwrite("saida.jpg", imagem) # salva a imagem no disco com função imwrite()

