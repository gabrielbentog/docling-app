# Usa uma imagem base Python oficial leve
FROM python:3.9-slim-buster

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
# Se você não tiver um, crie um com 'docling' dentro
COPY requirements.txt .

# Instala as dependências especificadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia seu script Python para o diretório de trabalho
COPY converter.py .

# Cria os diretórios de input e output
RUN mkdir -p input output

# Define o comando padrão para executar o script quando o contêiner for iniciado
CMD ["python", "converter.py"]