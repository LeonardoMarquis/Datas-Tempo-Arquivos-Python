#
# MEMORIA RAM
# ------
#      l
#      l
#      l
#      l
# ------         o S.O ja consome a maioria da memoria ram


# quando a memoria ram enche o computador fica mais lento, e a memoria ram tem que fazer um swap, que é 
# jogar pedaços da memoria ram para o disco rigido e pegar memoria do disco para a memoria ram, mas existe uma
# diferenca de velocidade, que é o gargalo de von neuman, ("von noiman"), porque a memoria ram trabalha de e o hdd geralmente de 50 a 160 MB/s e os ssd
# superam 500 MB/s, ja as memorias ram trabalham em velocidades bem maiores


# é hash


try:
    # código que pode dar problema
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    # erro específico
    print("Arquivo não encontrado.")
except Exception as e:
    # erro genérico
    print(f"Ocorreu um erro: {e}")
else:
    # se não deu erro, executa aqui
    print("Leitura concluída com sucesso.")
finally:
    # sempre executa, mesmo se deu erro ou não
    print("Encerrando operação.")
