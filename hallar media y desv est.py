import pandas as pd

# Ruta al archivo CSV
ruta_archivo = r'C:\Users\oem\Documents\universidad de los andes\octavo\Analitica computacional para la toma de decisiones\proyecto 3\datosfiltrados.csv'

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(ruta_archivo)

# Obtener la última columna
ultima_columna = df.iloc[:, -1]

# Calcular la media y la desviación estándar
media = ultima_columna.mean()
desviacion_estandar = ultima_columna.std()

# Imprimir los resultados
print(f'Media: {media}')
print(f'Desviación estándar: {desviacion_estandar}')
