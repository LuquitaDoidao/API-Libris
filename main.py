from flask import Flask
import fdb
from flask_cors import CORS
from datetime import datetime

# ==========================================================
#          CÓDIGO DE DEPURAÇÃO - LISTAR ROTAS
# ==========================================================
# Adicione este bloco ANTES de app.run()


app = Flask(__name__)
CORS(app, origins=["*"])

app.config.from_pyfile('config.py')

# Configurações do banco de dados
host = app.config['DB_HOST']
database = app.config['DB_NAME']
user = app.config['DB_USER']
password = app.config['DB_PASSWORD']

# Conexão com o banco de dados
try:
    con = fdb.connect(host=host, database=database, user=user, password=password)
    print("Conexão estabelecida com sucesso!")
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")



def carregar_configuracoes():
    try:
        cur = con.cursor()

        # Buscar a única linha da tabela CONFIGURACOES
        cur.execute("""
            SELECT RAZAO_SOCIAL, NOME_FANTASIA, MENSAGEM_INSTITUCIONAL,
                TELEFONE, EMAIL, WHATSAPP, CIDADE, BAIRRO, RUA, NUMERO, PIX,
                FACEBOOK, INSTAGRAM, YOUTUBE, X, TIKTOK,
                HORARIO_FUNCIONAMENTO_INICIO, HORARIO_FUNCIONAMENTO_FIM,
                HORARIO_ALMOCO_INICIO, HORARIO_ALMOCO_FIM
            FROM CONFIGURACOES
            WHERE ID_CONFIGURACAO = 1
        """)
        linha_config = cur.fetchone()

        if linha_config:
            app.config['RAZAO_SOCIAL'] = linha_config[0]
            app.config['NOME_FANTASIA'] = linha_config[1]
            app.config['MENSAGEM_INSTITUCIONAL'] = linha_config[2]
            app.config['TELEFONE'] = linha_config[3]
            app.config['EMAIL'] = linha_config[4]
            app.config['WHATSAPP'] = linha_config[5]
            app.config['CIDADE'] = linha_config[6]
            app.config['BAIRRO'] = linha_config[7]
            app.config['RUA'] = linha_config[8]
            app.config['NUMERO'] = linha_config[9]
            app.config['PIX'] = linha_config[10]
            app.config['FACEBOOK'] = linha_config[11]
            app.config['INSTAGRAM'] = linha_config[12]
            app.config['YOUTUBE'] = linha_config[13]
            app.config['X'] = linha_config[14]
            app.config['TIKTOK'] = linha_config[15]
            app.config['HORARIO_FUNC_INICIO'] = linha_config[16]
            app.config['HORARIO_FUNC_FIM'] = linha_config[17]
            app.config['HORARIO_ALMOCO_INICIO'] = linha_config[18]
            app.config['HORARIO_ALMOCO_FIM'] = linha_config[19]
        else:
            print("Nenhuma configuração encontrada.")

    except Exception as e:
        print(f"Erro ao carregar configurações: {e}")

    finally:
        if cur:
            cur.close()



# Carregar as configurações quando a aplicação iniciar
carregar_configuracoes()


from view import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
