# Tutorial de como rodar a api
segue abaixo passo a passo para rodar a api :)

## Versão do Python

### Verique se a versão é a .32
- no canto inferior direito, clique no interpretador
- vá em "Select existing"
- se pá é o primeiro, mas tente achar o de 32
- pronto

## Venv

### Cria a venv:
```bash
python -m venv .venv
```

### Entra na venv:
```bash
.\.venv\Scripts\activate
```

## Baixar os paranauê
```bash
pip install -r .\requirements.txt
```
## Observação inportante!!
se der algum erro com o "cur" ou "con" faça isso:

- vá em "config.py"
- mude o "DB_NAME" para o caminho do banco de dados
- dica: vai no DBeaver e copie o caminho lá

## Se ainda der erro
Fale com a Lais ou mande mensagem para este e-mail: laisrscurso@gmail.com


