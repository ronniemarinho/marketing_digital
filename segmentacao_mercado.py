import pandas as pd
import numpy as np
import random
import string

# Definindo o número de clientes e gerando dados fictícios
num_clientes = 1000
idades = np.random.randint(18, 80, size=num_clientes)
renda_anual = np.random.randint(20000, 200000, size=num_clientes) / 1000  # em milhares de dólares

# Gerando endereços de e-mail aleatórios
def generate_email():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(8)) + '@example.com'

emails = [generate_email() for _ in range(num_clientes)]

# Gerando valores para a coluna "última compra"
ultima_compra = np.random.choice(['celulares', 'móveis', 'eletrodomésticos', 'informática', 'mercado'], size=num_clientes)

# Criando DataFrame com os dados fictícios
dados = pd.DataFrame({
    'ClienteID': range(1, num_clientes + 1),
    'Idade': idades,
    'Renda Anual (milhares de dólares)': renda_anual,
    'Email': emails,
    'Última Compra': ultima_compra
})

# Salvando os dados em um arquivo CSV
dados.to_csv('dados_clientes_teste.csv', index=False)

print("Arquivo 'dados_clientes.csv' criado com sucesso!")
