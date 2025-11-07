# 1. Usa uma imagem base oficial do Python
FROM python:3.10-slim

# 2. Define o diretório de trabalho dentro do container
WORKDIR /app

# 3. Copia o arquivo de dependências
COPY requirements.txt .

# 4. Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia o código da aplicação
COPY . .

# 6. Expõe a porta que o Flask vai usar
EXPOSE 5000

# 7. Define o comando para rodar a aplicação
CMD ["python", "app.py"]