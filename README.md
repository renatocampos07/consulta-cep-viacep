# Consulta ViaCEP - API, Web Scraping e Power Automate

Este projeto contém **3 formas** de consulta de CEP usando o serviço [ViaCEP](https://viacep.com.br/):

---

<details>
<summary>
Consulta via API 
<img src="https://img.icons8.com/color/96/python.png" width="20"/>
Python + Requests
<img src="https://img.icons8.com/color/48/flash-on.png" width="15"/>
</summary>

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
<summary>
Consulta via Web Scraping 
<img src="https://img.icons8.com/color/96/python.png" width="20"/>
Python + Selenium
<img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Selenium_Logo.png" width="15"/>
</summary>

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
<summary> 
Consulta via Power Automate 
<img src="https://img.icons8.com/fluency/96/microsoft-power-automate-2020.png" width="20"/>
Conector Personalizado 🔌

</summary>

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
- **Exportar CSV (opcional):**  
  O fluxo possui uma condição configurada para **gerar CSV apenas se o usuário escolher**.  

</details>

---

## Caso haja erro:

  - **API**: confira se há conexão com a internet ativa 
  - **Scraping**: verifique se ChromeDriver está instalado na versão compatível ao Chrome   
  - **Power Automate**: aceite todas as permissões ao importar o conector personalizado e ao rodar o fluxo
  







