# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 21:01:10 2023

@author: 57314
"""

import pandas as pd
from sklearn.model_selection import train_test_split
import mlflow
import mlflow.sklearn
from pgmpy.estimators import MaximumLikelihoodEstimator
import mlflow
import mlflow.sklearn
from pgmpy.models import BayesianModel
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from pgmpy.estimators import BayesianEstimator

# Ruta del archivo CSV
ruta_csv = 'datosfiltradosv2.csv'
df = pd.read_csv(ruta_csv)
column_order = ['grupo'] + [col for col in df.columns if col != 'grupo']
df = df[column_order]

# Lista de columnas a quitar
columnas_a_quitar = ['cole_bilingue', 'cole_genero', 'cole_sede_principal','periodo','cole_calendario']

# Eliminar las columnas especificadas
df2 = df.drop(columns=columnas_a_quitar)

# Dividir el conjunto de datos en entrenamiento y prueba

X_train, X_test = train_test_split(df2, test_size=0.2, random_state=43)
y_test = X_test['grupo']
X_test = X_test.drop(columns=['grupo'])

# defina el servidor para llevar el registro de modelos y artefactos
# mlflow.set_tracking_uri('http://0.0.0.0:5000')
experiment = mlflow.set_experiment("sklearn-PR3")

with mlflow.start_run():
    # crear modelo
    edges = [('cole_area_ubicacion', 'cole_depto_ubicacion'),
             ('cole_area_ubicacion', 'cole_caracter'),
             ('cole_area_ubicacion', 'cole_naturaleza'),
             ('cole_depto_ubicacion', 'cole_caracter'),
             ('cole_depto_ubicacion', 'cole_naturaleza'),
             ('cole_depto_ubicacion', 'grupo'),
             ('cole_jornada', 'cole_naturaleza'),
             ('cole_jornada', 'cole_depto_ubicacion'),
             ('cole_jornada', 'grupo'),
             ('cole_jornada', 'cole_caracter'),
             ('cole_jornada', 'cole_area_ubicacion'),
             ('cole_naturaleza', 'cole_caracter'),
             ('cole_naturaleza', 'grupo')]

    modelo1 = BayesianModel(edges)
    # Lista de nombres de variables
    variables = ['grupo', 'cole_area_ubicacion', 'cole_caracter', 'cole_depto_ubicacion', 'cole_jornada', 'cole_naturaleza']

    # Lista de CPDs estimadas
    estimador_bayesiano = BayesianEstimator(modelo1, X_train)
    cpds = [estimador_bayesiano.estimate_cpd(variable) for variable in variables]

    # Añadir las CPDs estimadas al modelo
    modelo1.add_cpds(*cpds)
    
    predictions = modelo1.predict(X_test)
    # reistre el modelo
    mlflow.sklearn.log_model(modelo1, "modelo_bayesiano")
    # Loggear métricas
    accuracy = accuracy_score(y_test, predictions)
    f1_macro = f1_score(y_test, predictions, average='macro')
    f1_micro = f1_score(y_test, predictions, average='micro')
    
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("f1_macro", f1_macro)  # Cambiado de "f1_score" a "f1_macro"
    mlflow.log_metric("f1_micro", f1_micro)  # También puedes registrar f1_micro si es necesario
    print(accuracy)
    print(f1_macro)
    print(f1_micro)