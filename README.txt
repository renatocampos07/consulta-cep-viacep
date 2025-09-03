# Consulta CEP ViaCEP - Web Scraping, API e Power Automate

Este projeto contém **3 formas** de consulta de CEP usando o serviço [ViaCEP](https://viacep.com.br/):

---

<details>
<summary>1️⃣ Consulta via Web Scraping (Selenium)</summary>

### Requisitos
- Python 3.7+
- Pandas
- Selenium
- ChromeDriver compatível com seu navegador Chrome

### Instalação
```bash
pip install selenium pandas
```

### Como executar
- Execute `consulta_viacep_scraping.py`
- Digite um CEP (apenas números, ex: `01001000`)
- O resultado será salvo em `Resultado_CEP_Scraping.csv`

</details>

---

<details>
<summary>2️⃣ Consulta via API (Requests)</summary>

### Requisitos
- Python 3.7+
- Pandas
- Requests

### Instalação
```bash
pip install requests pandas
```

### Como executar
- Execute `consulta_viacep_api.py`
- Digite um CEP (apenas números, ex: `01001000`)
- O resultado será salvo em `Resultado_CEP_API.csv`

</details>

---

<details>
<summary>3️⃣ Consulta via Power Automate (Conector Personalizado)</summary>

### Requisitos
- Conta Microsoft Power Automate
- Arquivos do projeto:
  - `viacep_custom_connector.json`
  - `viacep_flow-power-automate.zip`

### Importando o conector
- Vá em **Data > Conectores Personalizados > Importar do arquivo JSON**
- Selecione `viacep_custom_connector.json`
- Salve e crie a conexão

### Importando o fluxo
- Vá em **Meus fluxos > Importar**
- Selecione `viacep_flow-power-automate.zip`
- Configure para usar o conector importado

### Executando
- Clique em **Executar**
- Digite um CEP (apenas números, ex: `01001000`)
- O fluxo retorna os dados do endereço:

```
CEP: 01001-000
Logradouro: Praça da Sé
Complemento: lado ímpar
Bairro: Sé
Localidade: São Paulo
UF: SP
```

</details>

---

## Observações

- Os 3 métodos funcionam como alternativas complementares.  
- Power Automate permite integração nativa com Excel, Teams, SharePoint etc.  
- Exemplo de CEP válido: `01001000`.  
- Caso haja erro:
  - **Scraping**: verifique dependências e se o ChromeDriver está no PATH  
  - **API**: confirme conexão com a internet  
  - **Power Automate**: confira se o conector personalizado foi configurado corretamente  
