import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ejemplo de DataFrame (reemplazarlo con tus datos)
ruta_csv = r'C:\Users\oem\Documents\universidad de los andes\octavo\Analitica computacional para la toma de decisiones\proyecto 3\datosfiltradosv2.csv'
df = pd.read_csv(ruta_csv)
column_order = ['grupo'] + [col for col in df.columns if col != 'grupo']
df = df[column_order]

# Iterar sobre las columnas diferentes a 'grupo'
for feature in df.columns:
    if feature != 'grupo':
        

        # Crear un DataFrame con los datos necesarios para la visualización
        data_for_plot = df.groupby(['grupo', feature]).size().unstack().apply(lambda x: x / x.sum(), axis=1)

        # Graficar barras apiladas
        ax = data_for_plot.plot(kind='bar', stacked=True, rot=0)

        plt.title(f'Porcentaje de {feature} por grupo')
        plt.xlabel('Grupo')
        plt.ylabel('Porcentaje')

        # Mejorar la visualización de la leyenda
        ax.legend(title=feature, bbox_to_anchor=(1, 1), loc='center', ncol=1, fancybox=True, shadow=True)

        plt.show()
