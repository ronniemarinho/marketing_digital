import pandas as pd
import numpy as np

# Definindo a quantidade de registros
num_registros = 1000

# Gerando valores para os campos
clienteid = np.arange(1, num_registros + 1)
idade = np.random.randint(18, 81, size=num_registros)
renda_anual = np.zeros(num_registros)  # Inicializa a renda com 0

# Definindo a renda com base na faixa etária
renda_anual[(idade >= 18) & (idade < 30)] = np.random.randint(20000, 40000, size=np.sum((idade >= 18) & (idade < 30)))
renda_anual[(idade >= 30) & (idade < 50)] = np.random.randint(40000, 70000, size=np.sum((idade >= 30) & (idade < 50)))
renda_anual[idade >= 50] = np.random.randint(60000, 100000, size=np.sum(idade >= 50))

# Gerando emails fictícios
emails = [f"cliente{idx}@exemplo.com" for idx in clienteid]

# Criando o DataFrame
dados = pd.DataFrame({
    'clienteid': clienteid,
    'idade': idade,
    'renda_anual': renda_anual,
    'email': emails
})

# Salvando os dados em um arquivo CSV
dados.to_csv('dados_clientes2.csv', index=False)

# Visualizando os primeiros registros
print(dados.head())
