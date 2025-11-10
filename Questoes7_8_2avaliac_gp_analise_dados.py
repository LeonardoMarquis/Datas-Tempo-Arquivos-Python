import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter


# no collab tem que rodar: !wget 'https://raw.githubusercontent.com/armandossrecife/lp20231/main/top-500-movies.csv'


# Recarregando df_dados_filmes para garantir que esteja definido aqui nessa parte
df_dados_filmes = pd.read_csv('top-500-movies.csv', sep=',', encoding='UTF-8')

# Certifica-se de que a coluna 'year' é numérica e converte para Int64 para lidar com NaNs
df_dados_filmes['year'] = pd.to_numeric(df_dados_filmes['year'], errors='coerce').astype('Int64')

# Remove linhas onde 'year' pode ser NaN após a conversão
df_filtered = df_dados_filmes.dropna(subset=['year']).copy()

# Determina o ano máximo no dataset para definir somente os últimos 25 anos
max_year = df_filtered['year'].max()

# Calcula o ano de início para o período de 25 anos tem um inclusive
start_year = max_year - 24 

# Filtra o DataFrame para incluir apenas os filmes dos últimos 25 anos
df_last_25_years = df_filtered[df_filtered['year'] >= start_year]

# Agrupa os dados por ano e soma a arrecadação mundial para cada ano
bilheteria_por_ano = df_last_25_years.groupby('year')['worldwide_gross'].sum()

# Cria o gráfico de série temporal
plt.figure(figsize=(12, 7))
sns.lineplot(x=bilheteria_por_ano.index, y=bilheteria_por_ano.values, marker='o', color='red')

plt.title(f'Evolução da Arrecadação Mundial por Ano ({start_year}-{max_year})', fontsize=16)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Arrecadação Mundial', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

# Função para formatar os valores do eixo Y em Milhões ou Bilhões
def format_currency(x, pos):
    if x >= 1e9:
        return f'${x*1e-9:.1f}B'  # Bilhões
    elif x >= 1e6:
        return f'${x*1e-6:.0f}M'  # Milhões
    else:
        return f'${x:,.0f}'

# Aplica o formatador ao eixo Y
formatter = FuncFormatter(format_currency)
plt.gca().yaxis.set_major_formatter(formatter)

# Define os ticks do eixo X para mostrar todos os anos e rotaciona para melhor leitura
plt.xticks(bilheteria_por_ano.index.unique().astype(int), rotation=45)
plt.tight_layout()
plt.show()




# quest 8
# 1. Filtra o DataFrame para conter APENAS filmes do gênero 'Action'
filmes_acao = df_dados_filmes[df_dados_filmes['genre'] == 'Action']

# 2. Ordena esses filmes pela bilheteria mundial (do maior para o menor)
acao_top_bilheteria = filmes_acao.sort_values(by='worldwide_gross', ascending=False)

# 3. Pega apenas os 20 primeiros filmes dessa lista
top_20_acao = acao_top_bilheteria.head(20)

# 4. Calcula a média da bilheteria mundial desses 20 filmes
media_bilheteria_mundial_top_20 = top_20_acao['worldwide_gross'].mean()

# Formata o valor como moeda
print(f"A média de arrecadação de bilheteria mundial dos 20 filmes de 'Ação' com maior bilheteria é: ${media_bilheteria_mundial_top_20:,.2f}")