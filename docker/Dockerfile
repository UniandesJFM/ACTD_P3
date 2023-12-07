# Instalar dependencias
RUN apt-get update && apt-get install -y python3 python3-pip

# Crear un directorio de trabajo
WORKDIR /app/

# Copiar archivos necesarios
COPY dashaws.py /app/
COPY modelo1.bif /app/


# Instalar dependencias de Python
RUN pip3 install --upgrade pip
RUN apt-get update && apt-get install -y python3-pip

# Instalar bibliotecas de Python
RUN pip3 install pandas pgmpy
# Instalar bibliotecas de Python
RUN pip3 install pandas pgmpy
RUN pip3 install gunicorn
RUN pip3 install dash
RUN pip3 install matplotlib

# Puerto a exponer para el tablero
EXPOSE 8050

# Comandos a ejecutar al correr el contenedor 
CMD ["python3", "dashaws.py"]