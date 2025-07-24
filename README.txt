# Consulta CEP ViaCEP - Web Scraping e API

Este projeto contém dois scripts em Python para consulta de dados de CEP usando o serviço [ViaCEP](https://viacep.com.br/):
- Um script realiza a consulta via Web Scraping com Selenium.
- Outro script realiza a consulta diretamente pela API ViaCEP com requests.

## Requisitos

- Python 3.7+
- [Pandas](https://pandas.pydata.org/docs/)
- [Requests](https://requests.readthedocs.io/) (apenas para o script API)
- [Selenium](https://selenium.dev/documentation/) (apenas para o script Selenium)
- [ChromeDriver](https://chromedriver.chromium.org/downloads) compatível com seu navegador Chrome (apenas para o script Selenium)

## Instalação das dependências

```bash
pip install selenium pandas requests

## Como executar

- Ao rodar qualquer um dos scripts, será solicitado que você digite um CEP (apenas números, ex: 01001000).

- O resultado será salvo em um arquivo CSV na mesma pasta:
  Resultado_CEP_Scraping.csv para o script de scraping
  Resultado_CEP_API.csv para o script de API

- Exemplo de CEP válido para teste: 01001000:
  Dúvidas ou problemas? Verifique se as dependências estão corretamente instaladas e se o ChromeDriver está no PATH.
  Em caso de erro com o CEP, certifique-se de informar exatamente 8 dígitos numéricos.
