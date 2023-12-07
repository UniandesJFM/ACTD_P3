# Selecciona la imagen base
FROM ubuntu:latest

# Crear un directorio de trabajo
WORKDIR /app/

# Copiar archivos necesarios
COPY dashaws.py /app/
COPY modelo1.bif /app/
COPY requirements.txt /app/

# Instalar dependencias de Python
RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

# Puerto a exponer para el tablero
EXPOSE 8050

# Comandos a ejecutar al correr el contenedor 
CMD ["python3", "dashaws.py"]
