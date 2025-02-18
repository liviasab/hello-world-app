# Usa uma imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de requisitos para o container
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação para o container
COPY . .

# Expõe a porta 8080
EXPOSE 8080

# Comando para rodar a aplicação
CMD ["python", "app.py"]