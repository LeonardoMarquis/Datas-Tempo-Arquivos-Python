# usar numeros randomicos
import random

A = 1
B = 10
numero_inteiro_random = random.randint(A,B)
print("\n")
print(f"Numero aleatorio entre {A} e {B}: {numero_inteiro_random}")


numero_float_random = random.random()
print(f"Numero aleatorio qualquer: {numero_float_random}")


print("\n")
cacadores = ["Tanjiro", "Nezuko", "Inosuke", "Zenitsu", "Aoi", "Kanao", "Murata", "Genya"]
cacadores_hashiras = ["Rengoku", "Shinobu", "Misturi", "Obanai", "Tomioka", "Sanemi", "Uzui", "Gyomei", "Muichiro"]


indice_aleatorio1 = random.randint(0, len(cacadores))
print(f"{cacadores}")
print(f"Cacador sorteado: {cacadores[indice_aleatorio1]}")
print(f"Cacador sorteado REPESCAGEM COM CHOICE(LISTA): {random.choice(cacadores)}")

print("\n")

indice_aleatorio2 = random.randint(0, len(cacadores_hashiras))
print(f"{cacadores_hashiras}")
print(f"Cacador Hashira sorteado: {cacadores_hashiras[indice_aleatorio2]}")


# embaralhar todo
print("\n")
print(f"Antes de embaralhar: {cacadores}")
random.shuffle(cacadores)
print(f"Depois de embaralhar: {cacadores}")