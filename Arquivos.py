
# o conjunto padrao de letras é encoding ask, que contem apenas as letras e simbolos que tem no alfabeto da lingua inglesa
# se quiser usar simbolos e acentros que tem no portugues e espanhol tem que usar encoding utf 8, e no caso dos arquivos manipulados com python 
# devemos salvar eles com o utf-8, 

# se abrir um arquivo no modo write, no arquivo so vai ter o que eu escrevi na ultima mexida, e as coisas salvas anteriores a essa abertura com modo
# write serao perdidas! Mas, se quiser apenas continuar escrevendo sem perder as coisas anteriores, tem que abrir no modo append
# os arquivos do computadores nao ficam na memoria ram, eles permanecem na memoria em que foram salvos, mas apenas os dados dele sao carregados
# quando abrimos ou executamos esse arquivo

# arquivo texto so guarda caracteres de texto, so gaurda caracteres de texto ex: txt, nem linhas graficas pretas nao sao txt, so se for o underline
# arquivo binario, guarda muitas e muitos coisas que nao sao textos, ex: docx, pdf, img, pdf, pptx, xml, excel

# url. universal resource locator


# ler tudo de uma vez

meu_arquivo = open('nomes.txt', mode='r')
conteudo = meu_arquivo.read()
print(conteudo)
meu_arquivo.close()

#ler linha a linha

meu_arquivo2 = open('nomes.txt', mode='r')
for linha in meu_arquivo2:
    print(linha)            # ja incluio '\n'
meu_arquivo2.close()

# sem pular linha extra
meu_arquivo3 = open('nomes.txt', mode='r')
for linha in meu_arquivo3:
    print(linha, end='')    # remove as quebras extras
meu_arquivo3.close()


# CONTAGENS UTEIS--------------------------------

# caracteres
with open('nomes.txt', 'r') as f:       # esse as, é para poder guardar essa abertura desse arquivo nesse modo como a variavel f
    conteudo = f.read()
qtd_caracteres = len(conteudo)
print(f'Chars: {qtd_caracteres}')

# linhas
qtd_linhas = 0
with open('nomes.txt', 'r') as f:
    for _ in f:
        qtd_linhas += 1
print(f'Linhas: {qtd_linhas}')


# com o bloc with, a conxao usando with open, ele fecha automaticamente quadno sai do bloco dele, tambem é assim no bloco with de coisas de requisacao
# com bancos de dados e outros

# o melhor jeito é abrir o arquivo como write apenas na primeira vez, porque se fizer isso na segunda vez, vai perder todos os salvamentos anteriores
# e sobrescrever com o novo

# o browser é inteligente, tanto que ele ja sabe interpretar o que esta guardado nas urls, ex de imagem, de pdf tanto pela web, quanto aberto direto pelo
# disco local


# se for um arquivo binario e eu quiser abrir como r normal, ele vai mostrar uns binarios estranhos e tentará
# abrir em base 64, que é abrir arquivo binario e converter em letras, entao tem que abrir como rb
# read binary