
# Script para consultar dados de um CEP usando Selenium no site ViaCEP e salvar em CSV.
#
# Instruções:

# 1. Instale as bibliotecas necessárias antes de rodar este script:
#    pip install selenium pandas
#    Selenium: https://selenium.dev/documentation/
#    Pandas: https://pandas.pydata.org/docs/
# 2. Baixe o ChromeDriver compatível com seu navegador Chrome e coloque o executável no PATH do sistema.
#    (Veja: https://chromedriver.chromium.org/downloads)
# 3. Execute este script em um terminal Python.
#
# O script solicita o CEP, consulta o site ViaCEP e salva os dados em um arquivo CSV.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import json
import pandas as pd

# Solicita o CEP ao usuário e remove o traço, se houver
cep = input("Digite o CEP para consulta: ").replace('-', '')

# Validação: CEP deve ter 8 dígitos numéricos
if not (cep.isdigit() and len(cep) == 8):
    print("CEP inválido! Digite exatamente 8 dígitos.")
else:
    driver = None
    try:
        # Abre o site ViaCEP na página do JSON do CEP
        url = f"https://viacep.com.br/ws/{cep}/json/"
        driver = webdriver.Chrome()
        driver.get(url)
        # Aguarda até 10 segundos pelo elemento <pre> que contém o JSON
        wait = WebDriverWait(driver, 10)
        pre = wait.until(EC.presence_of_element_located((By.TAG_NAME, "pre")))
        campos = json.loads(pre.text)

        # Verifica se o CEP existe na base
        if campos.get('erro'):
            print("CEP não encontrado na base de dados!")
        else:
            # Salva os dados principais em um arquivo CSV
            df = pd.DataFrame([[campos.get("cep"), campos.get("logradouro"), campos.get("complemento"),
                                campos.get("bairro"), campos.get("localidade"), campos.get("uf")]],
                              columns=["cep", "logradouro", "complemento", "bairro", "localidade", "uf"])
            df.to_csv("Resultado_CEP_Scraping.csv", index=False)
            print("Consulta realizada e CSV gerado com sucesso.")
    
    # Se ocorrer algum erro na requisição ou processamento, exibe a mensagem de erro
    except Exception as e:
        print(f"Erro na requisição ou processamento: {e}")

    finally:
        if driver:
            driver.quit()
