import os
import time
from flask import Flask
import pymysql

app = Flask(__name__)
DB_HOST = os.environ.get('MYSQL_HOST')
DB_USER = os.environ.get('MYSQL_USER')
DB_PASSWORD = os.environ.get('MYSQL_PASSWORD')
DB_NAME = os.environ.get('MYSQL_DB')

def get_db_connection():
    """Tenta conectar ao banco de dados tentando denovo"""
    retries = 10
    while retries > 0:
        try:
            conn = pymysql.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                db=DB_NAME,
                connect_timeout=5
            )
            return conn
        except pymysql.err.OperationalError as e:
            print(f"Erro ao conectar ao DB: {e}")
            retries -= 1
            time.sleep(3)
    return None

@app.route('/')
def hello_world():
    conn = get_db_connection()
    if conn:
        conn.close()
        return (
            "<h1>Bem-vindo ao Gestão Acadêmica Simplificada!</h1>"
            "<p>Aplicação Flask conectada ao banco de dados MySQL com sucesso!</p>"
        )
    else:
        return (
            "<h1>Erro no Ambiente</h1>"
            "<p>Não foi possível conectar ao banco de dados MySQL.</p>"
            f"<p>Verifique as configurações: HOST={DB_HOST}, DB={DB_NAME}</p>"
        ), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)