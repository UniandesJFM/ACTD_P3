# Selecciona la imagen base
FROM python:3.10

# Crear usuario que ejecuta el dash
RUN adduser --disabled-password --gecos '' dash-user

# Crear un directorio de trabajo
WORKDIR /app/

# Copiar archivos necesarios
COPY app/dashaws.py .
COPY app/modelo1.bif .

# Instalar dependencias de Python
RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip3 install --upgrade pip && \
    pip3 install  pandas pgmpy gunicorn dash matplotlib

# Puerto a exponer para el tablero
EXPOSE 8050

# Comandos a ejecutar al correr el contenedor 
CMD ["python3", "dashaws.py"]
