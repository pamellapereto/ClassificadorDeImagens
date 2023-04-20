import os
import shutil




pastaOrigem = "C:\\Users\\pamel\\Downloads"

pastaDestino = "C:\\Users\\pamel\\Python\\Aula102\\arquivosPython"

listaArquivos = os.listdir(pastaOrigem)

#print(listaArquivos)

for nome_arquivo in listaArquivos:

    nome, extensao = os.path.splitext(nome_arquivo)
    #print(nome)
    #print(extensao)

    if extensao == '':
        continue
    if extensao in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:

        caminho1 = pastaOrigem + '/' + nome_arquivo                        
        caminho2 = pastaDestino + '/' + "arquivos_imagem"                 
        caminho3 = pastaDestino + '/' + "arquivos_imagem" + '/' + nome_arquivo
        #print("caminho1 " , caminho1)
        #print("caminho3 ", caminho3)

        # Verifique se o caminho da pasta/diretório existe antes de mover
        # Caso contrário, crie uma NOVA pasta/diretório, e então mova
        if os.path.exists(caminho2):
          print("Movendo " + nome_arquivo + ".....")

          # Mover de caminho1 ---> caminho3
          shutil.move(caminho1, caminho3)

        else:
          os.makedirs(caminho2)
          print("Movendo " + nome_arquivo + ".....")
          shutil.move(caminho1, caminho3)

