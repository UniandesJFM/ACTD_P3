import pandas as pd
from sklearn.model_selection import train_test_split
import os
from pgmpy.estimators import MaximumLikelihoodEstimator
import matplotlib.pyplot as plt
from pgmpy.readwrite import BIFReader
from pgmpy.models import BayesianNetwork
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from pgmpy.inference import VariableElimination
# Ruta del archivo CSV
ruta_csv = r'C:\Users\oem\Documents\universidad de los andes\octavo\Analitica computacional para la toma de decisiones\proyecto 3\datosfiltradosv2.csv'
df = pd.read_csv(ruta_csv)

column_order = ['grupo'] + [col for col in df.columns if col != 'grupo']
df = df[column_order]

# Lista de columnas a quitar
columnas_a_quitar = ['cole_sede_principal','periodo','cole_calendario']

# Eliminar las columnas especificadas
df2 = df.drop(columns=columnas_a_quitar)

# Dividir el conjunto de datos en entrenamiento y prueba

X_train, X_test = train_test_split(df2, test_size=0.2, random_state=43)
y_test = X_test['grupo']
X_test = X_test.drop(columns=['grupo'])




edges = [('cole_area_ubicacion', 'cole_jornada'), 
         ('cole_area_ubicacion', 'cole_naturaleza'), 
         ('cole_area_ubicacion', 'grupo'), 
         ('cole_bilingue', 'cole_depto_ubicacion'), 
         ('cole_bilingue', 'cole_area_ubicacion'), 
         ('cole_bilingue', 'cole_caracter'), 
         ('cole_bilingue', 'cole_genero'), 
         ('cole_caracter', 'cole_depto_ubicacion'), 
         ('cole_caracter', 'cole_naturaleza'), 
         ('cole_caracter', 'cole_jornada'), 
         ('cole_caracter', 'cole_area_ubicacion'), 
         ('cole_depto_ubicacion', 'cole_jornada'), 
         ('cole_depto_ubicacion', 'cole_naturaleza'), 
         ('cole_depto_ubicacion', 'grupo'), 
         ('cole_depto_ubicacion', 'cole_area_ubicacion'), 
         ('cole_genero', 'cole_depto_ubicacion'), 
         ('cole_genero', 'cole_naturaleza'), 
         ('cole_genero', 'cole_area_ubicacion'), 
         ('cole_genero', 'cole_caracter'), 
         ('cole_jornada', 'grupo'), 
         ('cole_naturaleza', 'cole_jornada'), 
         ('cole_naturaleza', 'grupo')]



modelo1 = BayesianNetwork(edges)

modelo1.fit(data =X_train , estimator = MaximumLikelihoodEstimator)


from pgmpy.readwrite import BIFWriter, BIFReader
from pgmpy.readwrite import XMLBIFWriter
from pgmpy.readwrite import XMLBIFReader


writer = BIFWriter(modelo1)
bif_file_path = r'C:\Users\oem\Documents\universidad de los andes\octavo\Analitica computacional para la toma de decisiones\proyecto 3'
# Corrected line to save the BIF file
writer.write_bif(filename=bif_file_path + "/modelo1.bif")
  


# Ruta del archivo BIF
ruta_bif = r'C:\Users\oem\Documents\universidad de los andes\octavo\Analitica computacional para la toma de decisiones\proyecto 3\modelo1.bif'

# Crear un objeto BIFReader y leer el archivo BIF
bif_reader = BIFReader(ruta_bif)
modelo_bif = bif_reader.get_model()

# Imprimir el modelo BIF
print(modelo_bif)
variables = modelo_bif.nodes()

for variable in variables:
    # Obtén la CPD asociada a la variable
    cpd = modelo_bif.get_cpds(variable)  # Corregido aquí
    
    # Accede a los nombres de los estados de la variable
    posibles_valores = cpd.state_names[variable]
    
    # Imprime los posibles valores
    print(f"Posibles valores para '{variable}': {posibles_valores}")

print(modelo_bif.check_model())
infer = VariableElimination(modelo_bif)

result = infer.query(
            variables=["grupo"],
            evidence={"cole_area_ubicacion": "URBANO", "cole_bilingue": "N", "cole_caracter": "TECNICO", "cole_depto_ubicacion": "NARINO", "cole_genero": "MIXTO", "cole_jornada": "MANANA", "cole_naturaleza": "NO_OFICIAL"}
        )
print(result)