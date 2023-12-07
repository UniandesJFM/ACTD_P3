import dash
from dash import dcc  # dash core components
from dash import html # dash html components
from pgmpy.inference import VariableElimination
import numpy as np
from dash.dependencies import Input, Output, State
from pgmpy.readwrite import BIFReader
import plotly.express as px
from pgmpy.readwrite import  BIFReader
import pandas as pd
#from geopy.geocoders import Nominatim
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
# Read model from XML BIF file 
# Crear un objeto BIFReader y leer el archivo BIF
ruta_bif = r'C:\Users\oem\Documents\universidad de los andes\octavo\Analitica computacional para la toma de decisiones\proyecto 3\modelo1.bif'

bif_reader = BIFReader(ruta_bif)
modelo1 = bif_reader.get_model()
# Print model 
print("bif leido")

# Check_model check for the model structure and the associated CPD and returns True if everything is correct otherwise throws an exception
modelo1.check_model()
infer = VariableElimination(modelo1)

#dash
print("inferencia establecida")

##Visualizaciones
# Datos manualmente insertados
datos = {
    'periodo': ['20194']*8 + ['20201']*8 + ['20211']*8 + ['20221']*8 + ['20224']*8,
    'grupo': ['Grupo 1', 'Grupo 2', 'Grupo 3', 'Grupo 4', 'Grupo 5', 'Grupo 6', 'Grupo 7', 'Grupo 8']*5,
    'cantidad': [200, 5800, 164528, 328794, 277632, 123744, 17832, 634,
                 34, 34, 904, 2147, 3434, 4159, 1835, 129,
                 47, 14, 527, 1702, 3374, 4749, 2227, 246,
                 1, 28, 1162, 2628, 3777, 4981, 2219, 173,
                 242, 1620, 147430, 299896, 268406, 133900, 19714, 990]
}

dfBars = pd.DataFrame(datos)

# Calcular el porcentaje
dfBars['porcentaje'] = dfBars.groupby('periodo')['cantidad'].transform(lambda x: x / x.sum() * 100)


########
panel_1_content = html.Div([
    html.H2("Instrucciones"),
    html.P("Esta aplicacion permite estimar el grupo de puntaje, de la prueba saber 11, de un estudiante segun los atributos del colegio"),
    html.P("Seguirlas siguientes instrucciones:"),
    html.P("1. Diligenciar la informacion requerida, solo se pueden dejar vacias las que la lista desplegable lo permita"),
    html.P("2. click en el boton de ejecutar"),
    html.P("3. los resultados se mostraran en la parte inferior"),
])
panel_2_content = html.Div([
    html.H2("Recoleccion de data"),
    html.P("    "),
    html.Div([  # Agregamos un contenedor para organizar los elementos
        html.H6("cole_area_ubicacion:", style={'display': 'inline-block', 'margin-right': '10px'}),  # Establecemos el estilo inline-block
        dcc.Dropdown(
            id='cole_area_ubicacion',  # Identificador único para la lista desplegable
            options=[
                {'label':'URBANO','value':"URBANO"},
                {'label':'RURAL','value':"RURAL"},
            ],
            multi=False,  # Cambiado a False para permitir una sola selección
            #value=6,  # Opción preseleccionada
            style={'display': 'inline-block','width': '180px'}  # Establecemos el estilo inline-block
        ),
        html.H6("cole_jornada:", style={'display': 'inline-block', 'margin-right': '40px', 'margin-left':'40px'}),  # Establecemos el estilo inline-block
        dcc.Dropdown(
            id='cole_jornada',  # Identificador único para la lista desplegable
            options=[
                {'label':'UNICA','value':"UNICA"},
                {'label':'MAÑANA','value':"MANANA"},
                {'label':'NOCHE','value':"NOCHE"},
                {'label':'TARDE','value':"TARDE"},
                {'label':'SABATINA','value':"SABATINA"},
                {'label':'COMPLETA','value':"COMPLETA"},
            ],
            multi=False,  # Cambiado a False para permitir una sola selección
            #value=5,  # Opción preseleccionada
            style={'display': 'inline-block','width': '200px'}  # Establecemos el estilo inline-block
        ),
        html.H6("cole_naturaleza:", style={'display': 'inline-block', 'margin-right': '10px'}),  # Establecemos el estilo inline-block
        dcc.Dropdown(
            id='cole_naturaleza',  # Identificador único para la lista desplegable
            options=[
                {'label':'OFICIAL','value':"OFICIAL"},
                {'label':'NO OFICIAL','value':"NO_OFICIAL"},
            ],
            multi=False,  # Cambiado a False para permitir una sola selección
            value=0,  # Opción preseleccionada
            style={'display': 'inline-block','width': '200px'}  # Establecemos el estilo inline-block
        ),
        html.H6("cole_bilingue:", style={'display': 'inline-block', 'margin-right': '10px'}),  # Establecemos el estilo inline-block
        dcc.Dropdown(
            id='cole_bilingue',  # Identificador único para la lista desplegable
            options=[
                {'label':'SI','value':"S"},
                {'label':'NO','value':"N"},
            ],
            multi=False,  # Cambiado a False para permitir una sola selección
            value=0,  # Opción preseleccionada
            style={'display': 'inline-block','width': '200px'}  # Establecemos el estilo inline-block
        ),
        html.H6("cole_depto_ubicacion:", style={'display': 'inline-block', 'margin-right': '10px'}),  # Establecemos el estilo inline-block
        dcc.Dropdown(
            id='cole_depto_ubicacion',  # Identificador único para la lista desplegable
            options=[
                {'label':'AMAZONAS','value':"AMAZONAS"},
                {'label':'ANTIOQUIA','value':"ANTIOQUIA"},
                {'label':'ARAUCA','value':"ARAUCA"},
                {'label':'ATLANTICO','value':"ATLANTICO"},
                {'label':'BOGOTÁ','value':"BOGOTA"},
                {'label':'BOLIVAR','value':"BOLIVAR"},
                {'label':'BOYACA','value':"BOYACA"},
                {'label':'CALDAS','value':"CALDAS"},
                {'label':'CAQUETA','value':"CAQUETA"},
                {'label':'CASANARE','value':"CASANARE"},
                {'label':'CAUCA','value':"CAUCA"},
                {'label':'CESAR','value':"CESAR"},
                {'label':'CHOCO','value':"CHOCO"},
                {'label':'CORDOBA','value':"CORDOBA"},
                {'label':'CUNDINAMARCA','value':"CUNDINAMARCA"},
                {'label':'GUAINIA','value':"GUAINIA"},
                {'label':'GUAVIARE','value':"GUAVIARE"},
                {'label':'HUILA','value':"HUILA"},
                {'label':'LA GUAJIRA','value':"LA_GUAJIRA"},
                {'label':'MAGDALENA','value':"MAGDALENA"},
                {'label':'META','value':"META"},
                {'label':'NARIÑO','value':"NARINO"},
                {'label':'NORTE SANTANDER','value':"NORTE_SANTANDER"},
                {'label':'PUTUMAYO','value':"PUTUMAYO"},
                {'label':'QUINDIO','value':"QUINDIO"},
                {'label':'RISARALDA','value':"RISARALDA"},
                {'label':'SAN ANDRES','value':"SAN_ANDRES"},
                {'label':'SANTANDER','value':"SANTANDER"},
                {'label':'SUCRE','value':"SUCRE"},
                {'label':'TOLIMA','value':"TOLIMA"},
                {'label':'VALLE','value':"VALLE"},
                {'label':'VAUPES','value':"VAUPES"},
                {'label':'VICHADA','value':"VICHADA"},
            ],
            multi=False,  # Cambiado a False para permitir una sola selección
            value=0,  # Opción preseleccionada
            style={'display': 'inline-block','width': '200px'}  # Establecemos el estilo inline-block
        ),
        html.H6("cole_caracter:", style={'display': 'inline-block', 'margin-right': '10px'}),  # Establecemos el estilo inline-block
        dcc.Dropdown(
            id='cole_caracter',  # Identificador único para la lista desplegable
            options=[
                {'label':'TÉCNICO','value':"TECNICO"},
                {'label':'ACADÉMICO','value':"ACADEMICO"},
                {'label':'NO APLICA','value':"NO_APLICA"},
                {'label':'TÉCNICO/ACADÉMICO','value':"TECNICO_ACADEMICO"},
            ],
            multi=False,  # Cambiado a False para permitir una sola selección
            value=0,  # Opción preseleccionada
            style={'display': 'inline-block','width': '200px'}  # Establecemos el estilo inline-block
        ),
        html.H6("cole_genero:", style={'display': 'inline-block', 'margin-right': '10px'}),  # Establecemos el estilo inline-block
        dcc.Dropdown(
            id='cole_genero',  # Identificador único para la lista desplegable
            options=[
                {'label':'FEMENINO','value':"FEMENINO"},
                {'label':'MIXTO','value':"MIXTO"},
                {'label':'MASCULINO','value':"MASCULINO"},
            ],
            multi=False,  # Cambiado a False para permitir una sola selección
            value=0,  # Opción preseleccionada
            style={'display': 'inline-block','width': '200px'}  # Establecemos el estilo inline-block
        ),
        
    ], className='panel'),
])

panel_3_content = html.Div([
    html.H2("Resultados"),
    html.P("   "),
])

panel_4_content = html.Div([
    html.H1("About the data"),
    
    # Texto grande
    html.Div([
        html.H2("Cantidad de estudiantes que sacaron más de 300:", style={'font-size': '50px'}),
        html.P(f"19.28%", style={'font-size': '60px'}),
    ]),
    html.Div([
    html.H1("Comportamiento de los grupos por periodo"),
    dcc.Graph(
        figure=px.line(dfBars, x='periodo', y='porcentaje', color='grupo',
                       labels={'porcentaje': 'Porcentaje', 'periodo': 'Periodo', 'grupo': 'Grupo'},
                       
                       line_shape='linear', render_mode='svg')
    )
    ])
])
print("paneles creados")

# Diseño de la aplicación con los paneles
app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Pestaña 1', children=[
            html.H1(children='Predicción de puntaje saber 11'),  # Encabezado principal

            # Contenedor de Paneles
            html.Div([
                panel_1_content,  # Agrega aquí otros paneles si es necesario
                panel_2_content,
            ], className="panel-container"),
            
            # Agrega tus componentes aquí, como el botón y cualquier otra interfaz que desees
            html.Button('Realizar inferencia', id='inferencia-button'),
            
            # Agrega un espacio para mostrar el resultado
            html.Div([
                html.H2("Results"),
                html.P(id='resultado-inferencia'),
            ])
        ]),
        
        # Nueva pestaña para la segunda página
        dcc.Tab(label='Pestaña 2', children=[
            panel_4_content
        ])
    ])
])

print("layout creado")



@app.callback(
    Output('resultado-inferencia', 'children'),
    [Input('inferencia-button', 'n_clicks')],
    [State('cole_area_ubicacion', 'value'),
     State('cole_bilingue', 'value'),
     State('cole_caracter', 'value'),
     State('cole_depto_ubicacion', 'value'),
     State('cole_genero', 'value'),
     State('cole_jornada', 'value'),
     State('cole_naturaleza', 'value'),],
    allow_duplicate=True
)
def realizar_inferencia(n_clicks, cole_area_ubicacion, cole_bilingue, cole_caracter,cole_depto_ubicacion,cole_genero,cole_jornada,cole_naturaleza):
    if n_clicks is None:
        return "Esperando a que se haga clic en el botón..."

    try:
        result = infer.query(
            variables=["grupo"],
            evidence={"cole_area_ubicacion": str(cole_area_ubicacion), "cole_bilingue": str(cole_bilingue),
                      "cole_caracter": str(cole_caracter), "cole_depto_ubicacion": str(cole_depto_ubicacion),
                      "cole_genero": str(cole_genero), "cole_jornada": str(cole_jornada),
                      "cole_naturaleza": str(cole_naturaleza)}
        )
        result_values = result.values
        max_prob_index = np.argmax(result.values)
        max_prob_option = modelo1.get_cpds('grupo').state_names['grupo'][max_prob_index]

        # Obtén el rango de puntajes
        rangos = {
            "Grupo_1": "Entre 0 y 94 puntos",
            "Grupo_2": "Entre 94 y 147 puntos",
            "Grupo_3": "Entre 147 y 199 puntos",
            "Grupo_4": "Entre 199 y 251 puntos",
            "Grupo_5": "Entre 251 y 303 puntos",
            "Grupo_6": "Entre 303 y 355 puntos",
            "Grupo_7": "Entre 355 y 408 puntos",
            "Grupo_8": "Entre 408 y 500 puntos"
        }
        rango_puntaje = rangos.get(max_prob_option, "Rango no definido")

        # Crear la gráfica de barras
        opciones = modelo1.get_cpds('grupo').state_names['grupo']
        probabilidades = result_values.tolist()

        # Crear el mensaje
        mensaje = f"La opción más probable es el {max_prob_option}. El rango de puntajes correspondiente es: {rango_puntaje}"

        # Crear la gráfica de barras
        grafico = {
            'data': [{'x': opciones, 'y': probabilidades, 'type': 'bar'}],
            'layout': {'title': 'Probabilidad de cada opción', 'xaxis': {'title': 'Opciones'},
                       'yaxis': {'title': 'Probabilidad'}}
        }

        return [
            html.Div(mensaje),
            dcc.Graph(figure=grafico),
        ]

    except Exception as e:
        return f"Error durante la inferencia: {str(e)}"


if __name__ == '__main__':
   app.run_server(host = "0.0.0.0", debug = True)
#if __name__ == '__main__':
#    app.run_server(debug=True)
print("fin")