# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 17:30:36 2023

@author: 57314
"""

import pandas as pd
from sklearn.model_selection import train_test_split
import networkx as nx
import matplotlib.pyplot as plt
from pgmpy.estimators import HillClimbSearch, K2Score
from pgmpy.models import BayesianModel

# Ruta del archivo CSV
ruta_csv = r'C:\Users\57314\Documents\universidad\Analitica\proyecto 3\datosfiltradosv2.csv'
df = pd.read_csv(ruta_csv)
column_order = ['grupo'] + [col for col in df.columns if col != 'grupo']
df = df[column_order]


print(df.head())
columnas_a_eliminar = ["periodo", "cole_sede_principal","cole_calendario"]
df = df.drop(columns=columnas_a_eliminar)
print(df.head())
# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test = train_test_split(df, test_size=0.2, random_state=43)

from pgmpy.estimators import HillClimbSearch, K2Score

scoring_method = K2Score ( data =X_train)
esth = HillClimbSearch ( data =X_train)
estimated_modelk = esth.estimate(scoring_method = scoring_method , max_indegree =4 , max_iter =int (1e4))
print(estimated_modelk)
print(estimated_modelk.nodes())
print(estimated_modelk.edges())
print(scoring_method.score(estimated_modelk))


pos = nx.spring_layout(estimated_modelk)
nx.draw(estimated_modelk, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, font_color='black', arrowsize=10)
plt.show()

nodos_ancestros_grupo = set(nx.ancestors(estimated_modelk, "grupo"))
nodos_sin_relacion = set(estimated_modelk.nodes()) - nodos_ancestros_grupo - {"grupo"}
print(f"Nodos sin relación con 'grupo': {nodos_sin_relacion}")
