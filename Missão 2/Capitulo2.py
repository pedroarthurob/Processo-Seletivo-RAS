import cv2 as cv # importação da biblioteca
file_path = './Images/ponte.jpg' # caminho da imagem
imagem = cv.imread(file_path) # leitura da imagem com a função imread()
(b, g, r) = imagem[0, 0] # veja que a ordem BGR e não RGB

print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b) # valores das cores do pixel superior mais a esquerda


imagem = cv.imread(file_path)
# itera sobre cada pixel da imagem
for y in range(0, imagem.shape[0]): #percorre as linhas
    for x in range(0, imagem.shape[1]): #percorre colunas
        imagem[y, x] = (255,0,0) # altera o valor do pixel 
(b, g, r) = imagem[0, 0] # verifica os novos valores das cores do pixel superior mais a esquerda 
print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

cv.imshow("Imagem modificada", imagem) # mostra a imagem alterada
cv.waitKey(0)

imagem = cv.imread(file_path) # recarrega a imagem base para ser feitas novas alterações
# as demais linhas repetem a mesma estrutura, com diferentes mudanças nos pixels
for y in range(0, imagem.shape[0]):
    for x in range(0, imagem.shape[1]):
        imagem[y, x] = (x%256,y%256,x%256)
(b, g, r) = imagem[0, 0]

print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

cv.imshow("Imagem modificada", imagem)
cv.waitKey(0)

imagem = cv.imread(file_path)
for y in range(0, imagem.shape[0], 1): 
    for x in range(0, imagem.shape[1], 1): 
        imagem[y, x] = (0,(x*y)%256,0)
(b, g, r) = imagem[0, 0]

print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

cv.imshow("Imagem modificada", imagem)
cv.waitKey(0)

imagem = cv.imread(file_path)
for y in range(0, imagem.shape[0], 10): 
    for x in range(0, imagem.shape[1], 10): 
        imagem[y:y+5, x: x+5] = (0,255,255)
(b, g, r) = imagem[0, 0]

print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

cv.imshow("Imagem modificada", imagem)
cv.waitKey(0)
