
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from pgmpy.estimators import HillClimbSearch, BicScore

# Cargar el CSV en un DataFrame de pandas
ruta_csv = r'C:\Users\oem\Documents\universidad de los andes\octavo\Analitica computacional para la toma de decisiones\proyecto 3\datosfiltradosv2.csv'
df = pd.read_csv(ruta_csv)
column_order = ['grupo'] + [col for col in df.columns if col != 'grupo']
df = df[column_order]

# Lista de columnas a quitar
columnas_a_quitar = ['cole_bilingue', 'cole_genero', 'cole_sede_principal','periodo','cole_calendario']

# Eliminar las columnas especificadas
df2 = df.drop(columns=columnas_a_quitar)

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test = train_test_split(df2, test_size=0.2, random_state=43)

# Estimar el modelo
scoring_method = BicScore(data=X_train)
esth = HillClimbSearch(data=X_train)
estimated_modelb = esth.estimate(scoring_method=scoring_method, max_indegree=4, max_iter=int(1e4))

# Dibujar el grafo
G = nx.DiGraph()
G.add_nodes_from(estimated_modelb.nodes())
G.add_edges_from(estimated_modelb.edges())

# Dibujar el grafo con más separación entre nodos
pos = nx.spring_layout(G, seed=42, k=1.5)  # Ajusta el parámetro k para controlar la separación
nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=1000, font_size=10, arrowsize=20)

# Agregar una etiqueta con el BIC Score del modelo
bic_score_label = f'BIC Score: {scoring_method.score(estimated_modelb):.2f}'
print(bic_score_label )



# Mostrar el dibujo
plt.show()

nodos_ancestros_grupo = set(nx.ancestors(estimated_modelb, "grupo"))
nodos_sin_relacion = set(estimated_modelb.nodes()) - nodos_ancestros_grupo - {"grupo"}
print(f"Nodos sin relación con 'grupo': {nodos_sin_relacion}")