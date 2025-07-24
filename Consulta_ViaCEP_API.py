# Script para consultar dados de um CEP usando a API ViaCEP e salvar em CSV.
#
# Instruções:

# 1. Instale as bibliotecas necessárias antes de rodar este script:
#    pip install requests pandas
#    Requests: https://requests.readthedocs.io/
#    Pandas: https://pandas.pydata.org/docs/
# 2. Execute este script em um terminal Python.
#
# O script solicita o CEP, consulta a API ViaCEP e salva os dados em um arquivo CSV.

import requests
import pandas as pd

# Solicita o CEP ao usuário e remove o traço, se houver
cep = input("Digite o CEP para consulta: ").replace('-', '')

# Validação: CEP deve ter 8 dígitos numéricos
if not (cep.isdigit() and len(cep) == 8):
    print("CEP inválido! Digite exatamente 8 dígitos.")
else:
    try:
        # Consulta a API ViaCEP
        r = requests.get(f"https://viacep.com.br/ws/{cep}/json/", timeout=5)
        r.raise_for_status()  # Gera exceção para erros HTTP
        
        # Tenta processar a resposta como JSON
        try:
            campos = r.json()
        except Exception as e:
            print(f"Erro ao processar resposta da API (não é JSON válido): {e}")
            exit(1)

        # Verifica se o CEP existe na base
        if campos.get('erro'):
            print("CEP não encontrado na base de dados!")
        else:
            # Salva os dados principais em um arquivo CSV
            df = pd.DataFrame([[campos.get("cep"), campos.get("logradouro"), campos.get("complemento"),
                                campos.get("bairro"), campos.get("localidade"), campos.get("uf")]],
                              columns=["cep", "logradouro", "complemento", "bairro", "localidade", "uf"])
            df.to_csv("Resultado_CEP_API.csv", index=False)
            print("Consulta realizada e CSV gerado com sucesso.")
    
    # Se ocorrer algum erro na requisição ou processamento, exibe a mensagem de erro
    except requests.RequestException as e:
        print(f"Erro na requisição: {e}")