# Consulta CEP ViaCEP - Web Scraping e API

Este projeto contém dois scripts em Python para consulta de dados de CEP usando o serviço [ViaCEP](https://viacep.com.br/):
- Um script realiza a consulta via Web Scraping com Selenium.
- Outro script realiza a consulta diretamente pela API ViaCEP com requests.

## Requisitos

- Python 3.7+
- [Selenium](https://selenium.dev/documentation/)
- [Pandas](https://pandas.pydata.org/docs/)
- [Requests](https://requests.readthedocs.io/) (apenas para o script API)
- [ChromeDriver](https://chromedriver.chromium.org/downloads) compatível com seu navegador Chrome (apenas para o script Selenium)

## Instalação das dependências

```bash
pip install selenium pandas requests