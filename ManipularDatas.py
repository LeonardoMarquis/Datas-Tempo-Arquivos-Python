
import datetime



data_hoje = datetime.date.today()

dia = data_hoje.day
mes = data_hoje.month
ano = data_hoje.year

print("\n")
print(f"Today is {data_hoje}")
print(f"data_Hoje é {dia}/{mes}/{ano}")


data_hoje_formatado = data_hoje.strftime("%d/%m/%Y")
print(f"data_Hoje é {data_hoje_formatado}")
print("\n")


agora = datetime.datetime.now()
print(f"\nData e hora: {agora}")

agora_formatado = agora.strftime("%d/%m/%Y | %H:%M:%S")
print(f"\nData e hora Formatados: \n{agora_formatado}")
print("\n")


dia_da_week = data_hoje.weekday()        #retorna em ingles
def nome_dia_da_semana(indice):
    match indice:
        case 0:
            return "Segunda-feira"
        case 1:
            return "Terça-feira"
        case 2:
            return "Quarta-feira"
        case 3:
            return "Quinta-feira"
        case 4:
            return "Sexta-feira"
        case 5:
            return "Sabado"
        case 6:
            return "Domingo"
        case _:
            return "Digitaste algo errado!"

print(f"Dia da semana: {nome_dia_da_semana(dia_da_week)}")


# ver datas no futuro e ver datas no passado
data_futuro = data_hoje + datetime.timedelta(days=10)         # avançar 10 dias no futuro
dia_da_semana_data_futuro = nome_dia_da_semana(data_futuro.weekday())

print(f"Daqui 10 dias: {data_futuro}, {dia_da_semana_data_futuro}")


data_passado = data_hoje - datetime.timedelta(days=10)        # voltar 10 dias no passado
dia_da_semana_data_passado = nome_dia_da_semana(data_passado.weekday())

print(f"10 dias atrás: {data_passado}, {dia_da_semana_data_passado}")

