# imagem
FROM python:3.11-slim

# diretório de trabalho
WORKDIR /app

# copiar arquivos para o container
COPY . /app

# instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# expor a porta da aplicação
EXPOSE 5000

# rodar aplicação
CMD ["python", "app.py"]
